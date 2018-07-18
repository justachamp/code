"use strict";

/**
 * Computes m (total bits of Bloom filter) which is expected to achieve, for the specified
 * expected insertions, the required false positive probability.
 *
 * See http://en.wikipedia.org/wiki/Bloom_filter#Probability_of_false_positives for the formula.
 *
 * @param {number} n - expected insertions (must be positive)
 * @param {number} p - false positive rate (must be 0 < p < 1)
 * @return {number} The total bits value.
 */
function optimalNumberOfBits (n, p) {
  if (p === 0) {
    p = Number.MIN_VALUE;
  }
  // each element is a 32-bit integer
  return Math.ceil((-n * Math.log(p) / Math.pow(Math.log(2), 2)) / 32) * 32;
}

/**
 * Computes the optimal k (number of hashes per element inserted in Bloom filter), given the
 * expected insertions and total number of bits in the Bloom filter.
 *
 * See http://en.wikipedia.org/wiki/File:Bloom_filter_fp_probability.svg for the formula.
 *
 * @param {number} n - expected insertions (must be positive)
 * @param {number} m - total number of bits in Bloom filter (must be positive)
 * @return {number} The number of hashes per element.
 */
function optimalNumberOfHashFunctions (n, m) {
  // (m / n) * log(2), but avoid truncation due to division!
  return Math.max(1, Math.round((m / n ) * Math.log(2)));
}

/**
 * Get specific date key using formatting. Ex.: 2017-05-31-23
 * @param {Date} date
 * @param {string} delimiter
 * @return {string}
 */
function getKey (date, delimiter) {
  delimiter = delimiter || '-';

  const year = date.getUTCFullYear();
  const mm = date.getUTCMonth() + 1; // getMonth() is zero-based
  const dd = date.getUTCDate();
  const hh = date.getUTCHours();
  return [year, (mm > 9 ? '' : '0') + mm, (dd > 9 ? '' : '0') + dd, (hh > 9 ? '' : '0') + hh].join(delimiter);
}

/**
 * Get date keys array of specified size, subtracting each hour from date.
 * Key generated using formatting based on request type and date. Ex.: displayRes_2017-05-31-23
 * @param name - collection name based on request type (combined or displayRes)
 * @param date - date object
 * @param size - how many keys to generate from now
 * @return {Array}
 */
function getKeys(name, date, size) {
  let keys = [];
  for (let i = 0; i < size; i++) {
    const d = new Date(date.getTime());
    d.setHours(d.getHours() - (i + 1));
    keys.push(`${name}_${getKey(d)}`);
  }
  return keys;
}

module.exports = { optimalNumberOfBits, optimalNumberOfHashFunctions, getKey, getKeys };
