'use strict';

describe('Widget Preview', function() {
  beforeEach(module('angulardash.common'));

  var $compile;
  var $rootScope;
  var $interval;

  beforeEach(inject(function(_$compile_, _$rootScope_, _$interval_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;
    $interval = _$interval_;
    $rootScope.widget = {};
  }));

  it('doesn\'t show widget without required fields', function() {
    var element = $compile(
      '<widget-preview widget="widget"></widget-preview>'
    )($rootScope);
    $rootScope.$digest();
    expect(element.find('.addnow').text()).toBe('');
  });

  it('doesn\'t show widget with empty buttons', function() {
    var element = $compile(
      '<widget-preview widget="widget"></widget-preview>'
    )($rootScope);
    $rootScope.widget = {
      orientation: 'a',
      buttonSize: 'a',
      buttonStyle: 'a',
      counterPosition: 'a',
      buttons: []
    };
    $rootScope.$digest();
    $interval.flush(1000);
    expect(element.find('#script-preview').text()).toBe('');
  });
});
