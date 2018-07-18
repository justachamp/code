/*jshint -W030 */
'use strict';

const _ = require('lodash');
const sinon = require('sinon');
const BloomFilter = require('bloomfilter').BloomFilter;

const CONFIG = require('fq-helper/configReader');

const LongStore = require('../../../../../src/bloom/store/long').LongStore;
const utils = require('../../../../../src/bloom/utils');

const NUM_BITS = 1024 * 1024;
const NUM_HASH_FUNCTIONS = 7;


describe('Bloom filter storage: long', function () {

  before(() => {
    this.config = CONFIG.bloomFilter;
  });

  beforeEach(() => {
    const options = {
      name: 'combined',
      directory: 'test/bloom_final',
      size: 2,
      numHashFunctions: NUM_HASH_FUNCTIONS
    };

    this.longStore = new LongStore(options);
  });

  describe('#check()', () => {

    context('when we checking on empty buffers', () => {
      it('should return false', () => {
        const testingHash = 'request-testing-hash';
        expect(this.longStore.check(testingHash)).to.equal(false);
      });
    });

    context('when we checking with fulfilled operational buffer', () => {
      it('should return true', () => {
        const testingHash = 'request-testing-hash';
        const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom.add(testingHash);
        this.longStore.operationalBuffer = { key: 'some key', etag: 'some etag', bloom: bloom };
        expect(this.longStore.check(testingHash)).to.equal(true);
        expect(this.longStore.check('unknown-hash')).to.equal(false);
      });
    });

    context('when we checking with fulfilled history buffer', () => {
      it('should return true', () => {
        const testingHash = 'request-testing-hash';
        const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom.add(testingHash);
        this.longStore.historyBuffer.push({ key: 'some history key', etag: 'some etag', bloom: bloom });
        expect(this.longStore.check(testingHash)).to.equal(true);
        expect(this.longStore.check('unknown-hash')).to.equal(false);
      });
    });

    context('when we checking with both buffers, but testing hash in operational only', () => {
      it('should return true for both keys', () => {
        const testingHash = 'request-testing-hash';
        const someHash = 'some-hash';

        const bloom1 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom1.add(testingHash);
        const bloom2 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom2.add(someHash);

        this.longStore.operationalBuffer = { key: 'some operational key', etag: 'some etag', bloom: bloom1 };
        this.longStore.historyBuffer.push({ key: 'some history key', etag: 'some etag', bloom: bloom2 });

        expect(this.longStore.check(testingHash)).to.equal(true);
        expect(this.longStore.check(someHash)).to.equal(true);
        expect(this.longStore.check('unknown-hash')).to.equal(false);
      });
    });

  });

  describe('#replaceOperational()', () => {

    context('adding key to streaming set', () => {
      it('should catch specified error', done => {
        const date = new Date();
        const key = `${this.longStore.name}_${utils.getKey(date)}`;
        this.longStore.streamingSet.add(key);
        this.longStore.replaceOperational(date)
          .catch(err => {
            expect(err.message).to.equal('Already fetching same key');
            done();
          });
      });
    });

    context('negative flow during first call', () => {
      it('should catch undefined bloom attribute', done => {
        const date = new Date();
        const key = `${this.longStore.name}_${utils.getKey(date)}`;

        const fakeFetch = () => {
          expect(this.longStore.streamingSet.has(key)).to.equal(true);
          return Promise.reject({ meta : { key: key }, message: 'some message' })
        };

        const fetchStub = sinon.stub(this.longStore.adapter, 'fetch').callsFake(fakeFetch);

        expect(this.longStore.streamingSet.has(key)).to.equal(false);

        this.longStore.replaceOperational(date)
          .catch(err => {
            expect(this.longStore.streamingSet.has(key)).to.equal(false);
            expect(err.meta.key).to.equal(key);
            expect(_.isUndefined(err.meta.bloom)).to.equal(true);
            fetchStub.restore();

            done();
          });

      });
    });

    context('negative flow when operational buffer were initialised with Bloom filter', () => {
      it('should catch bloom attribute with Bloom filter', done => {
        const date = new Date();
        const key = `${this.longStore.name}_${utils.getKey(date)}`;

        const fakeFetch = () => {
          expect(this.longStore.streamingSet.has(key)).to.equal(true);
          return Promise.reject({ meta : { key: key }, message: 'some message' })
        };

        const fetchStub = sinon.stub(this.longStore.adapter, 'fetch').callsFake(fakeFetch);

        const testingHash = 'request-testing-hash';
        const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom.add(testingHash);
        this.longStore.operationalBuffer = { key: 'some key', etag: 'some etag', bloom: bloom };

        expect(this.longStore.streamingSet.has(key)).to.equal(false);

        this.longStore.replaceOperational(date)
          .catch(err => {
            expect(this.longStore.streamingSet.has(key)).to.equal(false);
            expect(err.meta.key).to.equal(key);
            expect(err.meta.bloom.test(testingHash)).to.equal(true);
            fetchStub.restore();

            done()
          });

      });
    });

    context('positive flow', () => {
      it('should catch undefined bloom attribute', done => {
        const date = new Date();
        const key = `${this.longStore.name}_${utils.getKey(date)}`;
        const etag = 'some etag';
        const testingHash = 'request-testing-hash';

        const fakeFetch = () => {
          expect(this.longStore.streamingSet.has(key)).to.equal(true);

          const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
          bloom.add(testingHash);
          return Promise.resolve({ key: key, view: bloom.buckets, etag: etag })
        };

        const fetchStub = sinon.stub(this.longStore.adapter, 'fetch').callsFake(fakeFetch);

        expect(this.longStore.streamingSet.has(key)).to.equal(false);

        this.longStore.replaceOperational(date)
          .then(data => {
            expect(this.longStore.streamingSet.has(key)).to.equal(false);
            expect(data.key).to.equal(key);
            expect(data.etag).to.equal(etag);
            expect(data.bloom.test(testingHash)).to.equal(true);

            fetchStub.restore();
            done();
          })
          .catch(err => done(err));

      });
    });
  });

  describe('#pushOperationalToHistory()', () => {
    const testingHash1 = 'request-testing-hash-1';
    const testingHash2 = 'request-testing-hash-2';
    const testingHash3 = 'request-testing-hash-3';

    context('adding item to history (size = 2) 1 time', () => {
      it('should return true', () => {

        const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom.add(testingHash1);

        const item = { key: 'some key', bloom: bloom, etag: 'some etag' };
        this.longStore.pushOperationalToHistory(item);

        expect(this.longStore.check(testingHash1)).to.equal(true);

      });
    });

    context('adding item to history (size = 2) 2 times', () => {
      it('should return true for both', () => {

        const bloom1 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom1.add(testingHash1);
        const item1 = { key: 'some key', bloom: bloom1, etag: 'some etag' };

        const bloom2 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom2.add(testingHash2);
        const item2 = { key: 'some key', bloom: bloom2, etag: 'some etag' };

        this.longStore.pushOperationalToHistory(item1);
        this.longStore.pushOperationalToHistory(item2);

        expect(this.longStore.check(testingHash1)).to.equal(true);
        expect(this.longStore.check(testingHash2)).to.equal(true);
      });
    });

    context('adding item to history (size = 2) 3 times', () => {
      it('should return false for the first hash', () => {

        const bloom1 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom1.add(testingHash1);
        const item1 = { key: 'some key', bloom: bloom1, etag: 'some etag' };

        const bloom2 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom2.add(testingHash2);
        const item2 = { key: 'some key', bloom: bloom2, etag: 'some etag' };

        const bloom3 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
        bloom3.add(testingHash3);
        const item3 = { key: 'some key', bloom: bloom3, etag: 'some etag' };

        this.longStore.pushOperationalToHistory(item1);
        this.longStore.pushOperationalToHistory(item2);
        this.longStore.pushOperationalToHistory(item3);

        expect(this.longStore.check(testingHash1)).to.equal(false);
        expect(this.longStore.check(testingHash2)).to.equal(true);
        expect(this.longStore.check(testingHash3)).to.equal(true);
      });
    });
  });

  describe('#warmHistoryBuffer()', () => {

    context('when calling with network delay simulation', () => {
      it('should return filled history buffer with correct ordering', (done) => {

        const historySize = this.config.slidingWindowHours - 1; // 1 hour chunk goes to operational buffer

        const options = {
          name: 'combined',
          directory: 'test/bloom_final',
          size: historySize,
          numHashFunctions: NUM_HASH_FUNCTIONS
        };

        this.longStore = new LongStore(options);

        const fakeFetch = (prefix, key) => {
          const bloom = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS);
          const data = { key: key, view: bloom.buckets, etag: 'some etag' };

          return new Promise(resolve => setTimeout(() => resolve(data), Math.random() * 1000));
        };

        const fetchStub = sinon.stub(this.longStore.adapter, 'fetch').callsFake(fakeFetch);

        expect(this.longStore.historyBuffer.length).to.equal(0);

        this.longStore.warmHistoryBuffer()
          .then(data => {

            const keys = _.pluck(this.longStore.historyBuffer.toArray(), 'key');
            const sortedKeys = _.pluck(_.sortBy(this.longStore.historyBuffer.toArray(), 'key'), 'key').reverse();

            expect(data.length).to.equal(historySize);
            expect(this.longStore.historyBuffer.length).to.equal(historySize);
            expect(keys).to.eql(sortedKeys);

            fetchStub.restore();
            done()
          })
          .catch(err => done(err))

      });
    });

  });

});