(function() {
  'use strict';

  function WidgetService($http, AppSettings) {
    var backendApi = AppSettings.backendApi;

    this.addConfiguration = function addConfiguration(siteId, postObj) {
      return $http.post(backendApi + 'sites/' + siteId + '/widgets', postObj);
    };

    this.getConfigurationById = function getConfigurationById(siteId, widgetId) {
      return $http.get(backendApi + 'sites/' + siteId + '/widgets/' + widgetId);
    };

    this.editConfiguration = function editConfiguration(siteId, widgetId, obj) {
      return $http.patch(backendApi + 'sites/' + siteId + '/widgets/' + widgetId, obj);
    };

    this.getConfigurations = function getConfigurations(siteId, type) {
      var configUrl = backendApi + 'sites/' + siteId + '/widgets';
      if (type) {
        configUrl += '?type=' + type;
      }
      return $http.get(configUrl);
    };
  }

  angular.module('angulardash.widget')
    .service('WidgetService', ['$http', 'AppSettings', WidgetService]);
})();
