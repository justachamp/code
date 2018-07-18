(function() {
  'use strict';

  function copyPasteWidgetForm(VanityDomainService) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/copy-paste-widget-form.html',
      link: function(scope, element, attributes, form) {
        scope.form = form;
        scope.widget.orientation = 'horizontal';
        scope.widget.buttonSize = 'medium';
        scope.widget.buttonStyle = 'icon';

        if (scope.trimKey) {
          VanityDomainService.getDomains(scope.trimKey).then(function(data) {
            scope.domains = data.data.vanityDomains;
          });
        }
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('copyPasteWidgetForm', ['VanityDomainService', copyPasteWidgetForm]);
})();
