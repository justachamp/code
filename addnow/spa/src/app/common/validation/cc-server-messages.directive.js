(function() {
  'use strict';

  function ccServerMessages() {
    return {
      restrict: 'A',
      scope: {
        ngMessages: '='
      },
      transclude: true,
      templateUrl: 'app/common/validation/cc-server-messages.html',
      link: function() {
      }
    };
  }

  angular.module('angulardash.common').directive('ccServerMessages', ccServerMessages);
})();
