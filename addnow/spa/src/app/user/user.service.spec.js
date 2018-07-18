'use strict';

describe('Service: UserService', function() {
  beforeEach(module('angulardash.user'));

  var $rootScope;
  var $httpBackend;
  var UserService;
  var AppSettings;
  var backendApi;

  beforeEach(inject(function(_$rootScope_, _$httpBackend_, _UserService_, _AppSettings_) {
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;
    UserService = _UserService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;
  }));

  describe('signUp', function() {
    it('should respond with token, id, and email when user registers', function() {
      $httpBackend.expectPOST(backendApi + 'users', {
        email: 'test@test.pl', password: '123qwe'
      }).respond(201, {id: 2, email: 'test@test.pl', token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'});
      UserService.signUp('test@test.pl', '123qwe');
      $httpBackend.flush();
    });
  });

  describe('signIn', function() {
    it('should respond with token when user exists', function() {
      $httpBackend.expectPOST(backendApi + 'tokens', {
        email: 'test@test.pl', password: '123qwe'
      }).respond(200, {token: '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'});
      UserService.signIn('test@test.pl', '123qwe');
      $httpBackend.flush();
    });
  });

  describe('forgotPass', function() {
    it('should respond with 204 code when user exists', function() {
      $httpBackend.expectPOST(backendApi + 'users/reset_password', {email: 'test@test.pl'}).respond(204);
      UserService.forgotPass('test@test.pl');
      $httpBackend.flush();
    });
  });
});
