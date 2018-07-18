'use strict';

describe('AccountSettingsService', function() {
  beforeEach(module('angulardash.account-settings'));

  var $rootScope;
  var $httpBackend;
  var AccountSettingsService;
  var AppSettings;
  var backendApi;

  beforeEach(inject(function(_$rootScope_, _$httpBackend_, _AccountSettingsService_, _AppSettings_) {
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;
    AccountSettingsService = _AccountSettingsService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;
  }));

  describe('updateSettings for account data', function() {
    it('should respond with email end offset', function() {
      $httpBackend.expectPATCH(backendApi + 'account', {
        offset: 60, email: 'test@test.pl'}
      ).respond(200, {email:'test@test.pl', offset: 60});
      AccountSettingsService.updateSettings({timeZone: 60, email: 'test@test.pl'});
      $httpBackend.flush();
    });
  });

  describe('updateSettings for account data and password', function() {
    it('should respond with email end offset', function() {
      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      $httpBackend.expectPATCH(backendApi + 'account', {
        offset: 60, old_password: '123qwe', password: '1234', email: 'test@test.pl'
      }).respond(200, {email:'test@test.pl', offset: 60});

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      AccountSettingsService.updateSettings({
        timeZone: 60, email: 'test@test.pl'
      }, {
        oldPassword: '123qwe',
        newPassword: '1234'
      });
      $httpBackend.flush();
    });
  });

  describe('getSettings', function() {
    it('should respond with settings', function() {
      $httpBackend.expectGET(backendApi + 'account').respond(200, {offset: 60});
      AccountSettingsService.getSettings();
      $httpBackend.flush();
    });
  });
});
