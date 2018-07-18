(function() {
  'use strict';

  function GetStartedCtrl($scope, $location, $localStorage) {
    $scope.data = {};
    $scope.data.website = $location.search().website || '';
    $scope.redirect = function redirect(path) {
      $location.path(path).search({website: $scope.data.website, sliderId: $scope.slider.carId});
    };

    $scope.submitform = function submitform(valid) {
      if (valid) {
        $location.path('/getstarted/2').search('website', $scope.data.website);
        $localStorage.website = $scope.data.website;
      }
    };
  }

  angular.module('angulardash.getstarted')
    .controller('GetStartedCtrl', ['$scope', '$location', '$localStorage', GetStartedCtrl]);
})();
