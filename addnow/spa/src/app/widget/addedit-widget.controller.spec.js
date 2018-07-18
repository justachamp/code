'use strict';

describe('Controller: AddEditWidgetCtrl', function() {
  beforeEach(module('angulardash.widget'));

  var $scope;
  var $controller;
  var $modalInstance;
  var $filter;
  var WidgetCtrl;
  var WidgetService;
  var MenuService;
  var Enums;
  var validateForm;
  var AppSettings;
  var host;
  var parser;

  function createController(widgetConfig, siteId, hashId, trimKey, socialNetworks, isValidForm) {
    WidgetCtrl = $controller('AddEditWidgetCtrl', {
      $scope: $scope,
      $modalInstance: $modalInstance,
      widgetConfig: widgetConfig,
      WidgetService: WidgetService,
      validateForm: validateForm,
      MenuService: MenuService,
      siteId: siteId,
      trimKey: trimKey,
      hashId: hashId,
      Enums: Enums,
      socialNetworks: socialNetworks,
      $filter: $filter
    });
    $scope.form = {
      $valid: isValidForm,
      $invalid: !isValidForm
    };
  }

  beforeEach(inject(function($rootScope, _$controller_, _$filter_, _Enums_, _AppSettings_) {
    $scope = $rootScope.$new();
    $controller = _$controller_;
    $filter = _$filter_;
    Enums = _Enums_;
    AppSettings = _AppSettings_;
    parser = document.createElement('a');
    parser.href = AppSettings.backendApi;
    host = parser.host;

    $modalInstance = jasmine.createSpyObj('$modalInstance', ['dismiss', 'close']);
    WidgetService = jasmine.createSpyObj('WidgetService', [
      'addConfiguration', 'editConfiguration'
    ]);
    WidgetService.addConfiguration.and.returnValue({
      then: function() {
        return {
          data: {id: 123},
          catch: function() {}
        };
      }
    });
    WidgetService.editConfiguration.and.returnValue({
      then: function() {}
    });

    MenuService = jasmine.createSpyObj('MenuService', ['markMenuItemsForUpdate']);
    this.socialNetworks = [
      {id: 10, service: 'facebook', url: 'http://www.facebook.com/clarin'},
      {id: 11, service: 'instagram', url: 'http://www.instagram.com/clarin'},
      {id: 13, service: 'googlePlus', url: 'http://www.googleplus.com/clarin'},
      {id: 14, service: 'linkedin', url: 'http://www.linkedin.com/clarin'},
      {id: 15, service: 'pinterest', url: 'http://www.pinterest.com/clarin'},
      {id: 16, service: 'twitter', url: 'http://www.twitter.com/clarin'}
    ];
  }));

  describe('add new widget', function() {
    var defaultWidget = {
      type: 'sharing-buttons',
      isActive: true,
      buttons: []
    };

    it('use predefined values', function() {
      createController(defaultWidget, 1, 1, null, this.socialNetworks, true);
      expect($scope.widgetConfig).toEqual(defaultWidget);
    });

    it('should save valid form', function() {
      createController(defaultWidget, 1, 1, null, this.socialNetworks, true);
      $scope.submitAddPage();
      expect(WidgetService.addConfiguration).toHaveBeenCalledWith(1, defaultWidget);
    });

    it('should not save invalid form', function() {
      createController(defaultWidget, 1, 1, null, this.socialNetworks, false);
      $scope.submitAddPage();
      expect(WidgetService.addConfiguration).not.toHaveBeenCalled();
    });

    it('all buttons are non selected', function() {
      createController(defaultWidget, 1, 1, null, this.socialNetworks, true);
      expect($scope.nonSelectedButtons).toEqual(WidgetCtrl.allButtons);
    });
  });

  describe('edit existing widget', function() {
    var widgetObject = {
      id: 124,
      buttons: [
        {service: 'facebook', text: 'Facebook', isExtraButton: false, followUrl: ''},
        {service: 'twitter', text: 'Twitter', isExtraButton: false, followUrl: ''}
      ],
      buttonSize: 'large',
      orientation: 'vertical',
      buttonStyle: 'label',
      counterPosition: 'top',
      type: 'sharing-buttons',
      isActive: true
    };

    it('should use passed values', function() {
      createController(widgetObject, 1, 1, null, [], true);
      expect($scope.widgetConfig).toEqual(widgetObject);
      expect($scope.isEdit()).toBeTruthy();
    });

    it('should save valid form', function() {
      createController(widgetObject, 1, 1, null, [], true);
      $scope.submitAddPage();
      expect(WidgetService.editConfiguration).toHaveBeenCalledWith(1, widgetObject.id, widgetObject);
    });

    it('should not save invalid form', function() {
      createController(widgetObject, 1, 1, null, [], false);
      $scope.submitAddPage();
      expect(WidgetService.addConfiguration).not.toHaveBeenCalled();
    });
  });

  describe('has function', function() {
    var sharingButtonsWidget;
    var newsletterWidget;
    var followButtonWidget;
    var encodeURIComponentFake;
    var encodeURIComponentOriginal;
    var encodeURIComponent;

    beforeEach(function() {
      sharingButtonsWidget = {
        id: 123,
        buttons: [{service: 'facebook'}, {service: 'twitter'}],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'sharing-buttons',
        isActive: true
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
        mediaUrl: 'http://media',
        isActive: true
      };
      followButtonWidget = {
        id: 123,
        buttons: [
          {
            service: 'facebook',
            text: 'Facebook',
            hasCounter: false
          },
          {
            service: 'instagram',
            text: 'Instagram',
            hasCounter: false
          }
        ],
        buttonSize: 'large',
        orientation: 'vertical',
        buttonStyle: 'label',
        counterPosition: 'top',
        type: 'follow-buttons',
        isActive: true
      };
      encodeURIComponentFake = function(url) {
        return url;
      };

      encodeURIComponentOriginal = encodeURIComponent;
      encodeURIComponent = encodeURIComponentFake;
    });

    afterEach(function() {
      encodeURIComponent = encodeURIComponentOriginal;
    });

    it('generate tracking code by id', function() {
      createController(sharingButtonsWidget, 1, 1234, null, true);
      expect(WidgetCtrl.generateTrackingCode(1234)).toContain('["set", "hash_id", "1234"');
    });

    it('generate sharingLinks by id with selected channels', function() {
      createController(newsletterWidget, 1, 1, null, true);
      var links = WidgetCtrl.getSharingLinks(1);
      expect(links).toContain(host + '/tracker/share/facebook?url=http%3A%2F%2FURL&site_id=1&' +
        'message=test&media_url=http%3A%2F%2Fmedia');
      expect(links).toContain(host + '/tracker/share/twitter?url=http%3A%2F%2FURL&site_id=1&' +
        'message=test&media_url=http%3A%2F%2Fmedia');
      expect(links).not.toContain('linkedin');
    });

    it('generate sharingLinks with http if url without it', function() {
      newsletterWidget.pageUrl = 'URL';
      newsletterWidget.mediaUrl = 'media';
      createController(newsletterWidget, 1, 1, null, true);
      var links = WidgetCtrl.getSharingLinks(1);
      expect(links).toContain(host + '/tracker/share/facebook?url=http%3A%2F%2FURL&site_id=1&' +
        'message=test&media_url=http%3A%2F%2Fmedia');
      expect(links).toContain(host + '/tracker/share/twitter?url=http%3A%2F%2FURL&site_id=1&' +
        'message=test&media_url=http%3A%2F%2Fmedia');
      expect(links).not.toContain('linkedin');
    });

    it('generate sharingLinks without media', function() {
      newsletterWidget.mediaUrl = null;
      createController(newsletterWidget, 1, 1, null, true);
      var links = WidgetCtrl.getSharingLinks(1);
      expect(links).toContain(host + '/tracker/share/facebook?url=http%3A%2F%2FURL&site_id=1&message=test');
      expect(links).toContain(host + '/tracker/share/twitter?url=http%3A%2F%2FURL&site_id=1&message=test');
    });

    it('generate widget code', function() {
      createController(newsletterWidget, 1, 1, null, true);
      expect($scope.widgetCode()).toContain('data-id=\'124\'');
      $scope.widgetConfig = {};
      expect($scope.widgetCode()).toBe('');
    });

    it('generate tracking code depends on widget type', function() {
      createController(sharingButtonsWidget, 1, 1234, null, true);
      expect($scope.trackingCode()).toContain('["set", "hash_id", "1234"');
      $scope.widgetConfig = newsletterWidget;
      expect($scope.trackingCode()).toContain(host + '/tracker/share/facebook?url=http%3A%2F%2FURL&' +
        'site_id=1234&message=test&media_url=http%3A%2F%2Fmedia');
      $scope.widgetConfig = {};
      expect($scope.trackingCode()).toBe('');
    });

    it('check widgetTypes', function() {
      createController(newsletterWidget, 1, 1, null, true);
      expect($scope.isNewsletterWidget()).toBeTruthy();
      expect($scope.widgetTitle()).toBe('Newsletter widget');
      expect($scope.isSharingButtonsWidget()).toBeFalsy();
      $scope.widgetConfig = sharingButtonsWidget;
      expect($scope.isNewsletterWidget()).toBeFalsy();
      expect($scope.isSharingButtonsWidget()).toBeTruthy();
      expect($scope.widgetTitle()).toBe('Sharing Buttons Widget');

      // Follow Like checking
      $scope.widgetConfig = followButtonWidget;
      expect($scope.isNewsletterWidget()).toBeFalsy();
      expect($scope.isFollowWidget()).toBeTruthy();
      expect($scope.widgetTitle()).toBe('Follow Widget');
    });
  });
});
