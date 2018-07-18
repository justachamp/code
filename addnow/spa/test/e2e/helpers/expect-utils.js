'use strict';
var TIME_FOR_WAITING_ERROR = 1000;
var EC = protractor.ExpectedConditions;
var signin = require('../pages/signin');
var menu = require('../pages/menu');
var helper = require('../pages/page-helper');

exports.checkErrorIsVisible = function checkErrorIsVisible(errorText) {
  browser.wait(EC.presenceOf(element(by.cssContainingText('.msg-error', errorText)), TIME_FOR_WAITING_ERROR));
};

exports.checkResetPassword = function checkResetPassword(emailValue, passwordValue) {
  signin.logout();
  signin.login(emailValue, passwordValue);
  expect(helper.getCurrentUrl()).toBe('/site/dashboard/1');
};

exports.userMenuShouldBeOpened = function() {
  expect(menu.userOptions.getAttribute('class')).toContain('active');
};
