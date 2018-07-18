'use strict';

var signup = require('./pages/signup');
var helper = require('./pages/page-helper');
var siteSettings = require('./pages/site-settings');
var expectUtils = require('./helpers/expect-utils');

xdescribe('addnow', function() {
  describe('The Getting started view', function() {
    beforeEach(function() {
      signup.signUp('test@test.pl', '123qwe', '123qwe');
    });

    it('should block wrong domains', function() {
      siteSettings.setDomain('wrong domain');
      expectUtils.checkErrorIsVisible('You must enter a valid URL!');
    });

    it('should allow good domains', function() {
      siteSettings.addSite('domain.com');
      expect(helper.getCurrentUrl()).toBe('/site/edit/3');
    });
  });
});
