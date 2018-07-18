(function() {
  'use strict';

  function configureRoutes($routeProvider) {
    $routeProvider
      .when('/settings', {
        templateUrl: 'app/account-settings/account-settings.html',
        controller: 'AccountSettingsCtrl'
      })
      .when('/analytics/auth/', {
        template: '',
        controller: 'AnalyticsAuthCtrl'
      });
  }

  angular.module('angulardash.account-settings', ['angulardash.transform-middleware', 'angulardash.common',
    'ngStorage', 'angulardash.configuration', 'ngRoute']).config(['$routeProvider', configureRoutes]);
})();
