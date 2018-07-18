'use strict';

describe('RangeMap directive', function() {
  beforeEach(module('angulardash.site'));
  beforeEach(module('app/site/charts/range-map.html'));

  var $compile;
  var $rootScope;
  var amChartsSpy;
  var chart;
  var amChartsOriginal;

  beforeEach(inject(function(_$compile_, _$rootScope_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;

    amChartsSpy = jasmine.createSpyObj('AmCharts', ['makeChart']);
    chart = jasmine.createSpyObj('chart', ['validateData', 'validateNow', 'addListener']);
    chart.dataProvider = {
      areas: null
    };
    spyOn(chart.dataProvider, 'areas');
    amChartsSpy.makeChart.and.returnValue(chart);

    amChartsOriginal = AmCharts;
    AmCharts = amChartsSpy;
    $rootScope.config = {};
    $rootScope.provider = {};
  }));

  afterEach(function() {
    AmCharts = amChartsOriginal;
  });

  it('has rangemap block', function() {
    var element = $compile('<range-map data-config="config" data-provider="provider"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(element.children('#rangemap')).toBeDefined();
    expect(chart.validateNow).toHaveBeenCalled();
    expect(chart.validateData).toHaveBeenCalled();
    expect(chart.dataProvider.areas).toBe($rootScope.provider);
  });

  it('not works without provider', function() {
    $compile('<range-map data-config="config"></am-chart>"')($rootScope);
    $rootScope.$digest();

    expect(chart.validateData).not.toHaveBeenCalled();
  });
});
