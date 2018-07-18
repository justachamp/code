(function() {
  'use strict';

  function configureRoutes($routeProvider) {
    $routeProvider
      .when('/dashboard', {
        templateUrl: 'app/main/main.html',
        controller: 'MainCtrl'
      });
  }

  angular.module('angulardash.main', ['angulardash.site']).config(['$routeProvider', configureRoutes]);
})();
