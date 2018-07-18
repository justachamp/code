'use strict';

describe('AmChart directive', function() {
  beforeEach(module('angulardash.site'));

  var $compile;
  var $rootScope;
  var amChartsSpy;
  var chart;
  var amChartsOriginal;

  beforeEach(inject(function(_$compile_, _$rootScope_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;

    amChartsSpy = jasmine.createSpyObj('AmCharts', ['makeChart', 'pause', 'stop', 'rewind']);
    chart = jasmine.createSpyObj('chart', ['addListener', 'validateData', 'containerDiv', 'invalidateSize']);
    chart.noDataDiv = {
      hide: function() {},

      show: function() {}
    };
    spyOn(chart.noDataDiv, 'show');
    amChartsSpy.makeChart.and.returnValue(chart);

    amChartsOriginal = AmCharts;
    AmCharts = amChartsSpy;
    $rootScope.config = {};
    $rootScope.provider = {};
  }));

  afterEach(function() {
    AmCharts = amChartsOriginal;
  });

  it('generates random id', function() {
    var element = $compile('<am-chart data-config="config" data-provider="provider"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(element.attr('id')).toContain('chart_');
    expect(chart.validateData).toHaveBeenCalled();
  });

  it('uses attr id', function() {
    var element = $compile(
      '<am-chart id="my" data-config="config" data-provider="provider"></am-chart>"'
    )($rootScope);
    $rootScope.$digest();

    expect(element.attr('id')).toBe('my');
    expect(chart.validateData).toHaveBeenCalled();
  });

  it('shows noDataDiv if provider is []', function() {
    $compile('<am-chart data-config="config" data-provider="[]"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(chart.noDataDiv.show).toHaveBeenCalled();
    expect(chart.validateData).toHaveBeenCalled();
  });

  it('not works without provider', function() {
    $compile('<am-chart data-config="config"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(chart.validateData).not.toHaveBeenCalled();
  });

  it('not call noDataDiv.hode if provider is not empty and noDataDiv is null', function() {
    chart.noDataDiv = null;
    $compile('<am-chart data-config="config" data-provider="provider"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(chart.invalidateSize).toHaveBeenCalled();
  });
});
