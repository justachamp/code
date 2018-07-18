(function() {
  'use strict';

  function AccountSettingsService($http, AppSettings, $localStorage) {
    var backendApi = AppSettings.backendApi;

    this.updateSettings = function updateSettings(data, password) {
      var obj = {};
      if (password) {
        obj.oldPassword = password.oldPassword;
        obj.password = password.newPassword;
      }

      if (data) {
        obj.offset = data.timeZone;
        if ($localStorage.email !== data.email) {
          obj.email = data.email;
        }
      }

      return $http.patch(backendApi + 'account', obj);
    };

    this.getSettings = function getSettings() {
      return $http.get(backendApi + 'account');
    };

    this.updateAnalyticsIntegration = function updateAnalyticsIntegration(hasAnalytics) {
      return $http.patch(backendApi + 'account', {
        hasAnalytics: hasAnalytics
      });
    };
  }

  angular.module('angulardash.account-settings')
    .service('AccountSettingsService', ['$http', 'AppSettings', '$localStorage', AccountSettingsService]);
})();
