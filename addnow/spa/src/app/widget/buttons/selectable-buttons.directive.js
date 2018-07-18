(function() {
  'use strict';

  function selectableButtons() {
    return {
      restrict: 'E',
      require: '^ngModel',
      scope: {
        ngModel: '=',
        availableButtons: '='
      },
      templateUrl: 'app/widget/buttons/selectable-buttons.html',
      link: function(scope, element, attributes, ngModelController) {
        scope.sortableOptions = {
          connectWith: '.sortable-row',
          'ui-floating': true
        };

        ngModelController.$formatters.push(function(modelValue) {
          return modelValue;
        });

        ngModelController.$parsers.push(function(viewValue) {
          return viewValue;
        });

        ngModelController.$render = function() {
          scope.buttons = ngModelController.$viewValue;
        };

        scope.$watchCollection('buttons', function(newVal, oldVal) {
          if (newVal !== oldVal) {
            ngModelController.$setViewValue(angular.copy(newVal));
          }

          if (oldVal === undefined) {
            ngModelController.setPristine();
          }
        });

        scope.nonSelectedButtons = scope.availableButtons.filter(function(button) {
          for (var i = 0; i < scope.ngModel.length; i++) {
            if (scope.ngModel[i].service === button.service) {
              return false;
            }
          }

          return true;
        });
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('selectableButtons', selectableButtons);
})();
