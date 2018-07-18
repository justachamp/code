/*jshint -W030 */
'use strict';

const bloomUtils = require('../../../../src/bloom/utils');

describe('Bloom filter: utils', () => {

  describe('#optimalNumberOfBits()', () => {
    context('when we pass different fpp values', () => {
      it('should return more than zero', function () {
        for (let n = 1; n < 1000; n++) {
          for (let fpp = Number.MIN_VALUE; fpp < 1.0; fpp += 0.001) {
            expect(bloomUtils.optimalNumberOfBits(n, fpp) >= 0).to.equal(true);
          }
        }
      });
    });

    context('when we pass different total insertions number', () => {
      it('should return more than zero', function () {
        let random = Math.random();
        for (let repeats = 0; repeats < 10000; repeats++) {
          expect(bloomUtils.optimalNumberOfBits(Math.ceil(random * (1 << 16)), random) > 0).to.equal(true);
        }
      });
    });

    context('when we pass some crazy values', () => {
      it('should return exact value', function () {
        expect(bloomUtils.optimalNumberOfBits(Math.pow(2, 53) - 1 , 0.01)).to.equal(86334530673272900);
      });
    });

  });

  describe('#optimalNumberOfHashFunctions()', () => {
    context('when we pass different values', () => {
      it('should return more than zero', () => {
        for (let n = 1; n < 1000; n++) {
          for (let m = 0; m < 1000; m++) {
            expect(bloomUtils.optimalNumberOfHashFunctions(n, m) > 0).to.equal(true);
          }
        }
      });

      it('should return concrete values', () => {
        expect(bloomUtils.optimalNumberOfHashFunctions(319, 3072)).to.equal(7);
      });
    });
  });

  describe('#getKey()', () => {
    context('when we pass known date', () => {
      it('should return well formatted value', () => {
        const utcDate = new Date(Date.UTC(2017, 4, 1, 1, 0, 0));
        expect(bloomUtils.getKey(utcDate, '-')).to.equal('2017-05-01-01');
      });
    });
  });


  describe('#getKeys()', () => {
    context('when we pass collection name, date and size', () => {
      it('should return array of keys starting from previous hour', () => {
        const utcDate = new Date(Date.UTC(2017, 4, 1, 1, 0, 0));
        const keys = bloomUtils.getKeys('combined', utcDate, 5);
        const res = [
          'combined_2017-05-01-00',
          'combined_2017-04-30-23',
          'combined_2017-04-30-22',
          'combined_2017-04-30-21',
          'combined_2017-04-30-20'
        ];
        expect(keys).to.eql(res);
      })
    });
  });

});

