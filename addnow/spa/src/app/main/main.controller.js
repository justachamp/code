(function() {
  'use strict';

  function MainCtrl($location, SiteService) {
    SiteService.getSites().then(function(data) {
      if (data.data.length === 0) {
        $location.path('/site/add/');
      } else {
        $location.path('/site/dashboard/' + data.data[0].id);
      }
    });
  }

  angular.module('angulardash.main')
    .controller('MainCtrl', ['$location', 'SiteService', MainCtrl]);
})();
