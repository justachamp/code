/*jshint -W030 */
'use strict';

const bloomService = require('../../../../src/bloom/service');

describe('Bloom filter: service', () => {

  describe('Testing different request types', () => {

    const combinedCol = {
      name: "combined",
      requestTypes: [ "display", "displayImg" ],
      requestsPerHour: 80000000,
      falsePositiveProbability: 0.01,
      checkThrough: true
    };

    const displayResCol = {
      name: "displayRes",
      requestTypes: [ "displayRes" ],
      requestsPerHour: 40000000,
      falsePositiveProbability: 0.01,
      checkThrough: false
    };

    context('when we get combined request', () => {
      it('should return check result for displayRes as not duplicates', function () {

        const testingHash = 'request-testing-hash';

        let bloom = new bloomService.DistributedBloomFilter({ size: 1, startSyncing: false });

        const containsCombined1 = bloom.check(testingHash, combinedCol);
        const containsCombined2 = bloom.check(testingHash, combinedCol);
        const containsDisplayRes = bloom.check(testingHash, displayResCol);

        expect(containsCombined1).to.equal(false);
        expect(containsCombined2).to.equal(true);
        expect(containsDisplayRes).to.equal(false);
      });
    });

    context('when we get displayRes request', () => {
      it('should return check result all as duplicates', function () {

        const testingHash = 'request-testing-hash';

        let bloom = new bloomService.DistributedBloomFilter({ size: 1, startSyncing: false });

        const containsDisplayRes1 = bloom.check(testingHash, displayResCol);
        const containsDisplayRes2 = bloom.check(testingHash, displayResCol);
        const containsCombined = bloom.check(testingHash, combinedCol);

        expect(containsDisplayRes1).to.equal(false);
        expect(containsDisplayRes2).to.equal(true);
        expect(containsCombined).to.equal(true);
      })
    });

  });

});
