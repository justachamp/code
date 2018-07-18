'use strict';

var helper = require('./page-helper');
var ApiClient = require('../helpers/api-client');
var LocalStorage = require('../helpers/local-storage');

var Settings = function() {
  var passwordCurrentValue = '123qwe';
  var emailCurrentValue = 'test@test.pl';

  var email = element(by.model('formData.email'));
  var offset = element(by.model('formData.timeZone'));

  var oldPassword = element(by.model('formData.password'));
  var password = element(by.model('formData.newPassword1'));
  var confirmPassword = element(by.model('formData.newPassword2'));

  var submitEl = element(by.cssContainingText('form button.g4-button', 'SAVE CHANGES'));
  var settingsUrl = 'settings/';

  var _this = this;

  this.setSettings = function(emailValue, idTimezone, oldPasswordValue, passwordValue, confirmPasswordValue) {
    _this.goSettingsPage();
    setEmail(emailValue);
    setTimezone(idTimezone);
    setPassword(oldPasswordValue);
    setNewPassword(passwordValue);
    setConfirmPassword(confirmPasswordValue);
    submit();
  };

  this.goSettingsPage = function() {
    helper.goUrl(settingsUrl);
    browser.sleep(1000);
  };

  this.setDefaultData = function(emailValue, passwordValue, done) {
    if (emailValue === '') {
      emailValue = emailCurrentValue;
    }

    if (passwordValue === '') {
      passwordValue = passwordCurrentValue;
    }

    LocalStorage.getValue('ngStorage-token').then(function(token) {
      var re = new RegExp('\"', 'g');
      token = token.replace(re, '');
      console.log('TOKEN', token);

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      ApiClient.updateAccount(token, {
        offset: 60,
        email: emailValue,
        old_password: passwordValue,
        password: '123qwe'
      }, function(error, response, body) {
        if (error || response.statusCode !== 200) {
          console.log('Error:', error);
          console.log('RESPONSE:', body);
          done('Can\'t update user account');
        } else {
          done();
        }
      });

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
    }, done);
  };

  var set = function(field, fieldValue) {
    if (fieldValue !== '' || fieldValue === 'empty')
    {
      field.clear();
      field.sendKeys(fieldValue);
    }
  };

  var submit = function() {
    submitEl.click();
    browser.sleep(1000);
  };

  var setEmail = function(emailValue) {
    set(email, emailValue);
    if (emailValue !== '') {
      emailCurrentValue = emailValue;//TODO need to think how we can set value after correct submitting
    }
  };

  var setPassword = function(passwordValue) {
    set(oldPassword, passwordValue);
  };

  var setTimezone = function(idTimezone) {
    if (idTimezone !== '')
    {
      element.all(by.options('date.value as date.name for date in dates')).get(idTimezone).click();//TODO select timezon: need to find other way to select the timezone
    }
  };

  var setNewPassword = function(passwordValue) {
    set(password, passwordValue);

    if (passwordValue !== '') {
      passwordCurrentValue = passwordValue;
    }
  };

  var setConfirmPassword = function(confirmPasswordValue) {
    set(confirmPassword, confirmPasswordValue);
  };

  this.getTimeZoneValue = function() {
    browser.sleep(3000);
    return offset.getAttribute('value');
  };
};

module.exports = new Settings();
