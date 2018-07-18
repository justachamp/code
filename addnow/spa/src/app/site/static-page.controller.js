(function() {
  'use strict';

  function StaticCtrl($scope, $routeParams, $location) {
    var pageId = $routeParams.pageId;
    var templates = {
      marketers: 'assets/views/marketers.html',
      publishers: 'assets/views/publishers.html',
      copyright: 'assets/views/copyright.html',
      privacy: 'assets/views/privacy.html',
      terms: 'assets/views/terms.html'
    };

    if (templates[pageId]) {
      $scope.template = templates[pageId];
    } else {
      $location.path('/');
    }
  }

  angular.module('angulardash.site')
    .controller('StaticCtrl', ['$scope', '$routeParams', '$location', StaticCtrl]);
})();
