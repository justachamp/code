"use strict";

const _ = require('lodash');
const winston = require('winston');
const debug = require('debug')('bf-s3-adapter');
const AWS = require('aws-sdk');

const common = require('../../../lib/common');
const CustomError = require('../error').CustomError;

const log = common.logger();

const CRITICAL_ERROR_CODES = [
  'MissingRequiredParameter', 'CredentialsError', 'InvalidAccessKeyId', 'SignatureDoesNotMatch', 'UnknownEndpoint'
];

// code: NetworkingError
// message: connect EHOSTUNREACH 52.216.224.0:443

/**
 * Uploads stream, using intelligent concurrent handling of parts if the payload is large enough.
 * You can configure the concurrent queue size by setting options.
 * Note that this is the only operation for which the SDK can retry requests with stream bodies.
 *
 * @param awsCredentials
 * @param params
 * @return {Promise}
 */
const upload = (awsCredentials, params) => {
  let s3 = new AWS.S3(awsCredentials);

  return s3.upload(params).promise()
    .then(data => {
      debug(data);
      return { key: data.Key, etag: data.ETag };
    })
    .catch(err => {
      debug(err);
      log.error(err);

      // checking error codes that can brake normal app functioning
      if (_.contains(CRITICAL_ERROR_CODES, err.code)) {
        throw new CustomError('critical', err.message, err.code);
      } else {
        throw new CustomError('normal', err.message, err.code);
      }
    });

};

/**
 * Retrieves objects from Amazon S3
 *
 * @param awsCredentials
 * @param params
 * @return {Promise}
 */
const getObject = (awsCredentials, params) => {

  let s3 = new AWS.S3(awsCredentials);

  return new Promise((resolve, reject) => {
    const request = s3.getObject(params)
      .on('httpHeaders', (statusCode, headers, response, statusMessage) => {

        if (statusCode >= 300) {
          reject({ meta: { path: params.Key }, code: statusCode, message: statusMessage })
        } else {
          const info = {
            path: params.Key,
            contentType: headers['content-type'],
            contentLength: parseInt(headers['content-length']),
            etag: headers['etag'].slice(1, -1)
          };

          resolve({ info: info, httpStream: response.httpResponse.createUnbufferedStream() });
        }
      })
      .on('httpError', (err, response) => {
        // Triggered when the HTTP request failed
        debug('httpError:', err);
        log.error(err);
        reject({ meta: { path: params.Key }, code: err.code, message: err.message })
      });

      request.send();

  });

};

const deleteObject= (awsCredentials, params) => {
  let s3 = new AWS.S3(awsCredentials);
  return s3.deleteObject(params).promise();
};

module.exports = { upload, getObject, deleteObject };
