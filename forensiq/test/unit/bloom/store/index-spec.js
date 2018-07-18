/*jshint -W030 */
'use strict';

const _ = require('lodash');
const sinon = require('sinon');
const MockDate = require('mockdate');
const BloomFilter = require('bloomfilter').BloomFilter;

const CONFIG = require('fq-helper/configReader');

const Store = require('../../../../../src/bloom/store/index').Store;
const ShortStore = require('../../../../../src/bloom/store/short').ShortStore;
const LongStore = require('../../../../../src/bloom/store/long').LongStore;
const utils = require('../../../../../src/bloom/utils');

const NAME = 'test';
const NUM_BITS = 1024 * 1024;
const NUM_HASH_FUNCTIONS = 7;


const options = {
  slidingWindowHours: 4,
  mergerTimeoutIntervalSeconds: 180,
  storeConfiguration: {},
  startSyncing: false
};

const testingHash1 = 'request-testing-hash-1';
const testingHash2 = 'request-testing-hash-2';
const testingHash3 = 'request-testing-hash-3';
const testingHash4 = 'request-testing-hash-4';
const testingHash5 = 'request-testing-hash-5';
const testingHash6 = 'request-testing-hash-6';
const testingHash7 = 'request-testing-hash-7';


describe('Bloom filter storage: index', function () {
  this.timeout(5 * 1000); // override default timeout value (2000ms)
  this.binaries = [];

  before(() => {
    let someDate = new Date();
    someDate.setHours(someDate.getHours() + 4);
    // generating +- 3 hours from current time keys array
    const historyKeys = utils.getKeys(NAME, someDate, 7);

    const bloom1 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // -3
    const bloom2 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // -2
    const bloom3 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // -1
    const bloom4 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // current
    const bloom5 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // +1
    const bloom6 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // +2
    const bloom7 = new BloomFilter(NUM_BITS, NUM_HASH_FUNCTIONS); // +3

    bloom1.add(testingHash1);
    bloom2.add(testingHash2);
    bloom3.add(testingHash3);
    bloom4.add(testingHash4);
    bloom5.add(testingHash5);
    bloom6.add(testingHash6);
    bloom7.add(testingHash7);

    this.binaries.push({ key: historyKeys[6], bloom: bloom1, etag: 'some etag 1' });
    this.binaries.push({ key: historyKeys[5], bloom: bloom2, etag: 'some etag 2' });
    this.binaries.push({ key: historyKeys[4], bloom: bloom3, etag: 'some etag 3' });
    this.binaries.push({ key: historyKeys[3], bloom: bloom4, etag: 'some etag 4' });
    this.binaries.push({ key: historyKeys[2], bloom: bloom5, etag: 'some etag 5' });
    this.binaries.push({ key: historyKeys[1], bloom: bloom6, etag: 'some etag 6' });
    this.binaries.push({ key: historyKeys[0], bloom: bloom7, etag: 'some etag 7' });

    this.binariesKeys = _.pluck(this.binaries, 'key');
    // console.log('binariesKeys:', this.binariesKeys);

    this.fakeFetch = (prefix, key, etag) => {
      const item = _.where(this.binaries, { key: key })[0];
      const data = { key: key, view: item.bloom.buckets, etag: item.etag };

      return new Promise(resolve => setTimeout(() => resolve(data), Math.random() * 10));
    };

    this.fakeUpload = (prefix, data, meta) => {
      return new Promise(resolve => setTimeout(() => resolve({ key: 'some key'}), Math.random() * 10))
    }
  });

  beforeEach(() => {
    this.store = new Store(NAME, NUM_BITS, NUM_HASH_FUNCTIONS, options);
  });

  describe('test store warmHistoryBuffer with one syncLongStore', () => {

    context('when we fetch binary history and operational buffers', () => {
      it('should get correct store.check() results', (done) => {

        expect(this.store.name).to.equal(NAME);
        expect(this.store.shortStore).be.instanceOf(ShortStore);
        expect(this.store.longStore).be.instanceOf(LongStore);

        expect(this.store.check(testingHash1, false)).to.equal(false);
        expect(this.store.check(testingHash2, false)).to.equal(false);
        expect(this.store.check(testingHash3, false)).to.equal(false);
        expect(this.store.check(testingHash4, false)).to.equal(false);
        expect(this.store.check(testingHash5, false)).to.equal(false);
        expect(this.store.check(testingHash6, false)).to.equal(false);
        expect(this.store.check(testingHash7, false)).to.equal(false);

        this.fetchStub = sinon.stub(this.store.longStore.adapter, 'fetch').callsFake(this.fakeFetch);

        this.store.loadLongStore()
          .then(() => {
            expect(this.store.check(testingHash1, false)).to.equal(true);
            expect(this.store.check(testingHash2, false)).to.equal(true);
            expect(this.store.check(testingHash3, false)).to.equal(true);
            expect(this.store.check(testingHash4, false)).to.equal(false);
            expect(this.store.check(testingHash5, false)).to.equal(false);
            expect(this.store.check(testingHash6, false)).to.equal(false);
            expect(this.store.check(testingHash7, false)).to.equal(false);

            this.store.syncLongStore()
              .then(data => {
                expect(this.store.check(testingHash1, false)).to.equal(true);
                expect(this.store.check(testingHash2, false)).to.equal(true);
                expect(this.store.check(testingHash3, false)).to.equal(true);
                expect(this.store.check(testingHash4, false)).to.equal(true);
                expect(this.store.check(testingHash5, false)).to.equal(false);
                expect(this.store.check(testingHash6, false)).to.equal(false);
                expect(this.store.check(testingHash7, false)).to.equal(false);

                this.fetchStub.restore();
                done();
              })
              .catch(err => done(err))
          })
          .catch(err => done(err))
      });
    });
  });

  describe('#syncLongStore()', () => {

    context('when we make 2 calls per hour', () => {
      it('should return correct results', (done) => {

        this.fetchStub = sinon.stub(this.store.longStore.adapter, 'fetch').callsFake(this.fakeFetch);

        let someDate = new Date();
        someDate.setMinutes(4, 0); // set minutes more then mergerTimeoutIntervalSeconds config option

        // current hour sync
        this.store.syncLongStore()
          .then(data => {
            expect(data.isHourChanged).to.equal(false);

            expect(this.store.check(testingHash1)).to.equal(false);
            expect(this.store.check(testingHash2)).to.equal(false);
            expect(this.store.check(testingHash3)).to.equal(false);
            expect(this.store.check(testingHash4)).to.equal(true);
            expect(this.store.check(testingHash5)).to.equal(false);
            expect(this.store.check(testingHash6)).to.equal(false);
            expect(this.store.check(testingHash7)).to.equal(false);

            expect(this.store.longStore.historyBuffer.length).to.equal(0);
            expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[3]);

            someDate.setHours(someDate.getHours() + 1);
            MockDate.set(someDate);

            // +1 hour from current sync
            this.store.syncLongStore()
              .then(data => {
                expect(data.isHourChanged).to.equal(true); // can be false if minutes is in interval 0..3

                expect(this.store.check(testingHash1, false)).to.equal(false);
                expect(this.store.check(testingHash2, false)).to.equal(false);
                expect(this.store.check(testingHash3, false)).to.equal(false);
                expect(this.store.check(testingHash4, false)).to.equal(true);
                expect(this.store.check(testingHash5, false)).to.equal(false);
                expect(this.store.check(testingHash6, false)).to.equal(false);
                expect(this.store.check(testingHash7, false)).to.equal(false);

                expect(this.store.longStore.historyBuffer.length).to.equal(1);

                const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                expect(keys).to.eql(this.binariesKeys.slice(3, 4));
                expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[3]);

                // +1 hour from current sync repeat
                this.store.syncLongStore()
                  .then(data => {
                    expect(data.isHourChanged).to.equal(false);

                    expect(this.store.check(testingHash1, false)).to.equal(false);
                    expect(this.store.check(testingHash2, false)).to.equal(false);
                    expect(this.store.check(testingHash3, false)).to.equal(false);
                    expect(this.store.check(testingHash4, false)).to.equal(true);
                    expect(this.store.check(testingHash5, false)).to.equal(true);
                    expect(this.store.check(testingHash6, false)).to.equal(false);
                    expect(this.store.check(testingHash7, false)).to.equal(false);

                    expect(this.store.longStore.historyBuffer.length).to.equal(1);

                    const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                    expect(keys).to.eql(this.binariesKeys.slice(3, 4));
                    expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[4]);

                    someDate.setHours(someDate.getHours() + 1);
                    MockDate.set(someDate);

                    // +2 hours sync
                    this.store.syncLongStore()
                      .then(data => {
                        expect(data.isHourChanged).to.equal(true);

                        expect(this.store.check(testingHash1, false)).to.equal(false);
                        expect(this.store.check(testingHash2, false)).to.equal(false);
                        expect(this.store.check(testingHash3, false)).to.equal(false);
                        expect(this.store.check(testingHash4, false)).to.equal(true);
                        expect(this.store.check(testingHash5, false)).to.equal(true);
                        expect(this.store.check(testingHash6, false)).to.equal(false);
                        expect(this.store.check(testingHash7, false)).to.equal(false);

                        expect(this.store.longStore.historyBuffer.length).to.equal(2);

                        const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                        expect(keys).to.eql(this.binariesKeys.slice(3, 5));
                        expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[4]);

                        // +2 hours sync repeat
                        this.store.syncLongStore()
                          .then(data => {
                            expect(data.isHourChanged).to.equal(false);

                            expect(this.store.check(testingHash1, false)).to.equal(false);
                            expect(this.store.check(testingHash2, false)).to.equal(false);
                            expect(this.store.check(testingHash3, false)).to.equal(false);
                            expect(this.store.check(testingHash4, false)).to.equal(true);
                            expect(this.store.check(testingHash5, false)).to.equal(true);
                            expect(this.store.check(testingHash6, false)).to.equal(true);
                            expect(this.store.check(testingHash7, false)).to.equal(false);

                            expect(this.store.longStore.historyBuffer.length).to.equal(2);

                            const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                            expect(keys).to.eql(this.binariesKeys.slice(3, 5));
                            expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[5]);

                            someDate.setHours(someDate.getHours() + 1);
                            MockDate.set(someDate);

                            // +3 hours sync
                            this.store.syncLongStore()
                              .then(data => {
                                expect(data.isHourChanged).to.equal(true);

                                expect(this.store.check(testingHash1, false)).to.equal(false);
                                expect(this.store.check(testingHash2, false)).to.equal(false);
                                expect(this.store.check(testingHash3, false)).to.equal(false);
                                expect(this.store.check(testingHash4, false)).to.equal(true);
                                expect(this.store.check(testingHash5, false)).to.equal(true);
                                expect(this.store.check(testingHash6, false)).to.equal(true);
                                expect(this.store.check(testingHash7, false)).to.equal(false);

                                expect(this.store.longStore.historyBuffer.length).to.equal(3);

                                const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                                expect(keys).to.eql(this.binariesKeys.slice(3, 6));
                                expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[5]);

                                // +3 hours sync repeat
                                this.store.syncLongStore()
                                  .then(data => {
                                    expect(data.isHourChanged).to.equal(false);

                                    expect(this.store.check(testingHash1, false)).to.equal(false);
                                    expect(this.store.check(testingHash2, false)).to.equal(false);
                                    expect(this.store.check(testingHash3, false)).to.equal(false);
                                    expect(this.store.check(testingHash4, false)).to.equal(true);
                                    expect(this.store.check(testingHash5, false)).to.equal(true);
                                    expect(this.store.check(testingHash6, false)).to.equal(true);
                                    expect(this.store.check(testingHash7, false)).to.equal(true);

                                    expect(this.store.longStore.historyBuffer.length).to.equal(3);

                                    const keys = _.pluck(this.store.longStore.historyBuffer.toArray(), 'key');
                                    expect(keys).to.eql(this.binariesKeys.slice(3, 6));
                                    expect(this.store.longStore.operationalBuffer.key).to.equal(this.binariesKeys[6]);


                                    done();
                                  })
                                  .catch(err => done(err))

                              })
                              .catch(err => done(err))
                          })
                          .catch(err => done(err))

                      })
                      .catch(err => done(err))

                  })
                  .catch(err => done(err))

              })
              .catch(err => done(err))

          })
          .catch(err => done(err))

      });
    });
  });

  describe('#syncShortStore()', () => {

    context('when we make 12 calls (simulate 12 calls per hour)', () => {
      it('should return correct results', (done) => {

        const uploadStub = sinon.stub(this.store.shortStore.adapter, 'upload').callsFake(this.fakeUpload);

        const rotateBufferSpy = sinon.spy(this.store.shortStore, "rotateBuffer");

        let promises = [];

        for(let i = 0; i < 12; i++) {
          promises.push(this.store.syncShortStore())
        }

        Promise.all(promises)
          .then(values => {
            expect(uploadStub.callCount).to.equal(12);
            expect(rotateBufferSpy.callCount).to.equal(2);
            rotateBufferSpy.restore();
            uploadStub.restore()

            done()
          })
          .catch(err => done(err))
      });
    });
  });

});