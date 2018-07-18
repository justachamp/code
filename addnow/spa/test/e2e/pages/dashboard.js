'use strict';

var helper = require('./page-helper');

var Dashboard = function() {
  var datePicker = element(by.model('dateRange'));
  var _this = this;

  this.getDashboardPage = function(siteId) {
    return '/site/dashboard/' + siteId;
  };

  this.openDashboard = function(siteId) {
    browser.get(helper.getBaseUrl() + _this.getDashboardPage(siteId));
  };

  this.hasOneMainChart = function() {
    var count = element.all(by.css('div[data-provider="eventsSummary"] .amcharts-main-div')).count();
    var successCb = function(value) {
      return value === 1;
    };

    var errorCb = function() {
      return false;
    };

    return count.then(successCb, errorCb);
  };

  this.getShareAndClicksRows = function() {
    return element.all(by.repeater('sharesAndClicksByToolItem in sharesAndClicksByTool'));
  };

  this.openDatePicker = function() {
    return datePicker.click();
  };

  this.getDatePickerValue = function() {
    return datePicker.getAttribute('value');
  };

  this.getDatePickerPeriodButton = function(period) {
    return element(by.cssContainingText('.ranges li', 'By ' + period));
  };

  this.getSharesAndClicksByToolRowsCount = function() {
    return element.all(by.repeater('sharesAndClicksByToolItem in sharesAndClicksByTool')).count();
  };

  this.getSharesAndClicksByToolItemSharesPercents = function() {
    return element.all(by.exactBinding('sharesAndClicksByToolItem.sharesPercent'));
  };

  this.getSharesAndClicksByToolItemShares = function() {
    return element.all(by.exactBinding('sharesAndClicksByToolItem.shares'));
  };

  this.getSummaryMainChartsCount = function() {
    return element.all(by.css('#summary .amcharts-main-div')).count();
  };

  this.getTopSocialChannelsRowsCount = function() {
    return element.all(by.repeater('topSocialChannelsItem in topSocialChannels')).count();
  };

  this.getTopSocialChannelsItemSharesPercent = function() {
    return element.all(by.exactBinding('topSocialChannelsItem.sharesPercent'));
  };

  this.getTopSocialChannelsItemShares = function() {
    return element.all(by.exactBinding('topSocialChannelsItem.shares'));
  };

  this.getTopContentBySharesRowsCount = function() {
      return element.all(by.repeater('topContentBySharesItem in topContentByShares')).count();
    };

  this.getTopContentByClicksRowsCount = function() {
    return element.all(by.repeater('topContentByClicksItem in topContentByClicks')).count();
  };

  this.getTopContentBySharesItemSharesPercent = function() {
    return element.all(by.exactBinding('topContentBySharesItem.sharesPercent'));
  };

  this.getTopContentBySharesItemShares = function() {
    return element.all(by.exactBinding('topContentBySharesItem.shares'));
  };

  this.getTopContentBySharesItemClicksPercent = function() {
    return element.all(by.exactBinding('topContentBySharesItem.clicksPercent'));
  };

  this.getTopContentBySharesItemClicks = function() {
    return element.all(by.exactBinding('topContentBySharesItem.clicks'));
  };

  this.getKeywordsCount = function() {
    return element.all(by.repeater('copiedKeywordsItem in copiedKeywords')).count();
  };

  this.getKeywordsItemCopies = function() {
    return element.all(by.exactBinding('copiedKeywordsItem.copies'));
  };

  this.getTopCountriesCount = function() {
    return element.all(by.repeater('topCountriesItem in topCountries')).count();
  };

  this.getTopCountriesShares = function() {
    return element.all(by.binding('topCountriesItem.shares'));
  };

  this.getTopCountriesClicks = function() {
    return element.all(by.binding('topCountriesItem.clicks'));
  };

  this.getGeoMapsCount = function() {
    return element.all(by.css('#geo .amcharts-main-div')).count();
  };

  this.getTotalExternalSharesCount = function() {
    return element.all(by.repeater('totalExternalSharesItem in totalExternalShares')).count();
  };

  this.getTotalExternalSharesItemSharesPercent = function() {
    return element.all(by.exactBinding('totalExternalSharesItem.sharesPercent'));
  };

  this.getTotalExternalSharesItemShares = function() {
    return element.all(by.exactBinding('totalExternalSharesItem.shares'));
  };
};

module.exports = new Dashboard();
