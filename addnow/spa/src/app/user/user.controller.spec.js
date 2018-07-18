'use strict';

describe('Controller: UserCtrl', function() {
  beforeEach(module('angulardash.user'));

  var $scope;
  var $controller;
  var $httpBackend;
  var $location;
  var $localStorage;
  var UserCtrl;
  var UserService;
  var AppSettings;
  var backendApi;

  function createController(isValidForm) {
    UserCtrl = $controller('UserCtrl', {
      $scope: $scope,
      $location: $location,
      $localStorage: $localStorage
    });
    $scope.forms = {
      form: {
        $valid: isValidForm,
        $invalid: !isValidForm
      }
    };
  }

  beforeEach(inject(function($rootScope, _$controller_, _$httpBackend_, _UserService_, _AppSettings_) {
    $scope = $rootScope.$new();
    $controller = _$controller_;
    $httpBackend = _$httpBackend_;
    UserService = _UserService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;

    $location = jasmine.createSpyObj('$location', ['path', 'search', 'url']);
    $localStorage = jasmine.createSpyObj('$localStorage', ['$default', '$reset']);
    $location.path.and.returnValue('/');
    $location.search.and.returnValue({website: 'ww.pl'});
  }));

  describe('submitSignUp', function() {
    beforeEach(function() {
      createController(true);
      $scope.registration.email = 'test@test.pl';
      $scope.registration.password = '123qwe';
    });

    it('it should run signup service', function() {

      $httpBackend.expectPOST(backendApi + 'users', {
        email: 'test@test.pl', password: '123qwe'
      }).respond(201, {id: 2, email: 'test@test.pl', token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'});
      $scope.submitSignUp();
      $httpBackend.flush();
    });
  });

  describe('submitSignIn', function() {
    beforeEach(function() {
      createController(true);
      $scope.registration.email = 'test@test.pl';
      $scope.registration.password = '123qwe';
    });

    it('it should run signin service', function() {
      $scope.forms.form.email = 'test';
      $httpBackend.expectPOST(backendApi + 'tokens', {
        email: 'test@test.pl', password: '123qwe'
      }).respond(200, {token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'});
      $scope.submitSignIn();
      $httpBackend.flush();
    });
  });

  describe('submitForgotPass', function() {
    beforeEach(function() {
      createController(true);
    });

    it('it should run forgot pass service', function() {
      $scope.forgot = {mail: 'test@test.pl'};
      $httpBackend.expectPOST(backendApi + 'users/reset_password', {email: 'test@test.pl'}).respond(204);
      $scope.submitForgotPass();
      $httpBackend.flush();
    });
  });
});
