"use strict";

const _ = require('lodash');
const debug = require('debug')('bf-client');
const CBuffer = require('CBuffer');

const common = require('../../lib/common');

const log = common.logger();

const MESSAGE_SIZE = 152; // Rough active message size (Bytes)
const BUFFER_SIZE_PER_WORKER = 512*1024; // Size of buffer (Bytes)
const ACTIVE_MESSAGES_BUFFER_SIZE = Math.ceil(BUFFER_SIZE_PER_WORKER/MESSAGE_SIZE);
const IPC_CHANNEL = 'bloomfilter';

let messagesCounter = 0;
let activeMessages = new CBuffer(ACTIVE_MESSAGES_BUFFER_SIZE);

activeMessages.overflow = message => {
  log.warn('BF Worker [{0}] -> activeMessages overflow. Message is overridden: {1}'.format(process.pid, message.id));
};

/**
 * Sanity check
 *
 * @param {object} options - options we want to check
 * @param {object} keys - keys we should check
 * @return {boolean} return true if we pass all checks
 */
function sanityCheck (options, keys) {
  return keys.every(key => _.has(options, key) ? !_.isEmpty(options[key]) : false);
}

/**
 * Get result params values
 * @param {object} paramsObj - The params object.
 * @return {object} The array of values in paramsObj.
 */
function getResultParamsValues (paramsObj) {
  let result = [null];

  if (paramsObj) {
    for (let prop in paramsObj) {
      if (paramsObj.hasOwnProperty(prop)) {
        result.push(paramsObj[prop]);
      }
    }
  }
  return result;
}


/**
 * Worker incoming messages handler
 * @param {object} message - The message value.
 */
function messageHandler(message) {
  if (!message || message.channel !== IPC_CHANNEL) return false;

  debug('[' + process.pid + '] received message:', message.responseParams);

  let pendingMessage = activeMessages.pop();

  if (pendingMessage && pendingMessage.callback) {
    pendingMessage.callback.apply(null, getResultParamsValues(message.responseParams));
  }

}

/**
 * Determine request is duplicate or not by Bloom filter
 * by calling callback function with the result
 * @param {object} params - The options, Ex.: { org: {string}, s: {string}, rt: {string} }.
 * @param {function} callback - The request type value.
 */
function isSuspectedDuplicate(params, callback) {

  debug('PID:', process.pid);

  if (_.isFunction(callback)) {
    if (sanityCheck(params, ['org', 's', 'rt'])) {

      debug('[' + process.pid + '] request type:', params.rt);

      let message = {
        id: process.pid + '::' + messagesCounter++,
        channel: IPC_CHANNEL,
        workerPid: process.pid,
        data: {
          hash: params.org + ':' + params.s,
          requestType: params.rt,
          clientId: params.org
        },
        callback: callback
      };

      activeMessages.push(message);

      if (_.isFunction(process.send)) {
        process.send(message);

        debug('[' + process.pid + '] sent message hash:', message.data.hash);

      } else {
        return message;
      }

    } else {
      log.debug('Bloom-Filter::isSuspectedDuplicate# We should provide mandatory params fields');
      callback.apply(null, [{ message: 'We should provide mandatory params fields' }]);
    }
  } else {
    log.debug('Bloom-Filter::isSuspectedDuplicate# We should provide callback function');
    throw new Error('We should provide callback function');
  }

}

process.on('message', messageHandler);

module.exports = { _sanityCheck: sanityCheck, isSuspectedDuplicate };
