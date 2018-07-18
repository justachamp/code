(function() {
  'use strict';

  function configureClipProvider(ngClipProvider) {
    ngClipProvider.setPath('/assets/images/ZeroClipboard.swf');
    ngClipProvider.setConfig({
      cacheBust: false,
      hoverClass: 'g4-button-hover'
    });
  }

  angular.module('angulardash.widget', ['angulardash.common', 'ui.bootstrap', 'ui.sortable', 'sprintf', 'ngClipboard'])
    .config(['ngClipProvider', configureClipProvider]);
})();
