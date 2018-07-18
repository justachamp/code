(function() {
  'use strict';

  function ReminderUnsubscribeCtrl($scope, $routeParams, UserService) {
    $scope.token = $routeParams.token || '';

    UserService.remindersUnsubscribe($scope.token)
      .success(function() {
        $scope.backendok = true;
      })
      .error(function() {
        $scope.backendok = false;
      });
  }

  angular.module('angulardash.user')
    .controller('ReminderUnsubscribeCtrl', ['$scope', '$routeParams', 'UserService', ReminderUnsubscribeCtrl]);
})();
