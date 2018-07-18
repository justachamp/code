(function() {
  'use strict';

  function UserCtrl($scope, $location, UserService, $localStorage, $routeParams,
                    ErrorHandler, $rootScope) {
    $localStorage.$reset();
    $rootScope.token = null;

    //hack for resetPass form
    //TODO: refactor it
    $scope.forms = {};
    $scope.forgot = {};
    $scope.registration = {};
    $scope.conf = $location.search().email || '';
    $scope.mailToken = $routeParams.mailToken || '';
    $scope.errors = {};
    $scope.submitSignUp = function() {
      //flush server errors
      ErrorHandler.flushServerErrors($scope.forms.form, $scope.errors);
      if ($scope.forms.form.$valid) {
        UserService.signUp($scope.registration.email, $scope.registration.password)
          .success(function() {
            $localStorage.$default({
              email: $scope.registration.email
            });
            $location.search('sent', true);
            $location.path('/confirmation');
          })
          .error(function(data, status) {
            $scope.errors = ErrorHandler.parseResponse(status, data, $scope.forms.form);
          });
      }
    };

    $scope.submitSignIn = function() {
      ErrorHandler.flushServerErrors($scope.forms.form, $scope.errors);
      if ($scope.forms.form.$invalid) {
        return;
      }

      UserService.signIn($scope.registration.email, $scope.registration.password)
        .success(function(data) {
          $scope.$storage = $localStorage.$default({
            email: $scope.registration.email,
            token: data.token
          });
          $rootScope.token = data.token;
          if ($location.search().website) {
            $location.path('/site/add');
          } else {
            $location.path('/dashboard');
          }
        })
        .error(function(data, status) {
          $scope.errors = ErrorHandler.parseResponse(status, data, $scope.forms.form);
          var errors = $scope.errors.nonFieldServerErrors;
          if (errors.length === 1 &&
            errors[0] === 'You need to verify your account before logging in.') {
            $localStorage.$default({
              email: $scope.registration.email
            });
            errors[0] = errors[0] +
              '<br/> Don\'t see the message? <a href="/confirmation">Resend the message</a>';
          }
        });
    };

    $scope.submitResetPass = function() {
      ErrorHandler.flushServerErrors($scope.forms.form, $scope.errors);
      if ($scope.forms.form.$valid) {
        UserService.resetPass($scope.mailToken, $scope.registration.password)
          .success(function() {
            $scope.backendok = true;
          })
          .error(function(data, status) {
            $scope.errors = ErrorHandler.parseResponse(status, data, $scope.forms.form);
          });
      }
    };

    $scope.submitForgotPass = function() {
      ErrorHandler.flushServerErrors($scope.forms.form, $scope.errors);
      if ($scope.forms.form.$valid) {
        UserService.forgotPass($scope.forgot.mail)
          .success(function() {
            $scope.backendok = true;
          })
          .error(function(data, status) {
            $scope.errors = ErrorHandler.parseResponse(status, data, $scope.forms.form);
          });
      }
    };
  }

  angular.module('angulardash.user')
    .controller('UserCtrl', ['$scope', '$location', 'UserService', '$localStorage', '$routeParams',
      'ErrorHandler', '$rootScope', UserCtrl]);
})();
