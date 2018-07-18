(function() {
  'use strict';

  function notEmptyArray() {
    return {
      require: 'ngModel',
      link: function(scope, element, attrs, ngModel) {
        ngModel.$validators.notEmptyArray = function(modelValue) {
          if (modelValue) {
            return (angular.isArray(modelValue) &&  modelValue.length > 0);
          }

          return true;
        };
      }
    };
  }

  angular.module('angulardash.common').directive('notEmptyArray', notEmptyArray);
})();
