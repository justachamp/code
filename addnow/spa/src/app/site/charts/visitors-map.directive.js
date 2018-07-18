(function() {
  'use strict';

  function visitorsMap(VisitorsService, $interval) {
    return {
      restrict: 'E',
      replace: true,
      scope: {
        siteId: '='
      },
      templateUrl: 'app/site/charts/visitors-map.html',
      link: function(scope) {
        var config;
        var map;
        var colorMax;
        var colorMin;
        var minAlpha;
        var maxAlpha;
        var interval;
        var minBulletSize;
        var maxBulletSize;
        var minPointWeight;
        var maxPointWeight;
        var maxSquare;
        var minSquare;
        var rendered = false;
        var hasHistory = true;

        //---------------configuration----------------
        //colors in RGB format
        colorMax = [255, 0, 0];
        colorMin = [0, 0, 255];

        //opacity settings
        minAlpha = 0.3;
        maxAlpha = 1;

        //bubble size settings
        minBulletSize = 10;
        maxBulletSize = 40;

        minPointWeight = 0;
        maxPointWeight = VisitorsService.maxVisitorTime;

        //---------------configuration----------------

        // it's better to use circle square to show difference between values, not a radius
        maxSquare = maxBulletSize * maxBulletSize * 2 * Math.PI;
        minSquare = minBulletSize * minBulletSize * 2 * Math.PI;

        function getColor(percent) {
          var i;
          var color = [];
          for (i = 0; i < 3; i++) {
            color[i] = colorMin[i] + Math.ceil(percent * (colorMax[i] - colorMin[i]));
          }

          return 'rgb(' + color.join(',') + ')';
        }

        function getOpacity(percent) {
          return minAlpha + percent * (maxAlpha - minAlpha);
        }

        function getBalloonText(visitor) {
          var text = '';
          if (visitor.geo.city) {
            text += '<p>City: ' + visitor.geo.city + '</p>';
          }

          text += '<p>Country: ' + visitor.geo.country + '</p>';
          if (visitor.source) {
            text += '<p>source: ' + visitor.source + '</p>';
          }

          return text;
        }

        function renderData(visitors) {
          var key;
          var visitor;
          var value;
          var square;
          var size;
          var percents;

          map.dataProvider.images = [];
          for (key in visitors) {
            visitor = visitors[key];
            value = VisitorsService.maxVisitorTime - visitor.time;

            // calculate size of a bubble
            square = ((value - minPointWeight) / (maxPointWeight - minPointWeight)) *
              (maxSquare - minSquare) + minSquare;
            if (square < minSquare) {
              square = minSquare;
            }

            size = Math.sqrt(square / (Math.PI * 2));
            percents = square / (maxSquare - minSquare);

            map.dataProvider.images.push({
              alpha: getOpacity(percents),
              type: 'bubble',
              width: size,
              height: size,
              color: getColor(percents),
              longitude: visitor.geo.longitude,
              latitude: visitor.geo.latitude,
              customData: getBalloonText(visitor)
            });
          }

          // set same zoom levels to retain map position/zoom
          if (rendered) {
            map.dataProvider.zoomLevel = map.zoomLevel();
            map.dataProvider.zoomLatitude = map.zoomLatitude();
            map.dataProvider.zoomLongitude = map.zoomLongitude();
          }

          map.validateData();
        }

        config = {
          type: 'map',
          theme: 'gravity4',
          pathToImages: 'assets/images/amcharts/ammap/',
          panEventsEnabled: true,

          //backgroundColor : '#535364',
          //backgroundAlpha : 1,
          zoomControl: {
            panControlEnabled: true,
            zoomControlEnabled: true
          },
          dragMap: true,
          zoomOnDoubleClick: true,
          height: 400,
          dataProvider: {
            map: 'worldHigh'
          },
          responsive: {
            enabled: true
          },
          imagesSettings: {
            balloonText: '[[customData]]'
          },
          balloon: {
            adjustBorderColor: true,
            color: '#000000',
            cornerRadius: 5,
            fillColor: '#FFFFFF'
          }
        };

        angular.element('#visitorsmap').css({
          height: config.height
        });
        map = AmCharts.makeChart('visitorsmap', config);
        map.addListener('rendered', function() {
          rendered = true;
        });

        map.dataProvider.images = [];
        map.validateNow();
        scope.count = 0;

        scope.timeText = moment.duration(VisitorsService.maxVisitorTime, 'seconds').humanize();

        function getData(history, cb) {
          VisitorsService.getVisitors(scope.siteId, history).then(function(result) {
            renderData(result.places);
            scope.count = result.activeCount;
            if (cb) {
              cb();
            }
          });
        }

        //make history and realtime calls
        getData(hasHistory, function() {
          hasHistory = false;
          getData(hasHistory);
        });

        interval = $interval(function() {
          getData(hasHistory);
        }, VisitorsService.reloadPeriod);

        scope.$on('$destroy', function() {
          $interval.cancel(interval);
        });
      }
    };
  }

  angular.module('angulardash.site').constant('moment', moment)
    .directive('visitorsMap', ['VisitorsService', '$interval', visitorsMap]);
})();
