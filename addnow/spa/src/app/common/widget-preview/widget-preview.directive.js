(function() {
  'use strict';

  function widgetPreview($sce, $interval, CdnSettings) {
    return {
      restrict: 'E',
      scope: {
        widget: '='
      },
      template: '<script id="script-preview" type=\'text/javascript\'/><div class=\'addnow\' data-preview/>',
      link: function(scope, element) {
        var newConfig = angular.copy(scope.widget);
        var dirty = false;
        var interval;

        function onButtonsChanged(value) {
          newConfig.buttons = value;
          dirty = true;
        }

        function onWidgetChanged(value) {
          var needRender = (!angular.equals(newConfig.orientation, value.orientation)) ||
            (!angular.equals(newConfig.buttonSize, value.buttonSize)) ||
            (!angular.equals(newConfig.buttonStyle, value.buttonStyle)) ||
            (!angular.equals(newConfig.hasLinkShareButton, value.hasLinkShareButton)) ||
            (!angular.equals(newConfig.position, value.position)) ||
            (!angular.equals(newConfig.counterPosition, value.counterPosition));
          newConfig.orientation = value.orientation;
          newConfig.buttonSize = value.buttonSize;
          newConfig.buttonStyle = value.buttonStyle;
          newConfig.counterPosition = value.counterPosition;
          newConfig.hasLinkShareButton = value.hasLinkShareButton;
          newConfig.position = value.position;
          if (!dirty) {
            dirty = needRender;
          }
        }

        scope.$watchCollection('widget.buttons', onButtonsChanged, true);
        scope.$watch('widget', onWidgetChanged, true);

        scope.$on('$destroy', function() {
          $interval.cancel(interval);
        });

        function render() {
          if (dirty) {
            var code;
            var cdnHost;
            var scriptContent;
            var lines = [];
            if (!newConfig.buttons || (newConfig.buttons.length === 0)) {
              element.find('#script-preview').remove();
              element.find('.addnow').empty();
              angular.element('<script id="script-preview"/>').appendTo(element);
              dirty = false;
              return;
            }

            cdnHost = CdnSettings.host;

            //jscs:disable maximumLineLength
            lines.push('var _preview = _preview || {};');
            lines.push('if(!_preview.config) {');
            lines.push('_preview.config = {};}_preview.config = ');
            lines.push(angular.toJson(newConfig));
            lines.push(';_preview.cdnHost = \'');
            lines.push(cdnHost);
            lines.push('\';(function() {');
            lines.push('var preview = document.createElement(\'script\'); preview.type = \'text/javascript\';');
            lines.push(' preview.async = true;preview.src = (document.location.protocol === \'https:\' ?');
            lines.push('\'https://\' : \'http://\') + \'');
            lines.push(cdnHost);
            lines.push('/widget/preview.js\';');
            lines.push('var s = document.getElementsByTagName(\'script\')[0];');
            lines.push('s.parentNode.insertBefore(preview, s);})();');

            //jscs:enable maximumLineLength

            scriptContent = lines.join('');
            code = $sce.trustAsJs(scriptContent);
            element.find('#script-preview').remove();
            element.find('.addnow').empty().attr('class', 'addnow');
            angular.element('<script id="script-preview"/>').text(code).appendTo(element);
            dirty = false;
          }
        }

        interval = $interval(render, 500);
      }
    };
  }

  angular.module('angulardash.common')
    .directive('widgetPreview', ['$sce', '$interval', 'CdnSettings', widgetPreview]);
})();
