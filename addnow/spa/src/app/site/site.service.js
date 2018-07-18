(function() {
  'use strict';

  function SiteService($http, AppSettings, $resource) {
    var backendApi = AppSettings.backendApi;

    this.addSite = function addSite(postObj) {
      return $http.post(backendApi + 'sites', postObj);
    };

    this.getSiteById = function getSiteById(id) {
      return $http.get(backendApi + 'sites/' + id);
    };

    this.editSite = function editSite(id, site) {
      return $http.put(backendApi + 'sites/' + id, site);
    };

    this.patchSite = function patchSite(id, partials) {
      return $http.patch(backendApi + 'sites/' + id, partials);
    };

    this.getReportResource = function getReportResource() {
      return $resource(backendApi + 'digest/:id');
    };

    this.getSites = function getSites() {
      return $http.get(backendApi + 'sites');
    };
  }

  angular.module('angulardash.site')
    .service('SiteService', ['$http', 'AppSettings', '$resource', SiteService]);
})();
