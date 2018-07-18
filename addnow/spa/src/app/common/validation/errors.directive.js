(function() {
  'use strict';

  function errors() {
    return {
      restrict: 'E',
      scope: {
        data: '='
      },
      templateUrl: 'app/common/validation/errors.html',
      link: function() {
      }
    };
  }

  angular.module('angulardash.common').directive('errors', errors);
})();
