'use strict';

describe('Slider', function() {
  beforeEach(module('angulardash.common'));

  var $compile;
  var $rootScope;

  beforeEach(inject(function(_$compile_, _$rootScope_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;

    $rootScope.buttonSizeIndex = 0;
    $rootScope.buttonSizes = ['small', 'medium'];
  }));

  it('uses ticks labels', function() {
    var element;
    var ticks;

    element = $compile(
      '<span slider ng-model="buttonSizeIndex" value="buttonSizeIndex" handle="round" step="1" ticks-labels="::buttonSizes"></span>'
    )($rootScope);
    $rootScope.$digest();
    ticks = element.find('.slider-tick-label');

    expect(ticks.length).toBe(2);
    expect(ticks[0].innerHTML).toBe('small');
    expect(ticks[1].innerHTML).toBe('medium');
  });

  it('uses ticks and ticks labels', function() {
    var element;
    var ticks;

    $rootScope.indexes = [100,  500];
    element = $compile(
      '<span slider ng-model="buttonSizeIndex" value="buttonSizeIndex" handle="round" step="1" ticks-labels="::buttonSizes" ticks="indexes"></span>'
    )($rootScope);
    $rootScope.$digest();
    ticks = element.find('.slider-tick-label');

    expect(ticks.length).toBe(2);
    expect(ticks[0].innerHTML).toBe('small');
    expect(ticks[1].innerHTML).toBe('medium');
  });

  it('uses range as array and string', function() {
    var tooltip = '200,500';
    var element;

    $rootScope.valueStr = '[200, 500]';
    $rootScope.min = 0;
    $rootScope.max = 1000;

    element = $compile(
      '<span slider ng-model="valueStr" min="min" max="max" value="valueStr" handle="round" step="1" range="true"></span>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.slider-input').attr('value')).toBe(tooltip);

    $rootScope.value = [200, 500];
    element = $compile(
      '<span slider ng-model="value" min="min" max="max" value="value" handle="round" step="1" range="true"></span>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.slider-input').attr('value')).toBe(tooltip);
  });

  it('uses range with min,max values if defValue is scalar or string', function() {
    var tooltip = '0,1000';
    var element;

    $rootScope.min = 0;
    $rootScope.max = 1000;
    $rootScope.defValue = '200';
    $rootScope.value = '';

    element = $compile(
      '<span slider ng-model="value" min="min" max="max" value="defValue" handle="round" step="1" range="true"></span>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.slider-input').attr('value')).toBe(tooltip);

    $rootScope.defValue = 200;
    element = $compile(
      '<span slider ng-model="value" min="min" max="max" value="defValue" handle="round" step="1" range="true"></span>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.slider-input').attr('value')).toBe(tooltip);

    $rootScope.defValue = 'aaa';
    element = $compile(
      '<span slider ng-model="value" min="min" max="max" value="defValue" handle="round" step="1" range="true"></span>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.slider-input').attr('value')).toBe(tooltip);
  });
});
