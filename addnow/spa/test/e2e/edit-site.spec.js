'use strict';

var signin = require('./pages/signin');
var helper = require('./pages/page-helper');
var menu = require('./pages/menu');
var siteSettings = require('./pages/site-settings');

describe('addnow', function() {

  beforeAll(function() {
    signin.login('test@test.pl', '123qwe');
  });

  describe('Logged user in', function() {

    describe('Add site view', function() {

      beforeEach(function() {
        siteSettings.goURL();
      });

      it('should add site with only domain to menu list', function() {
        var someDomain = 'some.domain.com';

        siteSettings.setDomain(someDomain);
        siteSettings.clickSubmit();
        menu.clickSiteInDropdown(someDomain);

        expect(browser.getCurrentUrl()).toContain('site/edit/');
        expect(siteSettings.getDomain()).toBe(someDomain);
      });
    });

    describe('Edit site view', function() {
      beforeEach(function() {
        siteSettings.goSiteEditPageWithId('2');
      });

      it('should update domain name', function() {
        siteSettings.setDomain('another.domain1.com');
        siteSettings.clickSubmit();
        expect(helper.getCurrentUrl()).toContain('site/dashboard/');
      });

      it('should change all data', function() {
        var domainVal = 'another.domain2.com';

        siteSettings.setDomain(domainVal);
        siteSettings.changeStateCopyPasteCheckbox();
        siteSettings.changeStateAddressBarCheckbox();
        siteSettings.clickSubmit();
        menu.clickGear();

        expect(siteSettings.getDomain()).toBe(domainVal);
        expect(siteSettings.getAddressBarCheckboxState()).toMatch('switch-off');
        expect(siteSettings.getCopyPasteCheckboxState()).toMatch('switch-off');
      });
    });

    describe('Customise thank you popup message', function() {
      beforeEach(function() {
        siteSettings.goSiteEditPageWithId('2');
        siteSettings.clickCustomaseThankYouPopupButton();
      });

      it('should change thank you message', function() {
        var setThankYouMessage = 'sharing message for another.domain.com';
        siteSettings.setThankYouMessage(setThankYouMessage);
        siteSettings.clickSubmitCutomizeThankyouPopupButton();

        siteSettings.goSiteEditPageWithId('2');
        siteSettings.clickCustomaseThankYouPopupButton();

        expect(siteSettings.getThankYouMessage()).toBe(setThankYouMessage);
      });

      it('should change follow urls',function(){
        var setUrl = 'anotherurl';

        siteSettings.setAllFollowUrls(setUrl);
        siteSettings.clickSubmitCutomizeThankyouPopupButton();

        siteSettings.goSiteEditPageWithId('2');
        siteSettings.clickCustomaseThankYouPopupButton();

        expect(siteSettings.getFollowUrl('facebook')).toBe('http://facebook.com/' + setUrl);
        expect(siteSettings.getFollowUrl('googlePlus')).toBe('http://googleplus.com/' + setUrl);
        expect(siteSettings.getFollowUrl('linkedin')).toBe('http://linkedin.com/' + setUrl);
        expect(siteSettings.getFollowUrl('pinterest')).toBe('http://pinterest.com/' + setUrl);
        expect(siteSettings.getFollowUrl('twitter')).toBe('http://twitter.com/' + setUrl);
        expect(siteSettings.getFollowUrl('instagram')).toBe('http://instagram.com/' + setUrl);
        expect(siteSettings.getFollowUrl('youtube')).toBe('http://youtube.com/' + setUrl);
      });
    });
  });
});
