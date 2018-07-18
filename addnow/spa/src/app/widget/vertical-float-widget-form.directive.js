(function() {
  'use strict';

  function verticalFloatWidgetForm(VanityDomainService) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/vertical-float-widget-form.html',
      link: function(scope, element, attributes, form) {
        scope.form = form;
        scope.widget.buttonSize = 'big';

        if (!scope.widget.position) {
          scope.widget.position = 'left';
        }

        if (!scope.widget.buttonStyle) {
          scope.widget.buttonStyle = 'counter';
        }

        if (!scope.widget.buttonStyle) {
          scope.widget.buttonStyle = 'label';
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
    .directive('verticalFloatWidgetForm', ['VanityDomainService', verticalFloatWidgetForm]);
})();
