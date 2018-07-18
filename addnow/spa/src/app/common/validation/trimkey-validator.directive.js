(function() {
  'use strict';

  function trimKeyValidator(VanityDomainService, $q) {
    return {
      require: 'ngModel',
      link: function(scope, element, attrs, ngModel) {
        ngModel.$asyncValidators.trimKey = function(modelValue, viewValue) {
          if (viewValue) {
            return VanityDomainService.getDomains(viewValue);
          }

          return $q.when(true);
        };
      }
    };
  }

  angular.module('angulardash.common').directive('trimKeyValidator', ['VanityDomainService', '$q', trimKeyValidator]);
})();
