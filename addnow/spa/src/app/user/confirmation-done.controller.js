(function() {
  'use strict';

  function ConfirmationDoneCtrl($scope, $routeParams, UserService) {
    $scope.mailToken = $routeParams.mailToken || '';

    UserService.confirmEmail($scope.mailToken)
      .success(function() {
        $scope.backendok = true;
      })
      .error(function() {
        $scope.backendok = false;
      });
  }

  angular.module('angulardash.user')
    .controller('ConfirmationDoneCtrl', ['$scope', '$routeParams', 'UserService', ConfirmationDoneCtrl]);
})();
