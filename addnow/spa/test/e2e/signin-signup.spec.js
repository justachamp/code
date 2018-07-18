'use strict';

var signin = require('./pages/signin');
var helper = require('./pages/page-helper');
var signup = require('./pages/signup');
var expectUtils = require('./helpers/expect-utils');

describe('addnow', function() {
  describe('signIn in view', function() {
    afterEach(function() {
      browser.executeScript('window.sessionStorage.clear();');
      browser.executeScript('window.localStorage.clear();');
    });

    it('should allow good credentials', function() {
      //allure.feature('My Feature');
      //allure.story('My Story1');
      //allure.description('Some desc');
      signin.login('test@test.pl', '123qwe');
      expect(browser.getLocationAbsUrl()).toBe('/site/dashboard/1');
    });

    it('should block wrong credentials', function() {
      signin.login('nonExistingUser@test.pl', '123qwe');
      expect(helper.getCurrentUrl()).toBe('/signin/');
    });
  });

  describe('signUp view', function() {

    afterEach(function() {
      browser.executeScript('window.sessionStorage.clear();');
      browser.executeScript('window.localStorage.clear();');
    });

    it('should redirect to confirmation when user is new', function() {
      signup.signUp('nonExistingUser@test.pl', '123qwe', '123qwe');
      expect(helper.getCurrentUrl()).toBe('/confirmation/?sent');
    });

    it('should not signup when user exists', function() {
      signup.signUp('test@test.pl', '123qwe', '123qwe');
      expectUtils.checkErrorIsVisible('User with this email already exists.');
    });
  });
});
