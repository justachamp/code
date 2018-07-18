(function() {
  'use strict';
  angular.module('angulardash.common')
    .directive('passwordMatch', [function() {
      return {
        restrict: 'A',
        scope: true,
        require: 'ngModel',
        link: function(scope, elem, attrs, control) {
          var checker = function() {
            return scope.$eval(attrs.ngModel) === scope.$eval(attrs.passwordMatch);
          };

          scope.$watch(checker, function(n) {
            //set the form control to valid if both
            //passwords are the same, else invalid
            control.$setValidity('unique', n);
          });
        }
      };
    }]);
})();
