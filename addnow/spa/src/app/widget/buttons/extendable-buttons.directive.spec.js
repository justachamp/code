'use strict';

describe('Extendable Buttons', function() {
  beforeEach(module('angulardash.widget'));
  beforeEach(module('app/widget/buttons/extendable-buttons.html'));

  var $compile;
  var $rootScope;

  beforeEach(inject(function(_$compile_, _$rootScope_) {
    $compile = _$compile_;
    $rootScope = _$rootScope_;
    $rootScope.widget = {
      buttons: [
        {
          service: 'twitter',
          isExtraButton: false,
          text: 'Twitter',
          isShortLink: true
        },
        {
          service: 'facebook',
          isExtraButton: true,
          text: 'Facebook',
          isShortLink: true
        }
      ]
    };
  }));

  it('displays buttons', function() {
    var element = $compile(
      '<form><extendable-buttons ng-model="widget.buttons"></extendable-buttons></form>'
    )($rootScope);
    $rootScope.$digest();

    expect(element.find('.available-icons li').length).toBe(15);
    expect(element.find('.selected-icons li').length).toBe(2);
    expect(element.find('.selected-icons li')[0].innerHTML).toMatch('twitter');
    expect(element.find('.selected-icons li')[1].innerHTML).toEqual('');

    expect(element.find('.selected-plus li').length).toBe(2);
    expect(element.find('.selected-plus li')[0].innerHTML).toMatch('facebook');
    expect(element.find('.selected-plus li')[1].innerHTML).toEqual('');
  });
});
