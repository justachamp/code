(function() {
  'use strict';

  function socialInput() {
    return {
      restrict: 'AE',
      require: '^form',
      scope:{
        icon:'@',
        placeholder:'@',
        url:'='
      },
      templateUrl:'app/common/socialInput/socialInput.html',
      link: function(scope, iElement, iAttrs, form) {
        scope.form = form;
        iElement.click(function(event) {
          event.stopPropagation();
          iElement.find('input').focus();
        });

        iElement.find('input').bind('focus', function() {
          iElement.find('div').addClass('active');
        });

        iElement.find('input').bind('blur', function() {
          iElement.find('div').removeClass('active');
        });
      }
    };
  }

  angular.module('angulardash.common').directive('socialInput', socialInput);
})();
