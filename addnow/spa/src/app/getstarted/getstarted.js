(function() {
  'use strict';

  function configureRoutes($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/getstarted/getstartedS1.html',
        controller: 'GetStartedCtrl'
      })
      .when('/getstarted/2', {
        templateUrl: 'app/getstarted/getstartedS2.html',
        controller: 'GetStartedCtrl'
      });
  }

  angular.module('angulardash.getstarted', ['ngStorage', 'ngRoute']).config(['$routeProvider', configureRoutes]);
})();
