(function() {
  'use strict';

  function ConfirmationCtrl($scope, $localStorage, $routeParams, UserService) {
    $scope.email = $localStorage.email;
    $scope.resend = function() {
      if ($scope.email) {
        UserService.verify($scope.email);
      }
    };

    if (!$routeParams.sent) {
      $scope.resend();
    }
  }

  angular.module('angulardash.user')
    .controller('ConfirmationCtrl', ['$scope', '$localStorage', '$routeParams', 'UserService', ConfirmationCtrl]);

})();
