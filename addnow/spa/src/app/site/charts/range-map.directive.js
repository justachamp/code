(function() {
  'use strict';

  function rangeMap() {
    return {
      restrict: 'E',
      replace: true,
      scope: {
        config: '=',
        provider: '=',
        topCountries: '='
      },
      templateUrl: 'app/site/charts/range-map.html',
      link: function(scope) {
        var map;
        var height;
        var config = angular.copy(scope.config);
        var rendered = false;
        height = config.height || '200px';
        angular.element('#rangemap').css({
          height: height
        });
        map = AmCharts.makeChart('rangemap', config);

        config.dataProvider = [];
        map.validateNow();
        map.addListener('rendered', function() {
          rendered = true;
        });

        scope.$watch('provider', function(newValue) {
          if (newValue) {
            map.dataProvider.areas = newValue;
            if (rendered) {
              map.dataProvider.zoomLevel = map.zoomLevel();
              map.dataProvider.zoomLatitude = map.zoomLatitude();
              map.dataProvider.zoomLongitude = map.zoomLongitude();
            }

            map.validateData();
          }
        });
      }
    };
  }

  angular.module('angulardash.site').directive('rangeMap', rangeMap);
})();
