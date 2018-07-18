(function() {
  'use strict';

  function configureHttpProvider($httpProvider) {
    $httpProvider.interceptors.push(['$localStorage', '$location', '$q', 'TransformUtils', 'AppSettings',
      'TrackerSettings',
      function($localStorage, $location, $q, TransformUtils, AppSettings, TrackerSettings) {
        return {
          request: function(config) {
            if ($localStorage.token) {
              config.headers.Authorization = 'JWT ' + $localStorage.token;
            }

            //convert request to backend to snake_case
            if (config.data && config.url.indexOf(AppSettings.backendApi) !== -1) {
              config.data = TransformUtils.toSnakeCase(config.data);
            }

            return config;
          },

          response: function(response) {
            var responseUrl = response.config.url;
            var isApiBackendCall = (responseUrl.indexOf(AppSettings.backendApi) !== -1) ||
              (responseUrl.indexOf(TrackerSettings.backendApi) !== -1);

            //convert backend response to camelCase
            if (response.data && isApiBackendCall) {
              response.data = TransformUtils.toCamelCase(response.data);
            }

            return response;
          },

          responseError: function(rejection) {
            if (rejection.status === 401 || rejection.status === 403) {
              $localStorage.$reset();
              $location.path('/signin');
            }

            return $q.reject(rejection);
          }
        };
      }]);
  }

  angular.module('angulardash.transform-middleware', ['angulardash.configuration', 'ngStorage'])
    .config(['$httpProvider', configureHttpProvider]);
})();
