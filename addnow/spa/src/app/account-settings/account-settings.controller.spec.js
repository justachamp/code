'use strict';

describe('AccountSettingsCtrl', function() {
  beforeEach(module('angulardash.account-settings'));

  var $scope;
  var $controller;
  var $httpBackend;
  var $location;
  var $localStorage;
  var AccountSettingsCtrl;
  var AccountSettingsService;
  var AppSettings;
  var backendApi;

  function createController(isValidForm) {
    AccountSettingsCtrl = $controller('AccountSettingsCtrl', {
      $scope: $scope,
      $location: $location,
      $localStorage: $localStorage
    });
    $scope.form = {
      email: {
        $dirty: true
      },
      time: {
        $dirty: true
      },
      $valid: isValidForm,
      $invalid: !isValidForm,
      $setPristine: function() {}
    };
  }

  beforeEach(inject(function($rootScope, _$controller_, _$httpBackend_, _AccountSettingsService_, _AppSettings_) {
    $scope = $rootScope.$new();
    $controller = _$controller_;
    $httpBackend = _$httpBackend_;
    AccountSettingsService = _AccountSettingsService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;

    $location = jasmine.createSpyObj('$location', ['path', 'search', 'url']);
    $localStorage = jasmine.createSpyObj('$localStorage', ['$default']);
    $location.path.and.returnValue('/');
    $location.search.and.returnValue({website:'ww.pl'});
  }));

  describe('submitAccChanges', function() {
    beforeEach(function() {
      createController(true);
      $scope.formData.email = 'test@test.pl';
      $scope.formData.password = '123qwe';
      $scope.formData.timeZone = 60;
    });

    it('should run updateSettings service for data changing', function() {
      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectGET(backendApi + 'account').respond(200, {offset: 60, has_analytics: false});

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectPATCH(backendApi + 'account', {
        offset: 60, email: 'test@test.pl'
      }).respond(200, {email:'test@test.pl', offset: 60});
      $scope.submitAccChanges();
      $httpBackend.flush();
    });

    it('should run updateSettings service for password changing', function() {
      $scope.formData.newPassword2 = '1234';

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectGET(backendApi + 'account').respond(200, {offset: 60, has_analytics: false});
      $httpBackend.expectPATCH(backendApi + 'account', {
        offset: 60, old_password: '123qwe', password: '1234', email: 'test@test.pl'
      }).respond(200, {email:'test@test.pl', offset: 60});

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      $scope.submitAccChanges();
      $httpBackend.flush();
    });

    it('should get correct time zone from api at page load', function() {
      $scope.formData.timeZone = 0;
      $httpBackend.expectGET(backendApi + 'account').respond(200, {offset: 60});
      $httpBackend.flush();
      expect($scope.formData.timeZone).toEqual(60);
    });
  });
});
