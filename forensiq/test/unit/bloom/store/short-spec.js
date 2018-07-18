/*jshint -W030 */
'use strict';

const sinon = require('sinon');

const CONFIG = require('fq-helper/configReader');

const CustomError = require('../../../../../src/bloom/error').CustomError;
const ShortStore = require('../../../../../src/bloom/store/short').ShortStore;


describe('Bloom filter storage: short', function () {

  before(() => {
    this.config = CONFIG.bloomFilter;
  });

  beforeEach(() => {
    const options = {
      name: 'combined',
      directory: 'test/bloom_raw',
      numBits: 1024*1024,
      numHashFunctions: 7
    };

    this.shortStore = new ShortStore(options);
  });

  describe('#check()', () => {

    context('when we just check', () => {
      it('should return false', () => {
        const testingHash = 'request-testing-hash';
        this.shortStore.check(testingHash, false);
        expect(this.shortStore.check(testingHash, false)).to.equal(false);
      });
    });

    context('when we check and add', () => {
      it('should return true', () => {
        const testingHash = 'request-testing-hash';
        this.shortStore.check(testingHash, true);
        expect(this.shortStore.check(testingHash, false)).to.equal(true);
      });
    });

  });

  describe('#addHash()', () => {

    context('when we add hash', () => {
      it('should return true', () => {
        const testingHash = 'request-testing-hash';
        expect(this.shortStore.check(testingHash, false)).to.equal(false);
        this.shortStore.addHash(testingHash);
        expect(this.shortStore.check(testingHash, false)).to.equal(true);
      });
    });

  });

  describe('#rotateBuffer()', () => {

    context('when we rotate buffer 1 time', () => {
      it('should return true', () => {
        const testingHash = 'request-testing-hash';
        expect(this.shortStore.check(testingHash, true)).to.equal(false);
        this.shortStore.rotateBuffer();
        expect(this.shortStore.check(testingHash, false)).to.equal(true);
      });
    });

    context('when we rotate buffer 2 times', () => {
      it('should return false', () => {
        const testingHash = 'request-testing-hash';
        expect(this.shortStore.check(testingHash, true)).to.equal(false);
        this.shortStore.rotateBuffer();
        this.shortStore.rotateBuffer();
        expect(this.shortStore.check(testingHash, false)).to.equal(false);
      });
    });

  });

  describe('#upload()', () => {

    context('when we call upload without proper adapter configuration', () => {
      it('should return CustomError with type: critical', done => {
        const lastBloom = this.shortStore.cbuffer.last();
        const data = lastBloom.buckets;

        const fakeUpload = () => {
          return Promise.reject(new CustomError('critical', 'error message', 'error code'))
        };
        const uploadStub = sinon.stub(this.shortStore.adapter, 'upload').callsFake(fakeUpload);

        this.shortStore.configureAdapter({});

        this.shortStore.upload(data)
          .catch(err => {
            expect(err.type).to.equal('critical');

            uploadStub.restore();
            done();
          });
      });
    });

    context('when we call upload ', () => {
      it('should return specified response', done => {
        const lastBloom = this.shortStore.cbuffer.last();
        const data = lastBloom.buckets;

        let responseSchema = {
          title: 'response schema v1',
          type: 'object',
          required: ['key', 'etag'],
          properties: {
            key: { type: 'string' },
            etag: { type: 'string' }
          }
        };

        const fakeUpload = () => {
          return Promise.resolve({ key: 'some key', etag: 'some etag' })
        };
        const uploadStub = sinon.stub(this.shortStore.adapter, 'upload').callsFake(fakeUpload);

        this.shortStore.configureAdapter(this.config.store);

        this.shortStore.upload(data)
          .then(data => {
            expect(data).to.be.jsonSchema(responseSchema);

            uploadStub.restore();
            done();
          })

      });
    });

  });


});