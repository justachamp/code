(function() {
  'use strict';

  function configureAnalytics(AnalyticsProvider) {
    // initial configuration
    AnalyticsProvider.setAccount('UA-47358447-4');

    // track all routes (or not)
    AnalyticsProvider.trackPages(true);

    // track all url query params (default is false)
    AnalyticsProvider.trackUrlParams(true);

    // Use analytics.js instead of ga.js
    AnalyticsProvider.useAnalytics(true);
  }

  function configureRoutes($routeProvider, $locationProvider) {
    $routeProvider
      .when('/internal-error', {
        templateUrl: '500.html'
      })
      .otherwise({
        redirectTo: '/'
      });
    $locationProvider.html5Mode(true);
  }

  angular.module('angulardash', ['ngSanitize', 'ngRoute', 'ngStorage', 'angular-google-analytics',
      'angulardash.account-settings', 'angulardash.configuration', 'angulardash.common', 'angulardash.getstarted',
      'angulardash.main', 'angulardash.navbar', 'angulardash.user', 'angulardash.user', 'angulardash.widget'])
    .config(['$routeProvider', '$locationProvider', configureRoutes])
    .config(configureAnalytics)
    .run(['$localStorage', '$http', '$rootScope', function($localStorage, $http, $rootScope) {
      $rootScope.token = $localStorage.token;
    }]);
})();
