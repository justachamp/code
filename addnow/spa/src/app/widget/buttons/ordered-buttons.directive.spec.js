'use strict';

describe('Ordered Buttons', function() {
  beforeEach(module('angulardash.widget'));
  beforeEach(module('app/widget/buttons/ordered-buttons.html'));

  var $compile;
  var $rootScope;

  beforeEach(inject(function(_$compile_, _$rootScope_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;
    $rootScope.widget = {buttons: []};
    $rootScope.buttons = [
      {
        service: 'facebook',
        text: 'Facebook',
        followUrl: 'Facebook follow url'
      },
      {
        service: 'instagram',
        text: 'Instagram',
        followUrl: 'Instagram follow url'
      },
      {
        service: 'twitter',
        text: 'Twitter'
      }
    ];
  }));

  it('displays buttons', function() {
    var element = $compile('<form><ordered-buttons ng-model="buttons"></ordered-buttons></form>')($rootScope);
    $rootScope.$digest();

    expect(element.find('.selected-icons li').length).toBe(3);
    expect(element.find('.selected-icons li')[0].innerHTML).toContain('facebook');
    expect(element.find('.selected-icons li')[1].innerHTML).toContain('instagram');
    expect(element.find('.selected-icons li')[2].innerHTML).toContain('twitter');
  });
});
