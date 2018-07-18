"use strict";

const _ = require('lodash');
const debug = require('debug')('bf-store-long');
const CBuffer = require('CBuffer');
const BloomFilter = require('bloomfilter').BloomFilter;

const Adapter = require('../adapters').Adapter;
const utils = require('../utils');

/**
 * Long and Operating memory
 * This class responsible in fetching Bloom binaries from AWS S3
 *
 * Long (history data) downloaded on app starting and contains not-modifiable data chunks.
 * Operating memory fetching current chunk from a storage every minute
 */
class LongStore {

  constructor(options) {
    this.name = options.name;
    this.directory = options.directory;
    this.numHashFunctions = options.numHashFunctions;

    this.historyBuffer = new CBuffer(options.size);
    this.operationalBuffer = {};

    this.streamingSet = new Set();
    this.adapter = new Adapter();
  }

  configureAdapter(options) {
    this.adapter.configure(options)
  }

  check(hash) {
    const isOperationalContains = (this.operationalBuffer && this.operationalBuffer.bloom)
      ? this.operationalBuffer.bloom.test(hash)
      : false;

    return isOperationalContains || this.historyBuffer.some(item => {
      if (item && item.bloom) {
        debug('checking history buffer item:', item.key);
        return item.bloom.test(hash)
      } else {
        debug('checking history buffer item was empty:', item);
      }
    })

  }

  replaceOperational(date) {
    /**
     *
     * @param bloomChunk
     *   bloomChunk.key: {string}
     *   bloomChunk.etag: {string}
     *   bloomChunk.view: {Uint32Array} }
     * @return {{key, bloom: *, etag}}
     */
    const fetchOnFulfilled = bloomChunk => {
      debug(`adapter fetch -> fulfilled: ${bloomChunk.key}`);

      this.streamingSet.delete(bloomChunk.key);

      let buffer = {};

      try {
        buffer = {
          key: bloomChunk.key,
          bloom: new BloomFilter(bloomChunk.view, this.numHashFunctions),
          etag: bloomChunk.etag
        };

      } catch (err) {
        debug(err);
        throw err;
      }

      this.operationalBuffer = buffer;
      return buffer;
    };

    const fetchOnRejected = err => {
      debug('adapter fetch -> rejected:', err.message, '->', err['meta']['key']);
      if (this.streamingSet.has(err.meta.key)) {
        this.streamingSet.delete(err.meta.key);
      }
      err.meta['bloom'] = this.operationalBuffer && this.operationalBuffer.bloom;
      throw err;
    };

    const key = `${this.name}_${utils.getKey(date)}`;
    debug('adapter fetch ->', key);

    if (this.streamingSet.has(key)) {
      debug('Already fetching same key');
      return Promise.reject(new Error('Already fetching same key'));
    }

    this.streamingSet.add(key);

    let etag = (this.operationalBuffer && this.operationalBuffer.key === key)
      ? this.operationalBuffer.etag
      : undefined;

    return this.adapter.fetch(this.directory, key, etag)
      .then(
        bloomChunk => fetchOnFulfilled(bloomChunk),
        error => fetchOnRejected(error)
      )
  }

  pushOperationalToHistory(item) {
    debug('calling pushOperationalToHistory for:', item.key);
    this.historyBuffer.push(item)
  }

  warmHistoryBuffer() {
    debug('initiate history buffer warming...');

    const keys = utils.getKeys(this.name, new Date(), this.historyBuffer.size);

    const fetchOnFulfilled = (bloomChunk, link) => {
      debug(`adapter fetch -> fulfilled: ${bloomChunk.key}`);

      link.key = bloomChunk.key;
      link.etag = bloomChunk.etag;

      try {
        link.bloom = new BloomFilter(bloomChunk.view, this.numHashFunctions);
      } catch (err) {
        debug(err);
        throw err
      }

      return bloomChunk.key
    };

    const fetchOnRejected = err => {
      debug('adapter fetch -> rejected:', err.message, '->', err['meta']['key']);
    };

    const wrapper = (directory, key, linkTo) => {
      fetchPromises.push(this.adapter.fetch(directory, key)
        .then(
          bloomChunk => fetchOnFulfilled(bloomChunk, linkTo),
          error => fetchOnRejected(error)
        )
      )
    };

    let fetchPromises = [];

    for (let key of keys) {
      this.historyBuffer.push({});
      wrapper(this.directory, key, this.historyBuffer.last());
    }

    return Promise.all(fetchPromises);
  }
}

module.exports = { LongStore };
