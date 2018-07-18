(function() {
  'use strict';

  function VanityDomainService($http, TrackerSettings) {
    var backendApi = TrackerSettings.backendApi;

    // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
    this.getDomains = function(apiKey) {
      return $http.get(backendApi + 'vanity_domains', {
        params: {
          trim_api_key: encodeURIComponent(apiKey)
        }
      });
    };

    // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
  }

  angular.module('angulardash.common')
    .service('VanityDomainService', ['$http', 'TrackerSettings', VanityDomainService]);
})();
