(function() {
  'use strict';

  function followButtonsWidgetForm(ButtonUtils) {
    return {
      restrict: 'AE',
      require: '^form',
      scope: {
        widget: '=',
        socials: '=',
        errors: '='
      },

      templateUrl: 'app/widget/follow-buttons-widget-form.html',
      controller: ['$scope', function($scope) {
        var urlExists = function(url) {
          return url !== undefined && url.length > 0;
        };

        $scope.buttons = $scope.widget.buttons.map(function(button) {
          return {
            service: button.service,
            isExtraButton: false,
            text: button.text,
            followUrl: button.followUrl
          };
        });


        if (!$scope.widget.id) {
          ButtonUtils.mapButtonWithSiteUrl($scope.buttons, $scope.socials);
        }

        ButtonUtils.mapButtonWithSocial($scope.buttons, $scope.socials);

        $scope.buttons.sort(function(a, b) {
          if (urlExists(a.followUrl) && urlExists(b.followUrl)) {
            return 0;
          }

          if (!urlExists(a.followUrl) && !urlExists(b.followUrl)) {
            return 0;
          }

          if (!urlExists(a.followUrl) && urlExists(b.followUrl)) {
            return 1;
          }

          if (urlExists(a.followUrl) && !urlExists(b.followUrl)) {
            return -1;
          }
        });

        $scope.$watch('buttons', function(changedButtons) {
          $scope.buttonsWithUrl = [];
          $scope.buttonsWithoutUrl = [];
          changedButtons.forEach(function(item) {
            if (item.followUrl !== undefined && item.followUrl.length > 0) {
              $scope.buttonsWithUrl.push(item);
            } else {
              $scope.buttonsWithoutUrl.push(item);
            }
          });
          $scope.widget.buttons = changedButtons;
        }, true);
      }],

      link: function(scope, element, attributes, form) {
        scope.form = form;
      }
    };
  }

  angular.module('angulardash.widget')
    .directive('followButtonsWidgetForm', ['ButtonUtils', followButtonsWidgetForm]);
})();
