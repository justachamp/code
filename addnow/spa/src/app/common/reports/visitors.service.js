(function() {
  'use strict';

  function VisitorsService($http, AppSettings) {
    var backendApi = AppSettings.backendApi;
    var places = {};
    var maxTime = 3600;
    var params;
    var lastUpdateTime;

    function putVisitor(visitor) {
      //TODO: move it
      var now = moment().utc();
      var visitorKey = visitor.geo.longitude + ',' + visitor.geo.latitude;
      var visitorIsNotObsolete;
      var needUpdateVisitor;
      var time;

      visitor.key = visitorKey;
      if (visitor.source === '(not set)') {
        visitor.source = 'direct';
      }

      if (visitor.ts) {
        time = moment(visitor.ts).utc();
        visitor.time = now.diff(time, 'seconds');
      } else {
        visitor.time = 0;
      }

      visitorIsNotObsolete = visitor.time < maxTime;
      needUpdateVisitor = !places[visitorKey] || places[visitorKey].time > visitor.time;
      if (visitorIsNotObsolete && needUpdateVisitor) {
        places[visitorKey] = visitor;
      }
    }

    function removeObsoleteVisitors() {
      var visitor;
      var key;
      var delta = 0;

      if (lastUpdateTime) {
        delta = moment().utc().diff(lastUpdateTime, 'seconds');
      }

      for (key in places) {
        visitor = places[key];
        if (maxTime - visitor.time < delta) {
          delete places[key];
        } else {
          visitor.time += delta;
        }
      }
    }

    this.maxVisitorTime = maxTime;  // ttl in seconds
    this.reloadPeriod = 30000;

    /**
     * Get new visitors and remove old visitor from previous call
     */
    this.getVisitors = function(siteId, withHistory) {
      //1. clean old data + recalculate their weights
      //3. get new
      params = {};
      if (withHistory) {
        params.history = maxTime;
      }

      removeObsoleteVisitors();
      lastUpdateTime = moment().utc();
      return $http.get(backendApi + 'reports/sites/' + siteId + '/visitors', {
        params: params
      }).then(function(data) {
        var objs = data.data;
        var result = {};
        objs.forEach(putVisitor);
        result.places = places;
        if (!withHistory) {
          result.activeCount = objs.length;
        }

        return result;
      }, function(data) {
        //TODO
        return data;
      });
    };
  }

  angular.module('angulardash.common')
    .constant('moment', moment)
    .service('VisitorsService', ['$http', 'AppSettings', VisitorsService]);
})();
