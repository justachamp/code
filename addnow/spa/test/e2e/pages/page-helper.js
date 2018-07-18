'use strict';

var config = require('../config');

var Helper = function() {
  var conf = config[browser.params.target];
  var baseUrl = conf.targetUI;
  var _this = this;

  this.waitElement = function(element) {
    browser.wait(protractor.ExpectedConditions.elementToBeClickable(element), 3000);
  };

  this.goUrl = function(url) {
    browser.sleep(300);
    browser.get(baseUrl.concat(url));
    browser.sleep(300);
  };

  this.getBaseUrl = function()  {
    return baseUrl;
  };

  this.getCurrentUrl = function(URL) {
    return browser.getLocationAbsUrl();
  };

  this.getFieldValue = function(locator) {
    _this.waitElement(locator);
    return locator.getAttribute('value');
  };

  this.click = function(button) {
    _this.waitElement(button);
    button.click();
    browser.sleep(300);
  };

  this.setField = function(locator, value) {
    locator.clear();
    locator.sendKeys(value);
  };
};

module.exports = new Helper();
