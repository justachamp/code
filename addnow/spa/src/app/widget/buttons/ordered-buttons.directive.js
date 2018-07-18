(function() {
  'use strict';

  function orderedButtons() {
    return {
      restrict: 'E',
      require: '^ngModel',
      templateUrl: 'app/widget/buttons/ordered-buttons.html',
      scope: {},
      link: function(scope, element, attributes, ngModelController) {
        ngModelController.$formatters.push(function(modelValue) {
          return modelValue;
        });

        ngModelController.$parsers.push(function(viewValue) {
          return viewValue;
        });

        ngModelController.$render = function() {
          scope.buttons  = ngModelController.$viewValue;
        };

        scope.$watchCollection('buttons', function(newVal, oldVal) {
          if (newVal !== oldVal) {
            ngModelController.$setViewValue(angular.copy(newVal));
          }

          if (oldVal === undefined) {
            ngModelController.setPristine();
          }
        });

        scope.sortableOptions = {
          connectWith: '.sortable-row',
          'ui-floating': true
        };
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('orderedButtons', orderedButtons);
})();
