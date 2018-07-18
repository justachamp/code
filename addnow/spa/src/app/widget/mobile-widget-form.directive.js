(function() {
  'use strict';

  function mobileWidgetForm(VanityDomainService) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/mobile-widget-form.html',
      link: function(scope, element, attributes, form) {
        scope.form = form;
        scope.widget.orientation = 'horizontal';
        scope.widget.buttonSize = 'medium';
        scope.widget.buttonStyle = 'icon';

        if (!scope.widget.minWidth) {
          scope.widget.minWidth = 1080;
        }

        if (!scope.widget.position) {
          scope.widget.position = 'bottom';
        }

        if (scope.trimKey) {
          VanityDomainService.getDomains(scope.trimKey).then(function(data) {
            scope.domains = data.data.vanityDomains;
          });
        }
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('mobileWidgetForm', ['VanityDomainService', mobileWidgetForm]);
})();
