'use strict';

var request = require('request');
var config = require('../config');
var conf;

//request.debug = true;
conf = config[browser.params.target];

exports.updateAccount = function(token, accountSettings, cb) {
  request.put({
    url: conf.targetAPI + '/account',
    body: accountSettings,
    json: true,
    headers: {
      Authorization: 'JWT ' + token
    }
  }, cb);
};
