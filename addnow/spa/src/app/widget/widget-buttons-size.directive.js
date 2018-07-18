(function() {
  'use strict';

  function widgetButtonsSize(Enums) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        buttonSize: '='
      },
      templateUrl: 'app/widget/widget-buttons-size.html',
      link: function(scope) {
        scope.buttonSizes = Enums.BUTTON_SIZES;
        scope.buttonSizeIndex = scope.buttonSizes.indexOf(scope.buttonSize);
        //to prevent partially initializing of slider
        scope.sliderReady = true;

        scope.buttonSizeDelegate = function buttonSizeDelegate(value) {
          scope.buttonSize = scope.buttonSizes[value];
        };
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('widgetButtonsSize', ['Enums', widgetButtonsSize]);
})();
