'use strict';

var signin = require('./pages/signin');
var helper = require('./pages/page-helper');
var menu = require('./pages/menu');
var expectUtils = require('./helpers/expect-utils');

describe('addnow', function() {

  describe('Logged user in', function() {

    beforeAll(function() {
      signin.login('test@test.pl', '123qwe');
    });

    describe('menu view', function() {

      beforeEach(function() {
        helper.goUrl('/settings');
      });

      it('should go to new page view after clicking on add site', function() {
        menu.clickAddSiteButton();
        expect(helper.getCurrentUrl()).toBe('/site/add');
      });

      it('should get the list of all available websites', function() {
        menu.getAllSites().then(function(items) {
          expect(items.length).toBe(4);//TODO: need to choose other way for expects
          expect(items[1].getText()).toBe('test.pl.domain.com');
          expect(items[2].getText()).toBe('another.domain2.com');
        });
      });

      it('should go to website dashboard on click site from list', function() {
        menu.clickFirstSite();
        expect(helper.getCurrentUrl()).toBe('/site/dashboard/1');
      });

      it('should open menu settings', function() {
        menu.clickUserOptionsMenu();
        expectUtils.userMenuShouldBeOpened();
      });

      it('should go to settings view when dropdown option clicked', function() {
        menu.clickUserOptionsMenu();
        menu.clickUserOptionsSettings();
        expect(helper.getCurrentUrl()).toBe('/settings');
      });

    });

  });

});
