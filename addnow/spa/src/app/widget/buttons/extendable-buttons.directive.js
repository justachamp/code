(function() {
  'use strict';

  function extendableButtons(Enums) {
    return {
      restrict: 'E',
      require: '^ngModel',
      scope: {
        ngModel: '=',
        availableButtons: '=?',
        maxMainItems: '@',
        minMainItems: '@'
      },
      templateUrl: 'app/widget/buttons/extendable-buttons.html',
      link: function(scope, element, attributes, ngModelController) {
        if (!scope.availableButtons) {
          scope.availableButtons = Enums.SERVICE_BUTTONS;
        }

        if (scope.minMainItems !== undefined) {
          scope.minMainItems = parseInt(scope.minMainItems);
        } else {
          scope.minMainItems = 0;
        }

        if (scope.maxMainItems !== undefined) {
          scope.maxMainItems = parseInt(scope.maxMainItems);
        } else {
          scope.maxMainItems = scope.availableButtons.length;
        }

        scope.extraButtons = [];
        scope.mainButtons = [];
        scope.sortableOptions = {
          connectWith: '.sortable-row',
          'ui-floating': true,
          update: function(event, ui) {
            // check that its an actual moving between the two lists
            var source = event.target.id;
            var target = ui.item.sortable.droptarget.attr('id');
            var totalSelected = scope.mainButtons.length;

            if (source !== 'selectedItems' && target === 'selectedItems' &&
              totalSelected >= scope.maxMainItems) {
              ui.item.sortable.cancel();
            }
          }
        };

        scope.showDropZone = function showDropZone() {
          return scope.mainButtons.length < scope.maxMainItems;
        };

        scope.nonSelectedButtons = scope.availableButtons.filter(function(button) {
          for (var i = 0; i < scope.ngModel.length; i++) {
            if (scope.ngModel[i].service === button.service) {
              return false;
            }
          }

          return true;
        });

        scope.$watchCollection('mainButtons', function(newVal, oldVal) {
          if (newVal !== oldVal) {
            ngModelController.$setViewValue({
              mainButtons: newVal, extraButtons: scope.extraButtons
            });
          }

          if (oldVal === undefined) {
            ngModelController.$setPristine();
          }
        });

        scope.$watchCollection('extraButtons', function(newVal, oldVal) {
          if (newVal !== oldVal) {
            ngModelController.$setViewValue({
              mainButtons: scope.mainButtons, extraButtons: newVal
            });
          }

          if (oldVal === undefined) {
            ngModelController.$setPristine();
          }
        });

        function filterButtons(value, isExtraButton) {
          return value.filter(function(item) {
            if (!item.isExtraButton) {
              return !isExtraButton;
            }

            return item.isExtraButton === isExtraButton;
          });
        }

        ngModelController.$formatters.push(function(modelValue) {
          return {
            mainButtons: filterButtons(modelValue, false),
            extraButtons: filterButtons(modelValue, true)
          };
        });

        ngModelController.$parsers.push(function(viewValue) {
          var main = viewValue.mainButtons;
          var extra = viewValue.extraButtons;
          var result;

          main.forEach(function(item) {
            item.isExtraButton = false;
          });

          extra.forEach(function(item) {
            item.isExtraButton = true;
          });

          result = main.concat(extra);
          return result;
        });

        ngModelController.$render = function() {
          if (!ngModelController.$viewValue) {
            ngModelController.$viewValue = {
              mainButtons: [],
              extraButtons: []
            };
          }

          scope.mainButtons = ngModelController.$viewValue.mainButtons;
          scope.extraButtons  = ngModelController.$viewValue.extraButtons;
        };
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('extendableButtons', ['Enums', extendableButtons]);
})();
