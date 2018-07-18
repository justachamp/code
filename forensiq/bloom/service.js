"use strict";

const cluster = require('cluster');

const _ = require('lodash');
const debug = require('debug')('bf-service');

/* LIBS */
const common = require('../../lib/common');
const tTrack = require('../../lib/time-track');

const CONFIG = require('fq-helper/configReader');

const Store = require('./store').Store;
const bloomUtils = require('./utils');

const IPC_CHANNEL = 'bloomfilter';
const timeTrack = new tTrack.TimeTrack();


/**
 * Find worker by PID
 * @param {number} workerPid - The worker PID value.
 * @return {object} The worker object.
 */
function findWorkerByPid (workerPid) {
  for (let index in cluster.workers) {
    if (cluster.workers[index].process.pid == workerPid) {
      return cluster.workers[index];
    }
  }
}

/**
 * Sending message to a worker (called by master instance)
 * @param {object} message - The message value.
 */
function sendMessageToWorker (message) {
  let worker = findWorkerByPid(message.workerPid);
  worker.send(message);
}

/**
 * Class responsible for receiving messages from worker processes to test the hash
 * and to send result of Bloom Filter test
 * Returns request either: "possibly is suspected duplicate" or "definitely not a duplicate"
 */
class DistributedBloomFilter {

  constructor(options) {

    debug('PID:', process.pid, process.env.NODE_ENV);

    options || (options = {});

    this.config = CONFIG.bloomFilter;
    this.stores = {};

    const storeOptions = {
      slidingWindowHours: _.isUndefined(options.size) ? this.config.slidingWindowHours : options.size,
      startSyncing: _.isUndefined(options.startSyncing) ? this.config.startSyncing : options.startSyncing,
      storeConfiguration: this.config.store,
      mergerTimeoutIntervalSeconds: this.config.mergerTimeoutIntervalSeconds,
      longStoreSyncIntervalSeconds: this.config.longStoreSyncIntervalSeconds,  // fetch and replace every 1 minute
      shortStoreSyncIntervalSeconds: this.config.shortStoreSyncIntervalSeconds // push bloom binary every 5 minutes
    };

    // Please see more info about circular buffers for different request types
    // https://estalea.atlassian.net/wiki/display/FORMRC/Pixel+Requests+De-duplication

    let types = this.config.collections.map(item => {
      const numBits = bloomUtils.optimalNumberOfBits(item.requestsPerHour, item.falsePositiveProbability);
      const numHashFunctions = bloomUtils.optimalNumberOfHashFunctions(item.requestsPerHour, numBits);
      const storeOption = { name: item.name, numBits, numHashFunctions };

      debug(storeOption);

      return storeOption
    });

    types.forEach(type => this.stores[type.name] = new Store(type.name, type.numBits, type.numHashFunctions, storeOptions));

    this.initializeMessageHandler();

  }

  initializeMessageHandler() {

    /**
     * Master incoming messages handler
     * @param {object} message - The message value.
     */
    let messageHandler = message => {
      if (!message || message.channel !== IPC_CHANNEL) return false;

      const col = _.find(this.config.collections, col => _.contains(col.requestTypes, message.data.requestType));
      const bloomTest = this.check(message.data.hash, col);

      // track bloom checks
      timeTrack.trackBloomChecks(message.data.requestType, message.data.clientId);

      if (bloomTest) {
        // track suspected duplicates
        timeTrack.trackSuspectedDuplicates(message.data.requestType, message.data.clientId);
      }

      message.responseParams = { result: bloomTest };

      sendMessageToWorker(message);

    };

    Object.keys(cluster.workers).forEach(workerId => cluster.workers[workerId].on('message', messageHandler));

    cluster.on('fork', worker => worker.on('message', messageHandler));

  }

  /**
   * Get result of Bloom filters testing for the hash from store
   * @param {string} hash - The hash to check value.
   * @param {object} collection - The collection details object
   * @return {boolean} The result of testing against Bloom Filters value.
   */
  check(hash, collection) {
    debug('testing:', hash, 'rt:', collection.name);

    // check by order
    // - current request type testing first

    const res = this.stores[collection.name].check(hash, true);
    if (!res && collection.checkThrough) {
      // check other request types buckets
      return _.some(_.without(_.keys(this.stores), collection.name), rt => this.stores[rt].check(hash, false));
    }

    return res;
  };
}


module.exports = { DistributedBloomFilter };
