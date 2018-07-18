'use strict';

describe('Controller: NavbarCtrl', function() {
  beforeEach(module('angulardash.navbar'));

  var $scope;
  var $controller;
  var $httpBackend;
  var $location;
  var $localStorage;
  var NavbarCtrl;
  var SiteService;
  var AppSettings;
  var backendApi;

  function createController() {
    NavbarCtrl = $controller('NavbarCtrl', {
      $scope: $scope,
      $location: $location,
      $localStorage: $localStorage
    });
  }

  beforeEach(inject(function($rootScope, _$controller_, _$httpBackend_, _$location_, _SiteService_, _AppSettings_) {
    $scope = $rootScope.$new();
    $controller = _$controller_;
    $httpBackend = _$httpBackend_;
    $location = _$location_;
    $localStorage = {};
    SiteService = _SiteService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;
  }));

  describe('selectMenuItem', function() {
    it('should set sites to scope', function() {
      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      var sites = [
        {
          address_bar_sharing: false,
          domain: 'test.pl.domain.com',
          id: 1,
          hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
          thank_you_message: '',
          social_urls: []
        },
        {
          address_bar_sharing: true,
          domain: 'test.pl.domain.with.social.urls.com',
          id: 2,
          hash_id: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
          thank_you_message: 'thank you msg',
          social_urls: [
            {
              id: 1,
              service: 'facebook',
              url: 'http://facebook.com/url'
            }
          ]
        }
      ];
      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers

      var scopeSites = [
        {
          addressBarSharing: false,
          domain: 'test.pl.domain.com',
          id: 1,
          hashId: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
          thankYouMessage: '',
          socialUrls: []
        },
        {
          addressBarSharing: true,
          domain: 'test.pl.domain.with.social.urls.com',
          id: 2,
          hashId: '2:FeEqS2xWiIPRf0YA5Z6v0ig2bkM',
          thankYouMessage: 'thank you msg',
          socialUrls: [
            {
              id: 1,
              service: 'facebook',
              url: 'http://facebook.com/url'
            }
          ]
        }
      ];

      $httpBackend.expectGET(backendApi + 'sites').respond(200, sites);
      createController();

      $httpBackend.flush();
      expect($scope.sites).toEqual(scopeSites);
    });
  });

  describe('siteChange', function() {
    beforeEach(function() {
      createController();
    });

    it('should change location to dashboard view of sub item', function() {
      $scope.siteChange(1);
      expect($location.path()).toBe('/site/dashboard/1');
    });
  });

  /*describe('isSelectedSite', function() {
   beforeEach(function() {
   createController();
   });

   it('should return active when on site/dashboard', function() {
   $location.path('/site/dashboard/1');
   expect($scope.selectedSite.id).toEqual(1);
   });

   it('should return active when on site/edit', function() {
   $location.path('/site/edit?id=1');
   expect($scope.selectedSite.id).toEqual(1);
   });
   });*/
});
