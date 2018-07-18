"use strict";

const os = require('os');

const _ = require('lodash');
const debug = require('debug')('bf-adapters');
const uuidV1 = require('uuid/v1');
const parseArgs = require('minimist');

/* LIBS */
const tTrack = require('../../../lib/time-track');

const streams = require('../streams');
const s3Adapter = require('./aws-s3');

const timeTrack = new tTrack.TimeTrack();


class Adapter {
  constructor(options) { }

  configure(options) {
    this.bucket = options.bucket;
    this.credentials = options.credentials;
  }

  /**
   * Delete object by key
   * @param key
   * @private
   */
  _delete(key) {
    const params = {
      Bucket: this.bucket,
      Key: key
    };

    debug('deleting:', params.Key);
    return s3Adapter.deleteObject(this.credentials, params)
  }

  /**
   *
   * @param prefix - key prefix includes directory where to put files and filename prefix (collection name)
   * @param data - Bloom Filter Typed Array
   * @param meta - object with number of bits and hash functions for deserialization
   * @return {Promise}
   */
  upload(prefix, data, meta) {

    let uuid = uuidV1();

    let params = {
      Bucket: this.bucket,
      Key: `${prefix}_${uuid.split('-')[0]}_${Date.now()}.bin`,
      Body: new streams.ArrayReadableStream(data),
      ContentType: 'binary/octet-stream',
      ContentLength: data.buffer.byteLength,
      Metadata: {
        uuid: uuid,
        pid: process.pid.toString(),
        hostname: os.hostname(),
        numBits: meta.numBits,
        numHashFunctions: meta.numHashFunctions
      }
    };

    debug('uploading:', params['Key']);

    const endTracking = timeTrack.trackS3UploadRequest(this.bucket, params.Key);


    let uploadOnFulfilled = (response) => {
      endTracking();
      return response
    };

    let uploadOnRejected = (err) => {
      debug('s3 -> upload -> rejected:', err.message, '->', params['Key']);
      endTracking();

      let error = new Error(err.message);
      error.code = err.code;
      error.meta = { params: params };

      throw error;
    };

    return s3Adapter.upload(this.credentials, params)
      .then(data => uploadOnFulfilled(data), err => uploadOnRejected(err))
  }

  /**
   *
   * @param prefix
   * @param key
   * @param etag
   * @return {Promise}
   */
  fetch(prefix, key, etag) {

    let params = {
      Bucket: this.bucket,
      Key: `${prefix}/${key}.bin`,
      IfNoneMatch: etag
    };

    let output = {};
    let writer = new streams.ArrayWritableStream({ output: output });

    const downloadData = data => {

      return new Promise((resolve, reject) => {

        const argv = parseArgs(process.argv.slice(2), { boolean: ['progressbar'], default: { progressbar: false } });

        if (argv.progressbar) {
          let downloadedBytes = 0;
          const totalBytes = data.info.contentLength;
          const binaryName = data.info.path.split('/')[1];
          const calc = (val, total) => Math.round((val / total) * 100);
          const DELAY = 10 * 1000; // in milliseconds

          const progress = setInterval(() => debug(`${binaryName}: ${calc(downloadedBytes, totalBytes)}%`), DELAY);

          data.httpStream
            .on('data', chunk => downloadedBytes += chunk.length)
            .on('end', () => {
              clearInterval(progress);
              debug('s3 -> getObject -> streaming -> on end ->', key);
              resolve({ key: key, etag: data.info.etag, view: new Uint32Array(output.view.buffer) });
            })
            .on('error', err => {
              clearInterval(progress);
              debug('s3 -> getObject -> streaming -> on error ->', err);
              reject(new Error(err.message));
            });
        } else {
          data.httpStream
            .on('end', () => {
              debug('s3 -> getObject -> streaming -> on end ->', key);
              resolve({ key: key, etag: data.info.etag, view: new Uint32Array(output.view.buffer) });
            })
            .on('error', err => {
              debug('s3 -> getObject -> streaming -> on error ->', err);
              reject(new Error(err.message));
            });
        }

        data.httpStream.pipe(writer)

      });

    };

    const endTracking = timeTrack.trackS3DownloadRequest(this.bucket, key);

    /**
     * Get Object response
     * @param response
     *   response.info: {object}
     *     info.path: {string} - binary path
     *     info.contentType: {string} - 'application/octet-stream'
     *     info.contentLength: {number}
     *     info.etag: {string}
     *   response.httpStream: {object}
     */
    let getObjectOnFulfilled = (response) => {
      debug('s3 -> getObject -> fulfilled:', response['info']['path']);
      endTracking();

      return downloadData(response)
    };

    /**
     * Get Object error
     * @param err
     *   err.meta: {object}
     *     meta.path: {string} - binary path
     *   err.code: {number} - 404 or 304
     *   err.message: {string} - 'Not Found' or 'Not Modified'
     */
    let getObjectOnRejected = (err) => {
      debug('s3 -> getObject -> rejected:', err.message, '->', key);
      endTracking();

      let error = new Error(err.message);
      error.code = err.code;
      error.meta = { key: key };

      throw error;
    };

    return new Promise((resolve, reject) => {
      debug(`s3 -> getObject: ${key}`);

      s3Adapter.getObject(this.credentials, params)
        .then(response => getObjectOnFulfilled(response), error => getObjectOnRejected(error))
        .then(bloomChunk => resolve(bloomChunk), error => reject(error))

    });

  }
}

module.exports = {Adapter };
