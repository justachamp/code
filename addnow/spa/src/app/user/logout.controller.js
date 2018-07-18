(function() {
  'use strict';

  function LogoutCtrl($location, $localStorage, $rootScope) {
    $localStorage.$reset();
    $rootScope.token = null;
    $location.path('/');
  }

  angular.module('angulardash.user')
    .controller('LogoutCtrl', ['$location', '$localStorage', '$rootScope', LogoutCtrl]);
})();
