(function() {
  'use strict';

  function AnalyticsAuthCtrl($location, $routeParams, AnalyticsService, AccountSettingsService) {
    AnalyticsService.addCode($routeParams).then(function() {
      return AccountSettingsService.updateAnalyticsIntegration(true);
    }).then(function() {
        $location.search({});
        $location.path('/settings');
      },

      function() {
        AnalyticsService.logout();
        $location.search({});
        $location.path('/settings');
      });
  }

  angular.module('angulardash.account-settings')
    .controller('AnalyticsAuthCtrl', ['$location', '$routeParams', 'AnalyticsService',
      'AccountSettingsService', AnalyticsAuthCtrl]);
})();
