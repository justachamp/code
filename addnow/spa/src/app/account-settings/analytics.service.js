(function() {
  'use strict';

  function AnalyticsService($http, AppSettings) {
    var backendApi = AppSettings.backendApi;

    this.login = function() {
      return $http.get(backendApi + 'analytics/login');
    };

    this.logout = function() {
      return $http.get(backendApi + 'analytics/logout');
    };

    this.addCode = function(params) {
      return $http.post(backendApi + 'analytics/auth', params);
    };

    this.getAccounts = function() {
      return $http.get(backendApi + 'analytics/accounts');
    };
  }

  angular.module('angulardash.account-settings').constant('moment', moment)
    .service('AnalyticsService', ['$http', 'AppSettings', AnalyticsService]);
})();
