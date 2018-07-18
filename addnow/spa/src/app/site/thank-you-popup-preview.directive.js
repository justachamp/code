(function() {
  'use strict';

  function popupPreview($sce, CdnSettings) {
    return {
      restrict: 'E',
      scope: {},
      template: '',
      link: function(scope, element) {
        var code;
        var lines = [];

        //jscs:disable maximumLineLength
        lines.push('var _preview = _preview || {};');
        lines.push('_preview.cdnHost = \'');
        lines.push(CdnSettings.host);
        lines.push('\';(function() {');
        lines.push('var preview = document.createElement(\'script\'); preview.type = \'text/javascript\';');
        lines.push(' preview.async = true;preview.src = (document.location.protocol === \'https:\' ?');
        lines.push('\'https://\' : \'http://\') + \'');
        lines.push(CdnSettings.host);
        lines.push('/widget/preview.js\';');
        lines.push('var s = document.getElementsByTagName(\'script\')[0];');
        lines.push('s.parentNode.insertBefore(preview, s);})();');

        //jscs:enable maximumLineLength

        code = $sce.trustAsJs(lines.join(''));
        angular.element('<script id="script-preview"/>').text(code).appendTo(element);
      }
    };
  }

  angular.module('angulardash.site')
    .directive('popupPreview', ['$sce', 'CdnSettings', popupPreview]);
})();
