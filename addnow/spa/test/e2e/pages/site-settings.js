'use strict';

var helper = require('./page-helper');

var SiteSettings = function() {
  var siteAddUrl = 'site/add/';
  var _this = this;
  var domain = element(by.model('site.domain'));

  var addressBarSharing = element(by.model('site.addressBarSharing'));
  var copyPasteSharing = element(by.model('site.copyPasteSharing'));
  var submit = element(by.css('form button[type=submit]'));
  var cusomiseThankYouPopupButton = $('.add-popup-image-button');


  //Customisation thank you popup
  var thankYouMessage = element(by.model('thankYouData.message'));
  var mediaUrl = element(by.model('thankYouData.advertImageUrl'));
  var advertisementUrl = element(by.model('thankYouData.advertUrl'));
  var advertisementTitle = element(by.model('thankYouData.advertTitle'));
  var submitCutomizeThankyouPopupButton = element(by.css('.the-modal')).element(by.css('form button[type=submit]'));
  //Follow URLs
  var facebook = element(by.css('input[name=facebook]'));
  var googlePlus = element(by.css('input[name=googlePlus]'));
  var linkedin = element(by.css('input[name=linkedin]'));
  var pinterest = element(by.css('input[name=pinterest]'));
  var twitter = element(by.css('input[name=twitter]'));
  var youtube = element(by.css('input[name=youtube]'));
  var instagram = element(by.css('input[name=instagram]'));

  var networks = {
    facebook:{url:'http://facebook.com/', locator:facebook},
    twitter:{url:'http://twitter.com/', locator:twitter},
    linkedin:{url:'http://linkedin.com/', locator:linkedin},
    pinterest:{url:'http://pinterest.com/', locator:pinterest},
    instagram:{url:'http://instagram.com/', locator:instagram},
    googlePlus:{url:'http://googleplus.com/', locator:googlePlus},
    youtube:{url:'http://youtube.com/', locator:youtube}
  };

  this.clickSubmitCutomizeThankyouPopupButton = function(){
    helper.click(submitCutomizeThankyouPopupButton);
  };

  this.clickCustomaseThankYouPopupButton = function() {
    helper.click(cusomiseThankYouPopupButton);
  };

  this.goURL = function() {
    helper.goUrl(siteAddUrl);
  };

  this.goSiteEditPageWithId = function(siteId) {
    helper.goUrl('site/edit/' + siteId);
  };

  this.addSite = function(domainName) {
    _this.goURL();
    _this.setDomain(domainName);
    _this.clickSubmit();
  };

  this.clickSubmit = function() {
    helper.click(submit);
  };

  this.changeStateCopyPasteCheckbox = function() {
    helper.click(copyPasteSharing);
  };

  this.changeStateAddressBarCheckbox = function() {
    helper.click(addressBarSharing);
  };

  this.setThankYouMessage = function(message) {
    helper.setField(thankYouMessage, message);
  };

  this.setDomain = function(domainName) {
    helper.setField(domain, domainName);
  };

  this.setFollowUrl = function(network, value) {
    helper.setField(networks[network].locator, value);
  };

  this.setMediaUrl = function(value) {
    helper.setField(mediaUrl, value);
  };

  this.setAdvertisementUrl = function(value) {
    helper.setField(advertisementUrl, value);
  };

  this.setAdvertisementTitle = function(value) {
    helper.setField(advertisementTitle, value);
  };

  this.setAllFollowUrls = function(path) {//http://facebook.com/testing, here path is testing
    var allNetworks = Object.keys(networks);
    for (var i = 0; i < allNetworks.length; i++) {
      _this.setFollowUrl(allNetworks[i], networks[allNetworks[i]].url + path);
    }
  };

  this.getCopyPasteCheckboxState = function() {
    return copyPasteSharing.element(by.css('.toggle-switch-animate')).getAttribute('class');
  };

  this.getAddressBarCheckboxState = function() {
    return addressBarSharing.element(by.css('.toggle-switch-animate')).getAttribute('class');
  };

  this.getThankYouMessage = function() {
    return helper.getFieldValue(thankYouMessage);
  };

  this.getDomain = function() {
    return helper.getFieldValue(domain);
  };

  this.getFollowUrl = function(network) {
    return helper.getFieldValue(networks[network].locator);
  };

  this.getMediaUrl = function() {
    return helper.getFieldValue(mediaUrl);
  };

  this.getAdvertisementUrl = function() {
    return helper.getFieldValue(advertisementUrl);
  };

  this.getAdvertisementTitle = function() {
    return helper.getFieldValue(advertisementTitle);
  };
};

module.exports = new SiteSettings();
