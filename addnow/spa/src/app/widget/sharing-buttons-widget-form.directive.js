(function() {
  'use strict';

  function sharingButtonsWidgetForm(VanityDomainService) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/sharing-buttons-widget-form.html',
      controller: ['$scope', function($scope) {
        if (!$scope.widget.id) {
          $scope.widget.buttonSize = 'medium';
          $scope.widget.orientation = 'horizontal';
          $scope.widget.buttonStyle = 'icon';
        }
      }],

      link: function(scope, element, attributes, form) {
        scope.form = form;

        scope.showTypeOptions = function showTypeOptions() {
          return scope.widget.buttonSize === 'big' || scope.widget.buttonSize === 'large';
        };

        if (scope.trimKey) {
          VanityDomainService.getDomains(scope.trimKey).then(function(data) {
            scope.domains = data.data.vanityDomains;
          }, function() {
          });
        }

        scope.$watchGroup(['widget.buttonSize', 'widget.buttonStyle'], function(newValues, oldValues) {
          if (newValues[0] !== oldValues[0]) {
            if (newValues[0] === 'small' || newValues[0] === 'medium') {
              scope.widget.buttonStyle = 'icon';
              delete scope.widget.counterPosition;
            }
          }

          if (newValues[1] !== oldValues[1]) {
            if (newValues[1] === 'counter') {
              scope.widget.counterPosition = 'top';
            } else {
              delete scope.widget.counterPosition;
            }
          }
        });
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('sharingButtonsWidgetForm', ['VanityDomainService', sharingButtonsWidgetForm]);
})();
