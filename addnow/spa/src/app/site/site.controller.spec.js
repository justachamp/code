'use strict';

describe('Controller: SiteCtrl', function() {
  beforeEach(module('angulardash.site'));

  var $scope;
  var $controller;
  var $httpBackend;
  var $location;
  var $q;
  var SiteCtrl;
  var SiteService;
  var WidgetService;
  var ErrorHandler;
  var AnalyticsService;
  var AccountSettingsService;
  var AppSettings;
  var backendApi;
  var jasmineEnv;
  var goodInputs;
  var nested;

  function createController(isValidForm) {
    SiteCtrl = $controller('SiteCtrl', {
      $scope: $scope,
      $location: $location,
      WidgetService: WidgetService,
      ErrorHandler: ErrorHandler,
      AnalyticsService: AnalyticsService,
      AccountSettingsService: AccountSettingsService
    });
    $scope.form = {
      $valid: isValidForm,
      $invalid: !isValidForm
    };
  }

  beforeEach(inject(function($rootScope, _$controller_, _$httpBackend_, _$q_, _SiteService_, _AppSettings_) {
    $scope = $rootScope.$new();
    $q = _$q_;
    $controller = _$controller_;
    $httpBackend = _$httpBackend_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;

    jasmineEnv = jasmine.getEnv();
    jasmineEnv.updateInterval = 100;
    $location = jasmine.createSpyObj('$location', ['path', 'search', 'url']);
    $location.path.and.returnValue('/');
    $location.search.and.returnValue({website:'ww.pl'});
    SiteService = _SiteService_;
    ErrorHandler = jasmine.createSpyObj('ErrorHandler', ['parseResponse', 'flushServerErrors']);
    WidgetService = jasmine.createSpyObj('WidgetService', [
      'editConfiguration', 'getConfiguration', 'getConfigurations'
    ]);
    WidgetService.getConfiguration.and.returnValue({
      then: function() {}
    });

    WidgetService.getConfigurations.and.returnValue({
      then: function() {}
    });

    AnalyticsService = jasmine.createSpyObj('AnalyticsService', ['getAccounts']);
    AnalyticsService.getAccounts.and.returnValue({
      then: function() {}
    });

    AccountSettingsService = jasmine.createSpyObj('AccountSettingsService', ['getSettings']);
    AccountSettingsService.getSettings.and.callFake(function() {
      var deferred = $q.defer();
      deferred.resolve({data:{}});
      return deferred.promise;
    });
  }));

  describe('prepareSocialUrls', function() {
    beforeEach(function() {
      createController(true);
      goodInputs  = [
        {
          service: 'facebook',
          url: 'test.url.facebook'
        },
        {
          service: 'googlePlus',
          url: 'test.url.google'
        },
        {
          service: 'linkedin',
          url: 'test.url.linkedin'
        },
        {
          service: 'pinterest',
          url: 'test.url.pinterest'
        },
        {
          service: 'twitter',
          url: 'test.url.twitter'
        },
        {
          service: 'youtube',
          url: 'test.url.youtube'
        }
      ];
      nested = {};
    });

    it('should prepare list of nested inputs', function() {
      $scope.socialNetworks = goodInputs;
      SiteCtrl.prepareSocialUrls(nested);
      expect(nested).toEqual({
        socialUrls: [
          {name: 'facebook'},
          {name: 'googlePlus'},
          {name: 'linkedin'},
          {name: 'pinterest'},
          {name: 'twitter'},
          {name: 'youtube'}
        ]
      });
    });

    it('should prepare socialUrl object when they are present', function() {
      var result;
      $scope.socialNetworks = goodInputs;
      result = SiteCtrl.prepareSocialUrls(nested);
      expect(result).toEqual([
        {
          service: 'facebook',
          url: 'test.url.facebook'
        },
        {
          service: 'googlePlus',
          url: 'test.url.google'
        },
        {
          service: 'linkedin',
          url: 'test.url.linkedin'
        },
        {
          service: 'pinterest',
          url: 'test.url.pinterest'
        },
        {
          service: 'twitter',
          url: 'test.url.twitter'
        },
        {
          service: 'youtube',
          url: 'test.url.youtube'
        }
      ]);
    });

    it('should remove nestedSocial from nested inputs when user didn\'t input any media', function() {
      var result;
      result = SiteCtrl.prepareSocialUrls(nested);
      expect(result).toEqual([]);
      expect(nested).toEqual({});
    });
  });

  describe('getSite', function() {
    beforeEach(function() {
      createController(true);

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectGET(backendApi + 'sites/1').respond(200, {
        address_bar_sharing: false,
        api_key: '1254856352048jwdf285',
        domain: 'test.pl.domain.com',
        id: 1,
        hash_id: '1:04Q7fqXxgLx5HMtyPnXI8AWqDNY',
        thank_you_message: '',
        social_urls: [
          {
            id: 1,
            service: 'facebook',
            url: 'http://facebook.com/url'
          },
          {
            id: 1,
            service: 'twitter',
            url: 'http://twitter.com/url'
          },
          {
            id: 1,
            service: 'googlePlus',
            url: 'http://google.com/url'
          },
          {
            id: 1,
            service: 'pinterest',
            url: 'http://pinterest.com/url'
          },
          {
            id: 1,
            service: 'linkedin',
            url: 'http://linkedin.com/url'
          },
          {
            id: 1,
            service: 'instagram',
            url: 'http://instagram.com/url'
          },
          {
            id: 1,
            service: 'youtube',
            url: 'http://youtube.com/url'
          }
        ],
        analytics_account: '',
        analytics_property: '',
        analytics_profile: ''
      });

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      SiteCtrl.getSite('1');
      $httpBackend.flush();
    });

    it('should populate site object', function() {
      expect($scope.site.domain).toEqual('test.pl.domain.com');
      expect($scope.site.id).toEqual(1);
    });

    it('should populate socialNetworks inputs', function() {
      expect($scope.socialNetworks).toEqual([
        {
          service: 'facebook',
          url: 'http://facebook.com/url',
          text: 'Facebook',
          placeholder: 'http://facebook.com/..'
        },
        {
          service: 'twitter',
          url: 'http://twitter.com/url',
          text: 'Twitter',
          placeholder: 'http://twitter.com/..'
        },
        {
          service: 'linkedin',
          url: 'http://linkedin.com/url',
          text: 'LinkedIn',
          placeholder: 'http://linkedin.com/..'
        },
        {
          service: 'pinterest',
          url: 'http://pinterest.com/url',
          text: 'Pinterest',
          placeholder: 'http://pinterest.com/..'
        },
        {
          service: 'instagram',
          url: 'http://instagram.com/url',
          text: 'Instagram',
          placeholder: 'http://instagram.com/..'
        },
        {
          service: 'googlePlus',
          url: 'http://google.com/url',
          text: 'Google+',
          placeholder: 'http://plus.google.com/..'
        },
        {
          service: 'youtube',
          url: 'http://youtube.com/url',
          text: 'Youtube',
          placeholder: 'http://youtube.com/..'
        }
      ]);
    });
  });

  describe('addSite', function() {
    var patchRequest;

    beforeEach(function() {
      patchRequest = $httpBackend.expectPOST(backendApi + 'sites').respond(200, {id: 1});
      createController(true);
    });

    it('should create site', function() {
      SiteCtrl.addSite();
      $httpBackend.flush();

      expect($scope.site.id).toBe(1);
      expect($location.path).toHaveBeenCalledWith('/site/edit/' + $scope.site.id);
    });

    it('should be called from submitAddPage', function() {
      $scope.submitAddPage();
      $httpBackend.flush();

      expect($scope.site.id).toBe(1);
      expect($location.path).toHaveBeenCalledWith('/site/edit/' + $scope.site.id);
    });

    it('should handle errors', function() {
      var response = {
        error: 'internal error'
      };
      patchRequest.respond(500, response);
      SiteCtrl.addSite();
      $httpBackend.flush();
      expect(ErrorHandler.parseResponse).toHaveBeenCalledWith(500, response, jasmine.any(Object), jasmine.any(Object));
    });
  });

  describe('updateSite', function() {
    var putRequest;

    beforeEach(function() {
      putRequest = $httpBackend.expectPUT(backendApi + 'sites/1').respond(200, {id: 1});
      createController(true);
      $scope.site.id = 1;
      $scope.edit = true;
    });

    it('should send put with correct data', function() {
      SiteCtrl.updateSite();
      $httpBackend.flush();

      expect($location.path).toHaveBeenCalledWith('/site/dashboard/' + $scope.site.id);
    });

    it('should be called from submitAddPage', function() {
      $scope.submitAddPage();
      $httpBackend.flush();

      expect($location.path).toHaveBeenCalledWith('/site/dashboard/' + $scope.site.id);
    });

    it('should handle errors', function() {
      var response = {error: 'internal error'};
      putRequest.respond(500, response);
      SiteCtrl.updateSite();
      $httpBackend.flush();

      expect(ErrorHandler.parseResponse).toHaveBeenCalledWith(500, response, jasmine.any(Object), jasmine.any(Object));
    });
  });

  describe('addWidget', function() {
    it('should check widget type and populate specified list of widgets', function() {
      var sharingButtonWidget;
      var newsletterWidget;
      sharingButtonWidget = {
        id: 123,
        buttons: [{service: 'facebook'}, {service: 'twitter'}],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'sharing-buttons'
      };
      newsletterWidget = {
        id: 124,
        buttons: [{service: 'facebook'}, {service: 'twitter'}],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'newsletter',
        pageUrl: 'http://URL',
        pageTitle: 'test',
        mediaUrl: 'http://media'
      };
      createController(true);

      SiteCtrl.addWidget(sharingButtonWidget);
      SiteCtrl.addWidget(newsletterWidget);

      expect($scope.selectedWidgets.newsletter.length).toBe(1);
      expect($scope.selectedWidgets.newsletter[0]).toEqual(newsletterWidget);

      expect($scope.selectedWidgets['sharing-buttons'].length).toBe(1);
      expect($scope.selectedWidgets['sharing-buttons'][0]).toEqual(sharingButtonWidget);
    });

    it('should store the same widget type in one array', function() {
      var sharingButtonWidget = {
        id: 123,
        buttons: [{service: 'facebook'}, {service: 'twitter'}],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'sharing-buttons'
      };
      createController(true);

      SiteCtrl.addWidget(sharingButtonWidget);
      SiteCtrl.addWidget(sharingButtonWidget);

      expect($scope.selectedWidgets['sharing-buttons'].length).toBe(2);
      expect($scope.selectedWidgets['sharing-buttons'][0]).toEqual(sharingButtonWidget);
      expect($scope.selectedWidgets['sharing-buttons'][1]).toEqual(sharingButtonWidget);
    });
  });

  describe('utils method', function() {
    var sharingButtonsWidget = {
        id: 123,
        buttons: [{service: 'facebook'}, {service: 'twitter'}],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'sharing-buttons'
      };
    var newsletterWidget = {
      id: 124,
      buttons: [{service: 'facebook'}, {service: 'twitter'}],
      buttonSize: 'large',
      orientation: 'vertical',
      buttonStyle: 'label',
      counterPosition: 'top',
      type: 'newsletter',
      pageUrl: 'http://URL',
      pageTitle: 'test',
      mediaUrl: 'http://media'
    };

    beforeEach(function() {
      createController(true);
    });

    it('should define type of widget', function() {
      expect($scope.isSharingButtons(newsletterWidget)).toBeFalsy();
      expect($scope.isSharingButtons(sharingButtonsWidget)).toBeTruthy();

      expect($scope.isNewsletter(newsletterWidget)).toBeTruthy();
      expect($scope.isNewsletter(sharingButtonsWidget)).toBeFalsy();
    });
  });

  describe('updateWidgetState', function() {
    it('should change state and do backend call', function() {
      var widget = {id: 2};
      createController(true);
      $scope.site = {id: 1};
      $scope.updateWidgetState(widget, true);
      widget.isActive = true;
      expect(WidgetService.editConfiguration).toHaveBeenCalledWith($scope.site.id, widget.id, widget);

      widget.isActive = false;
      $scope.updateWidgetState(widget, false);
      expect(WidgetService.editConfiguration).toHaveBeenCalledWith($scope.site.id, widget.id, widget);
    });
  });
});
