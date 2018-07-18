'use strict';

describe('Service: SiteService', function() {
  beforeEach(module('angulardash.site'));

  var $rootScope;
  var $httpBackend;
  var SiteService;
  var AppSettings;
  var backendApi;
  var customMatchers;

  beforeEach(inject(function(_$rootScope_, _$httpBackend_, _SiteService_, _AppSettings_) {
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;
    SiteService = _SiteService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;

    customMatchers = {
      toEqualData: function() {
        return {
          compare: function(actual, expected) {
            var result = {};
            result.pass = angular.equals(actual, expected);
            return result;
          }
        };
      }
    };

    jasmine.addMatchers(customMatchers);
  }));

  describe('addSite', function() {
    it('should send data with social networks if present', function() {
      var site = {};

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectPOST(backendApi + 'sites', {
        domain: 'domain', social_urls: [{service: 'facebook', url: 'http://facebook.com/url'}]
      }).respond(202);

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      site.domain = 'domain';
      site.socialUrls = [{service: 'facebook', url: 'http://facebook.com/url'}];
      SiteService.addSite(site);
      $httpBackend.flush();
    });

    it('should send data without social networks if not present', function() {
      var site = {};

      $httpBackend.expectPOST(backendApi + 'sites', {domain: 'domain'}).respond(202);
      site.domain = 'domain';
      SiteService.addSite(site);
      $httpBackend.flush();
    });
  });

  describe('getSiteById', function() {
    it('should respond with site data', function() {
      $httpBackend.expectGET(backendApi + 'sites/1').respond(202);
      SiteService.getSiteById('1');
      $httpBackend.flush();
    });
  });

  describe('editSite', function() {
    it('should send put with correct data', function() {
      $httpBackend.expectPUT(backendApi + 'sites/1', {}).respond(204);
      SiteService.editSite('1', {});
      $httpBackend.flush();
    });
  });

  describe('getReportResource', function() {
    var resource;

    it('should have query method that send get request and respond with report data array', function() {
      $httpBackend.expectGET(backendApi + 'digest?begin_date=2&end_date=2&site=1').respond(200, [
        {channel: 'googlePlus', shares: 1111},
        {channel: 'facebook', shares: 2222}
      ]);
      resource = SiteService.getReportResource();

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      resource.query({site: 1, begin_date: '2', end_date: '2'}, function(response) {
        expect(response).toEqualData([
          {channel: 'googlePlus', shares: 1111},
          {channel: 'facebook', shares: 2222}
        ]);
      });

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.flush();
    });
  });

  describe('getSites', function() {
    it('should download sites from backend', function() {
      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      var sites = [
        {
          address_bar_sharing: false,
          domain: 'test.pl.domain.com',
          id: 1,
          hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
          thank_you_message: '',
          social_urls:[]
        },
        {
          address_bar_sharing: true,
          domain: 'test.pl.domain.with.social.urls.com',
          id: 2,
          hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
          thank_you_message: 'thank you msg',
          social_urls:[{
            id: 1,
            service: 'facebook',
            url: 'http://facebook.com/url'
          }]
        }
      ];
      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      var downloadedSites;

      $httpBackend.expectGET(backendApi + 'sites').respond(sites);
      SiteService.getSites().then(function(result) {
        downloadedSites = result;
      });

      $httpBackend.flush();
      expect(downloadedSites.data.length).toBe(2);
    });
  });
});
