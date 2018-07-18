"use strict";

const stream = require('stream');
const common = require('../../lib/common');

// Readable and Writable Array streams classes for storing Bloom filters chunks

/**
 * ArrayReadableStream
 * @param source - source array
 * @param options - optional stream options
 * @return {ArrayReadableStream}
 * @constructor
 */
class ArrayReadableStream extends stream.Readable {

  constructor (source, options) {
    super(options || {});

    this.buffer = source.buffer;
    this.pos = 0;
    this.byteLength = source.byteLength;
  }

  /**
   * Read
   * @param size - how many bytes to read
   * @private
   */
  _read (size) {
    let toRead;

    try {
      toRead = Math.min(this.byteLength - this.pos, size);

      if (toRead <= 0)
        return this.push(null);

      this.push(Buffer.from(new Uint8Array(this.buffer, this.pos, toRead)));
    } catch (err) {
      this.emit('error', err);
    }

    this.pos += toRead;
  }
}


/**
 * ArrayWritableStream
 * @param options - stream options containing output object reference
 * @return {ArrayWritableStream}
 * @constructor
 */
class ArrayWritableStream extends stream.Writable {

  constructor (options) {
    const defaults = { output: {} };
    options = Object.assign({}, defaults, options);

    super(options);

    this.output = options.output;
    this.output.view = new Uint8Array(0);
  }

  /**
   * Write
   * @param {buffer|string} chunk - the chunk to be written.
   * @param {string} encoding - If the chunk is a string, then this is the encoding type.
   * @param callback - Function Call this function when you are done processing the supplied chunk.
   * @private
   */
  _write (chunk, encoding, callback) {
    this.output.view = common.concatTypedArrays(this.output.view, new Uint8Array(chunk));

    callback();
  }

}

module.exports = { ArrayReadableStream, ArrayWritableStream };
