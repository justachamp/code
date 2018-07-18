(function() {
  'use strict';

  function filterDecodeURI() {
    return function(url) {
      try {
        return decodeURI(url);
      }
      catch (e) {
        return url;
      }
    };
  }

  angular.module('angulardash.common').filter('decodeURI', filterDecodeURI);
})();
