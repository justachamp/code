(function() {
  'use strict';

  function amChart() {
    var uniqueId = 1;
    return {
      restrict: 'E',
      replace: true,
      scope: {
        config: '=',
        provider: '=',
        daterange: '='
      },
      template: '<div style="min-width: 200px; position: relative; margin: 0 auto"></div>',
      link: function(scope, element) {
        var chart;
        var id;
        var height;
        id = element.attr('id');
        if (!id) {
          id = 'chart_' + uniqueId++;
          element.attr('id', id);
        }

        height = scope.config.height || '200px';
        element.css({
          height: height
        });
        scope.config.dataProvider = [];
        chart = AmCharts.makeChart(id, scope.config);

        chart.addListener('init', function(obj) {
          var chartContainer = $(obj.chart.containerDiv);

          chartContainer.after(
            '<div class="no-chart-data" style="display: none">Not enough data to display chart</div>'
          );
          obj.chart.noDataDiv = chartContainer.next('.no-chart-data');
          obj.chart.initialized = true;

          if (obj.chart.dataProvider.length === 0) {
            obj.chart.noDataDiv.show();
          }
        });

        scope.$watch('provider', function(newValue) {
          if (newValue) {
            chart.dataProvider = newValue;
            chart.validateData();
            angular.element(chart.containerDiv).show();

            //No data to display
            if (newValue.length === 0) {
              if (chart.noDataDiv) {
                chart.noDataDiv.show();
              } else {
                setTimeout(function() {
                  chart.noDataDiv.show();
                }, 200);
              }
            } else {
              chart.invalidateSize();
              if (chart.noDataDiv) {
                chart.noDataDiv.hide();
              }
            }
          }
        });
      }
    };
  }

  angular.module('angulardash.site').directive('amChart', amChart);
})();
