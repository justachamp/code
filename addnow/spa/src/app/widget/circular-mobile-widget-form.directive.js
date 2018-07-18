'use strict';

function circularMobileWidgetForm(VanityDomainService) {
  return {
    restrict: 'AE',
    require: '^form',
    scope: {
      widget: '=',
      trimKey: '=',
      errors: '='
    },
    templateUrl: 'app/widget/circular-mobile-widget-form.html',
    controller: ['$scope', function($scope) {
      $scope.maxMainItems = 5;
      $scope.minMainItems = 3;
    }],

    link: function(scope, element, attributes, form) {
      scope.form = form;
      scope.widget.orientation = 'horizontal';
      scope.widget.buttonSize = 'medium';
      scope.widget.buttonStyle = 'icon';

      if (!scope.widget.minWidth) {
        scope.widget.minWidth = 1080;
      }

      if (!scope.widget.position) {
        scope.widget.position = 'bottom-left';
      }

      if (scope.trimKey) {
        VanityDomainService.getDomains(scope.trimKey).then(function(data) {
          scope.domains = data.data.vanityDomains;
        });
      }

      scope.$watchCollection('widget.buttons', function() {
        if (scope.form.buttons && scope.form.buttons.$dirty && scope.form.buttons.$error.serverError) {
          scope.form.buttons.$setValidity('serverError', true);
        }
      });
    }
  };
}

angular.module('angulardash')
  .directive('circularMobileWidgetForm', ['VanityDomainService', circularMobileWidgetForm]);
