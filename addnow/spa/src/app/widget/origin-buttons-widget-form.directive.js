(function() {
  'use strict';

  function originButtonsWidgetForm(VanityDomainService, Enums) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/origin-buttons-widget-form.html',
      controller: ['$scope', function($scope) {
        $scope.availableButtons = Enums.ORIGIN_SERVICE_BUTTONS;
      }],

      link: function(scope, element, attributes, form) {
        scope.form = form;

        if (!scope.widget.orientation) {
          scope.widget.orientation = 'horizontal';
        }

        if (scope.trimKey) {
          VanityDomainService.getDomains(scope.trimKey).then(function(data) {
            scope.domains = data.data.vanityDomains;
          }, function() {
          });
        }
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('originButtonsWidgetForm', ['VanityDomainService', 'Enums', originButtonsWidgetForm]);
})();
