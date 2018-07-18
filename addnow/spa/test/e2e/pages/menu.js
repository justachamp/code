'use strict';

var helper = require('./page-helper');

var Menu = function() {
  var sitesSelect = element(by.css('.jump-to-site'));
  var addSite = element(by.css('.add-site-button'));
  var firstSiteInList = element(by.css('.jump-to-site option:nth-child(2)'));
  var userMenu = element(by.css('.user-menu-button'));
  var userOptionsMenu = element(by.css('.user-menu'));
  this.userOptions = element(by.css('.user-menu-options'));
  var userOptionsSettings = element(by.css('.user-menu-options nav a:nth-child(1)'));
  var sitesInList = element.all(by.css('.jump-to-site option'));
  var editGear = $('.site-config-button');
  var _this = this;

  this.clickAddSiteButton = function() {
    addSite.click();
  };

  this.clickGear = function() {
    helper.click(editGear);
  };

  this.getAllSites = function() {
    browser.sleep(5000);
    return element.all(by.css('.jump-to-site option'));
  };

  this.clickFirstSite = function() {
    helper.click(firstSiteInList);
  };

  this.clickUserMenu = function() {
    helper.click(userMenu);
  };

  this.clickUserOptionsMenu = function() {
    helper.click(userOptionsMenu);
  };

  this.clickUserOptionsSettings = function() {
    helper.click(userOptionsSettings);
  };

  this.siteSelectClick = function() {
    helper.click(sitesSelect);
  };

  this.findSiteInDropdown = function(siteName) {
    _this.siteSelectClick();
    return sitesInList.filter(function(elem) {
      return elem.getText().then(function(text) {
        return text === siteName;
      });
    });
  };

  this.clickSiteInDropdown = function(siteName) {
    _this.findSiteInDropdown(siteName)
        .then(function(filteredElements) {
          filteredElements[0].click();
        });
  };
};

module.exports = new Menu();
