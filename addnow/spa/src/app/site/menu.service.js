(function() {
  'use strict';

  function MenuService($q, SiteService, $localStorage, moment) {
    var sites = {};
    var needUpload = false;

    this.uploadMenuItems = function() {
      needUpload = true;
    };

    this.getMenu = function() {
      var deferred = $q.defer();
      var promiseSites;
      if (sites && !needUpload) {
        deferred.resolve(sites);
      } else {
        promiseSites = SiteService.getSites();
        promiseSites.success(function(data) {
          sites = data;
          deferred.resolve(sites);
          needUpload = false;
        }).catch(function(err) {
          needUpload = true;
          deferred.reject(err);
        });
      }

      return deferred.promise;
    };

    this.markMenuItemsForUpdate = function() {
      //need to touch localStorage to sync menu update between browser tabs
      $localStorage.menuUpdatedTs = moment();
    };

    this.uploadMenuItems();
  }

  angular.module('angulardash.site')
    .constant('moment', moment)
    .service('MenuService', ['$q', 'SiteService', '$localStorage', 'moment', MenuService]);
})();
