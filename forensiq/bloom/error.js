"use strict";

class CustomError extends Error {

  constructor(type, message, code) {
    super(message);
    this.type = type;
    this.code = code;
  }

}

module.exports = { CustomError };