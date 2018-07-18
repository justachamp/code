(function() {
  'use strict';

  function newsletterWidgetForm(Enums, VanityDomainService) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        trimKey: '=',
        errors: '='
      },
      templateUrl: 'app/widget/newsletter-widget-form.html',
      controller: ['$scope', function controller($scope) {
        $scope.availableButtons = Enums.NEWSLETTER_SERVICE_BUTTONS;
      }],

      link: function link(scope, element, attributes, form) {
        scope.form = form;
        scope.widget.orientation = 'horizontal';
        scope.widget.buttonSize = 'medium';
        scope.widget.buttonStyle = 'icon';

        scope.checkForMediaUrlInWidget = function checkForMediaUrlInWidget() {
          var pinterestFilter = function(button) {
            return button.service === 'pinterest';
          };
          var hasPinterest = scope.widget.buttons && scope.widget.buttons.filter(pinterestFilter).length > 0;

          return scope.form.buttons.$valid && hasPinterest;
        };

        if (scope.trimKey) {
          VanityDomainService.getDomains(scope.trimKey).then(function(data) {
            scope.domains = data.data.vanityDomains;
          });
        }
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('newsletterWidgetForm', ['Enums', 'VanityDomainService', newsletterWidgetForm]);
})();
