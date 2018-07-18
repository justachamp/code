"use strict";

const _ = require('lodash');
const debug = require('debug')('bf-store-short');
const CBuffer = require('CBuffer');
const BloomFilter = require('bloomfilter').BloomFilter;

const Adapter = require('../adapters').Adapter;

const RAW_BUCKETS = 2;

/**
 * Short memory
 * This class responsible in uploading current hour Bloom binaries to AWS S3
 *
 * Short memory contains two rotated local chunks for current hour.
 */
class ShortStore {

  constructor(options) {
    this.name = options.name;
    this.keyPrefix = `${options.directory}/${this.name}`;
    this.numBits = options.numBits;
    this.numHashFunctions = options.numHashFunctions;

    this.cbuffer = new CBuffer(RAW_BUCKETS);
    this.cbuffer.push(new BloomFilter(this.numBits, this.numHashFunctions));

    this.adapter = new Adapter();
  }

  configureAdapter(options) {
    this.adapter.configure(options)
  }

  /**
   * Check and add hash to short storage circular buffer
   * @param {string } hash - string that we are checking
   * @param {boolean} shouldAdd - flag to turn on adding hash to buffer
   * @return {boolean}
   */
  check(hash, shouldAdd) {
    const isContains = this.cbuffer.some(item => item.test(hash));

    if (isContains) {
      return true;
    }

    if (_.isBoolean(shouldAdd) && shouldAdd) {
      this.addHash(hash);
    }

    return false;
  }

  /**
   * Get current Bloom filter
   * @return {*}
   */
  getCurrent() {
    return this.cbuffer.last();
  }

  /**
   * Add hash to last Bloom filter item in circular buffer
   * @param {string} hash - string that we are checking
   */
  addHash(hash) {
    this.getCurrent().add(hash);
  }

  /**
   * Push new Bloom filter to circular buffer
   */
  rotateBuffer() {
    debug(`[${this.name}] -> pushing new Bloom filter to Circular buffer...`);
    this.cbuffer.push(new BloomFilter(this.numBits, this.numHashFunctions));
  }

  /**
   * Upload Bloom filter Typed array to AWS S3
   * @param {Uint32Array} data - binary to upload
   * @return {Promise}
   */
  upload(data) {
    const meta = {
      numBits: this.numBits.toString(),
      numHashFunctions: this.numHashFunctions.toString()
    };
    return this.adapter.upload(this.keyPrefix, data, meta);
  }
}

module.exports = { ShortStore };