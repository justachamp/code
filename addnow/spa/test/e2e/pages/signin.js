'use strict';

var helper = require('./page-helper');

var Signin = function() {
  var signUrl = 'signin/';
  var logoutUrl = 'logout/';
  var email = element(by.model('registration.email'));
  var password = element(by.model('registration.password'));
  var submit = $('button.g4-button');
  var _this = this;

  this.login = function(emailValue, passwordValue) {
    _this.goSigninPage();
    email.sendKeys(emailValue);
    password.sendKeys(passwordValue);
    submit.click();
    browser.sleep(1000);
  };

  this.goSigninPage = function() {
    helper.goUrl(signUrl);
  };

  this.logout = function() {
    helper.goUrl(logoutUrl);
  };
};

module.exports = new Signin();
