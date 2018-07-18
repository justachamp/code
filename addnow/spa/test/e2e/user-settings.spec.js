'use strict';

var signin = require('./pages/signin');
var userSettings = require('./pages/user-settings');
var expectUtils = require('./helpers/expect-utils');

describe('addnow', function() {
  var emailValue = '';
  var passwordValue = '';

  beforeAll(function() {
    signin.login('test@test.pl', '123qwe');
  });

  describe('Logged user in', function() {

    describe('Account setting view', function() {

      afterEach(function(done) {
        userSettings.setDefaultData(emailValue, passwordValue, function(err) {
          if (err) {
            done.fail(err);
          } else {
            done();
          }
        });

        emailValue = '';
        passwordValue = '';
      });

      it('should change timezone', function() {
        userSettings.setSettings('', '24', '', '', '');
        userSettings.goSettingsPage();
        expect(userSettings.getTimeZoneValue()).toBe('24');
      });

      it('should change password', function() {
        passwordValue = '1234';
        userSettings.setSettings('', '', '123qwe', passwordValue, passwordValue);
        userSettings.goSettingsPage();
        expectUtils.checkResetPassword('test@test.pl', passwordValue);
      });

      it('should change timezone and password', function() {
        passwordValue = '1234';
        userSettings.setSettings('', '24', '123qwe', passwordValue, passwordValue);
        userSettings.goSettingsPage();
        expect(userSettings.getTimeZoneValue()).toBe('24');
        expectUtils.checkResetPassword('test@test.pl', passwordValue); //TODO need to think about not one expect
      });

      //TODO need to change behavior (because of logout at changing email)
      /*
       xit('should change email and timezone', function() {
        userSettings.setSettings('test@test.com','23','','','');
        expect(userSettings.getTimeZoneValue()).toBe('23');
        expect(email.getAttribute('value')).toBe('test@test.com');
       });

       xit('should set email', function() {
             userSettings.setSettings('test@test.com','','','','');
             expect(userSettings.getEmailValue()).toBe('test@test.com');
       });

       xit('should change email and password', function() {
            userSettings.setSettings('test@test.com','','123qwe','1234','1234');
            expect(email.getAttribute('value')).toBe('test@test.com');
            helper.URLShouldBe('site/dashboard/1');
            expectUtils.checkResetPassword('test@test.pl','123qwe');
       });

       xit('should change timezone, password and email', function() {
          userSettings.setSettigns('test@test.com','24','123qwe','1234','1234');
          expect(userSettings.getEmailValue()).toBe('test@test.com');
          expect(userSettings.getTimeZoneValue()).toBe('23');
          helper.URLShouldBe('/site/dashboard/1');
          expectUtils.checkResetPassword('test@test.pl','123qwe');
       });*/
    });

    describe('should show error message', function() {
      it('about incorrect password', function() {
        userSettings.setSettings('', '', 'incorrect password', '1234', '1234');
        expectUtils.checkErrorIsVisible('Password is incorrect');
      });

      it('about password not match', function() {
        userSettings.setSettings('', '', '123qwe', '1234', '12345');
        expectUtils.checkErrorIsVisible('Passwords don\'t match.');
      });

      it('about required email field', function() {
        userSettings.setSettings('test', '', '', '', '');
        expectUtils.checkErrorIsVisible('You must enter valid email');
      });

      it('about necessary to add new password', function() {
        userSettings.setSettings('', '', '123qwe', '', '');
        expectUtils.checkErrorIsVisible('You did not enter a field.');
      });
    });
  });
});
