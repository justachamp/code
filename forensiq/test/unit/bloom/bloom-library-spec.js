/*jshint -W030 */
'use strict';

const _ = require('lodash');
const BloomFilter = require('bloomfilter').BloomFilter;

const bloomUtils = require('../../../../src/bloom/utils');


describe('Bloom filter: bloom library', function () {

  describe('testing BloomFilter()', function () {

    this.timeout(30 * 1000); // override default timeout value (2000ms)

    before(function() {
      this.numInsertions = 1000000;
      this.fpp = 0.03;

      let m = bloomUtils.optimalNumberOfBits(this.numInsertions, this.fpp);
      let k = bloomUtils.optimalNumberOfHashFunctions(this.numInsertions, m);

      this.bf = new BloomFilter(m, k);

      // Estimated cardinality should be zero.
      expect(this.bf.size()).to.equal(0);

      // Insert "numInsertions" even numbers into the BF.
      for (let i = 0; i < this.numInsertions * 2; i += 2) {
        this.bf.add(i.toString());
      }

      let x = Math.exp(this.bf.size() * (k / m)) - 1;

      expect(x > 0).to.equal(true);
      expect(x < 1).to.equal(true);

    });

    it('Assert that the BF "might" have all of the even numbers.', function () {
      for (let j = 0; j < this.numInsertions * 2; j += 2) {
        expect(this.bf.test(j.toString())).to.equal(true);
      }
    });

    it('Check for known false positives using a set of known false positives.', function () {
      // (These are all of the false positives under 900.)
      let falsePositives = [49, 51, 59, 163, 199, 321, 325, 363, 367, 469, 545, 561, 727, 769, 773, 781];
      for (let i = 1; i < 900; i += 2) {
        if (_.contains(falsePositives, i)) {
          expect(this.bf.test(i.toString())).to.equal(false);
        }
      }
    });

    it('Check that there are exactly 29967 false positives for this BF.', function () {
      let knownNumberOfFalsePositives = 29967;
      let numFpp = 0;
      for (let i = 1; i < this.numInsertions * 2; i += 2) {
        if (this.bf.test(i.toString())) {
          numFpp++;
        }
      }
      expect(numFpp).to.equal(knownNumberOfFalsePositives);

      let actualFpp = numFpp / this.numInsertions;  //0.029967
      expect(Math.round(actualFpp*100)/100).to.equal(this.fpp);
    });

  });

});

