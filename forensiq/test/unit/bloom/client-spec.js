/*jshint -W030 */
'use strict';

const bloomClient = require('../../../../src/bloom/client');

describe('Bloom filter: сlient', function () {

  describe('_sanityCheck()', function () {

    it('checking that we do not pass sanity checks', function () {
      expect(bloomClient._sanityCheck({ key1: 'some value' }, ['key1', 'key2'])).to.equal(false);
      expect(bloomClient._sanityCheck({ key1: 'some value', key2: '' }, ['key1', 'key2'])).to.equal(false);
      expect(bloomClient._sanityCheck({ key1: 'some value', key2: null }, ['key1', 'key2'])).to.equal(false);
    });

    it('checking that we do pass sanity checks', function () {
      expect(bloomClient._sanityCheck({ key1: 'some value', key2: 'some value' }, ['key1', 'key2'])).to.equal(true);
    });
  });

  describe('Client tests', function () {

    it('Check that client handle empty params as expected', function () {

      let cb = function (err, res) {
        expect(err.message).to.equal('We should provide mandatory params fields');
        expect(res).to.equal(undefined);
      };

      bloomClient.isSuspectedDuplicate({}, cb);
    });

    it('Check that client handle undefined callback as expected', function () {

      expect(bloomClient.isSuspectedDuplicate.bind(bloomClient, {}, undefined))
        .to.throw('We should provide callback function');

    });

    it('Check that client handle params as expected', function () {

      let cb = function (err, res) { };

      let message = bloomClient.isSuspectedDuplicate({ org: '1', s: '2', rt: 'display' }, cb);

      let messageSchema = {
        title: 'message schema v1',
        type: 'object',
        required: ['id', 'channel', 'workerPid', 'data', 'callback'],
        properties: {
          id: { type: 'string' },
          channel: { type: 'string' },
          workerPid: { type: 'number' },
          data: {
            type: 'object',
            required: ['hash', 'requestType', 'clientId'],
            properties: {
              hash: { type: 'string' },
              requestType: { type: 'string' },
              clientId: { type: 'string' }
            }
          },
          callback: { type: 'function' }
        }
      };

      expect(message).to.be.jsonSchema(messageSchema);
    });

  });

});
