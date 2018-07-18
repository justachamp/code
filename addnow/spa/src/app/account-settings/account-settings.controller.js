(function() {
  'use strict';

  function AccountSettingsCtrl($scope, $location, AccountSettingsService, AccountSettingsFactory, ErrorHandler, $localStorage,
                               AnalyticsService, $window) {
    var clearFormPasswordFields;
    $scope.formData = {};
    $scope.formData.password = '';
    $scope.formData.timeZone = 0;
    $scope.errors = {};
    $scope.dates = AccountSettingsFactory.timeZones;

    clearFormPasswordFields = function clearFormPasswordFields() {
      $scope.formData.password = '';
      $scope.formData.newPassword1 = '';
      $scope.formData.newPassword2 = '';
    };

    $scope.getSettings = function getSettings() {
      AccountSettingsService.getSettings().then(function(data) {
        $scope.formData.email = $localStorage.email;
        $scope.formData.timeZone = data.data.offset;
        $scope.hasAnalytics = data.data.hasAnalytics;
      });
    };

    $scope.getSettings();

    $scope.removeauth = function removeauth() {
      AnalyticsService.logout().then(function() {
        return AccountSettingsService.updateAnalyticsIntegration(false);
      }).then(function() {
        $scope.hasAnalytics = false;
      }).catch(function() {
        //TODO: add error handling
      });
    };

    $scope.auth = function auth() {
      var url;
      AnalyticsService.login().then(function(data) {
        url = data.data.authUrl;
        $window.location.href = url;
      }, function() {
        //TODO: add error handling
      });
    };

    $scope.submitAccChanges = function submitAccChanges() {
      var isDirtyData = false;
      var accData = null;
      var passwordData = null;
      ErrorHandler.flushServerErrors($scope.form, $scope.errors);
      if ($scope.form.$invalid) {
        return;
      }

      isDirtyData = $scope.form.email.$dirty || $scope.form.time.$dirty;
      if (isDirtyData) {
        accData = {
          timeZone: $scope.formData.timeZone,
          email: $scope.formData.email
        };
      }

      if ($scope.formData.newPassword2) {
        passwordData = {
          oldPassword: $scope.formData.password,
          newPassword: $scope.formData.newPassword2
        };
      }

      AccountSettingsService.updateSettings(accData, passwordData).success(function(data) {
        $scope.formData.timeZone = data.offset;
        if (data.email) {
          $scope.formData.email = data.email;
          $localStorage.email = $scope.formData.email;
        }

        clearFormPasswordFields();
        $scope.form.$setPristine();
        $location.path('/dashboard');
      }).error(function(data, status) {
        if (data.oldPassword) {
          data.password = data.oldPassword;
          delete data.oldPassword;
        }

        $scope.errors = ErrorHandler.parseResponse(status, data, $scope.form);
      });
    };
  }

  angular.module('angulardash.account-settings')
    .controller('AccountSettingsCtrl', ['$scope', '$location', 'AccountSettingsService', 'AccountSettingsFactory',
      'ErrorHandler', '$localStorage', 'AnalyticsService', '$window', AccountSettingsCtrl]);

})();
