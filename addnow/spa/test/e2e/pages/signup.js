'use strict';

var helper = require('./page-helper');

var Signup = function() {
  var signUpUrl = 'signup/';
  var emailSignUp = element(by.model('registration.email'));
  var passwordSignUp = element(by.model('registration.password'));
  var password2SignUp = element(by.model('registration.password2'));
  var submitSignUp = $('button.g4-button');
  var _this = this;

  this.goSignUpPage = function()  {
    helper.goUrl(signUpUrl);
  };

  this.signUp = function(email, password, confPassword)  {
    _this.goSignUpPage();
    emailSignUp.sendKeys(email);
    passwordSignUp.sendKeys(password);
    password2SignUp.sendKeys(confPassword);
    submitSignUp.click();
  };
};

module.exports = new Signup();
