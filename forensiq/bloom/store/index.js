"use strict";

const _ = require('lodash');
const debug = require('debug')('bf-store');

const LongStore = require('./long').LongStore;
const ShortStore = require('./short').ShortStore;

const RAW_DIRECTORY = 'bloom_raw';
const MERGED_DIRECTORY = 'bloom_final';
const MERGER_TIMEOUT_INTERVAL = 180;
const DELAY = 1000; // milliseconds

class Store {

  constructor(name, numBits, numHashFunctions, options) {

    options || (options = {});

    const historySize = options.slidingWindowHours - 1; // 1 hour chunk goes to operational buffer
    const timeout = options.mergerTimeoutIntervalSeconds || MERGER_TIMEOUT_INTERVAL;
    const crucialMoment = Math.round(timeout / 60);  // convert seconds to minutes

    this.name = name;
    this.shortStore = new ShortStore({ directory: RAW_DIRECTORY, name, numBits, numHashFunctions });
    this.longStore = new LongStore({ directory: MERGED_DIRECTORY, size: historySize, name, numHashFunctions });

    this.shortStore.configureAdapter(options.storeConfiguration);
    this.longStore.configureAdapter(options.storeConfiguration);

    this.shortSyncCounter = 0;
    this.longSyncsPerHourCounter = 0;

    // set initial minutes on current time to guarantee AWS Lambda merger function invocation on new hour
    this.lastUpdated = new Date();
    this.lastUpdated.setMinutes(crucialMoment, 0);

    if (options.startSyncing) {

      this.loadLongStore();

      this.syncLongInterval = setInterval(() => this.syncLongStore(), options.longStoreSyncIntervalSeconds * DELAY);
      this.syncShortInterval = setInterval(() => this.syncShortStore(), options.shortStoreSyncIntervalSeconds * DELAY);
    }
  }

  loadLongStore() {
    return this.longStore.warmHistoryBuffer()
      .then(keys => {
        keys.forEach(key => {
          if (key) {
            debug(`loadLongStore -> history buffer hold key: ${key}`);
          }
        })
      })
  }

  syncLongStore() {
    const now = new Date();
    const diff = now - this.lastUpdated;
    const HOUR = 60 * 60 * 1000;
    const isHourChanged = diff > HOUR;

    debug(`${this.name}: diff: ${Math.round(diff / (HOUR / 10)) / 10}`);
    debug(`${this.name}: isHourChanged: ${isHourChanged}`);

    let replaceOperationalOnFulfilled = (operationalBuffer) => {
      debug(`replaceOperational -> fulfilled: operational buffer -> ${operationalBuffer.key}`);

      this.longSyncsPerHourCounter++;

      if (isHourChanged) {
        debug(`Hour is changed, it was updated: ${this.longSyncsPerHourCounter} times`);
        this.longStore.pushOperationalToHistory(operationalBuffer);
        this.longSyncsPerHourCounter = 0;
        this.lastUpdated.setHours(this.lastUpdated.getHours() + 1);
      }

      return { isHourChanged };
    };

    let replaceOperationalOnRejected = (err) => {
      debug('replaceOperational -> rejected:', err.message, '->', err['meta']['key']);

      if (isHourChanged) {
        debug(`Hour is changed, it was updated: ${this.longSyncsPerHourCounter} times`);
        this.longStore.pushOperationalToHistory(operationalBuffer);
        this.longSyncsPerHourCounter = 0;
        this.lastUpdated.setHours(this.lastUpdated.getHours() + 1);
      }
    };

    return this.longStore.replaceOperational(this.lastUpdated)
      .then(
        operationalBuffer => replaceOperationalOnFulfilled(operationalBuffer),
        err => replaceOperationalOnRejected(err)
      );
  }

  syncShortStore() {

    this.shortSyncCounter++;

    const current = this.shortStore.getCurrent();

    // check remainder
    if (this.shortSyncCounter % 6 === 0) this.shortStore.rotateBuffer();

    debug(`[${this.name}] -> uploading bloom binary`);

    return this.shortStore.upload(current.buckets)
      .then(data => {
        debug(`[${this.name}] -> shortStore -> upload -> completed -> ${data.key} `);
        return data;
      })
      .catch(err => {
        debug(`[${this.name}] -> shortStore -> upload -> rejected -> ${err}`);

        // if (err.type === 'critical') {
        //   throw err;
        // }

        throw err
      })

  }

  /**
   *
   * @param {string} hash
   * @param {boolean} shouldAdd
   * @return {*}
   */
  check(hash, shouldAdd) {
    return this.shortStore.check(hash, shouldAdd) || this.longStore.check(hash);
  }

}

module.exports = { Store };
