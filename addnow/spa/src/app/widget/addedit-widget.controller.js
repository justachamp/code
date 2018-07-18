(function() {
  'use strict';

  function AddEditWidgetCtrl($scope, $modalInstance, widgetConfig, siteId, trimKey,
                             WidgetService, ErrorHandler, Enums, $filter, hashId,
                             AppSettings, CdnSettings, socialNetworks) {
    var _this = this;
    var parser;

    //extract host from backendApi string
    parser = document.createElement('a');
    parser.href = AppSettings.backendApi;

    this.generateTrackingCode = function(hashId) {
      return '<script type="text/javascript">\n' +
        '   var _addnow = _addnow || [];\n' +
        '   _addnow.push(["set", "hash_id", "' + hashId + '"]);\n' +
        '   (function() {' +
        'var addnow = document.createElement("script"); ' +
        'addnow.type = "text/javascript"; ' +
        'addnow.async = true; ' +
        'addnow.src = ("https:" === document.location.protocol ? "https://" : "http://") + ' +
        '"' + CdnSettings.host + '/widget/addnow.js"; ' +
        'var s = document.getElementsByTagName("script")[0]; ' +
        's.parentNode.insertBefore(addnow, s);' +
        '})();\n' +
        '</script>';
    };

    this.mergeButtons = function(buttons, defaultButtons) {
      var existentButtons = angular.copy(buttons);
      defaultButtons.forEach(function(defaultButton) {
        var existButton = buttons.filter(function(button) {
          return defaultButton.service === button.service;
        });

        if (existButton.length === 0) {
          existentButtons.push(defaultButton);
        }
      });

      return existentButtons;
    };

    this.getSharingLinks = function(hashId) {
      var schemeRegex = /^https?:\/\//i;
      var data = [];
      var url;
      var mediaUrl;
      var vanityDomain;

      //icon sizes: 22x22, 33x33, 38x38, 45x45, 48x48
      url = $scope.widgetConfig.pageUrl;
      if (!schemeRegex.test(url)) {
        url = 'http://' + url;
      }

      mediaUrl = $scope.widgetConfig.mediaUrl;
      if (mediaUrl) {
        if (!schemeRegex.test(mediaUrl)) {
          mediaUrl = 'http://' + mediaUrl;
        }
      }

      vanityDomain = $scope.widgetConfig.vanityDomain;

      // skip 'instagram' as we have no proper icon for it
      if ($scope.widgetConfig.buttons) {
        data = $scope.widgetConfig.buttons.map(function(element) {
          return _this.getSharingLink(element.service, hashId,
            $scope.widgetConfig.pageTitle, url, 'medium-icons', mediaUrl, vanityDomain);
        });
      }

      return data.join('\n');
    };

    this.getSharingLink = function(socialNetwork, hashId, message, url, iconSize, mediaUrl, vanityDomain) {
      var fmt = $filter('fmt');
      var hrefTemplate;
      var extraParamsTemplate;
      var href;
      var icon;

      icon = fmt('http://' + CdnSettings.host + '/widget/images/icons/%s/%s.png', iconSize,
        _this.convertToSlug(socialNetwork));

      hrefTemplate = 'http://' + parser.host + '/tracker/share/%s?url=%s&site_id=%s&message=%s';
      href = fmt(hrefTemplate, socialNetwork, encodeURIComponent(url), encodeURIComponent(hashId),
        encodeURIComponent(message));

      if (mediaUrl) {
        extraParamsTemplate = '&media_url=%s';
        href += fmt(extraParamsTemplate, encodeURIComponent(mediaUrl));
      }

      if (vanityDomain) {
        extraParamsTemplate = '&vanity_domain=%s';
        href += fmt(extraParamsTemplate, encodeURIComponent(vanityDomain));
      }

      return fmt('<a href="%s" target="_blank"><img src="%s" border="0" alt="%s"/></a>',
        href, icon, socialNetwork);
    };

    this.convertToSlug = function(text) {
      return text
        .replace(/([a-z])([A-Z])/g, '$1 $2').toLowerCase()
        .replace(/[^\w ]+/g, '')
        .replace(/ +/g, '-');
    };

    $scope.isEdit = function() {
      return !!$scope.widgetConfig.id;
    };

    $scope.widgetCode = function(code) {
      angular.element(code).removeClass('clipboard-copy-effect');
      if ($scope.isEdit()) {
        return '<div class=\'addnow\' data-id=\'' + $scope.widgetConfig.id + '\'></div>';
      }

      return '';
    };

    $scope.trackingCode = function(code) {
      angular.element(code).removeClass('clipboard-copy-effect');
      if ($scope.isEdit()) {
        if ($scope.isNewsletterWidget()) {
          return _this.getSharingLinks(hashId);
        }

        return _this.generateTrackingCode(hashId);
      }

      return '';
    };

    $scope.codeCopied = function(code) {
      angular.element(code).addClass('clipboard-copy-effect');
    };

    $scope.isFollowWidget = function() {
      return $scope.widgetConfig.type === Enums.FOLLOW_BUTTON.value;
    };

    $scope.isVerticalFloatWidget = function() {
      return $scope.widgetConfig.type === Enums.VERTICAL_FLOAT.value;
    };

    $scope.isSharingButtonsWidget = function() {
      return $scope.widgetConfig.type === Enums.SHARING_BUTTONS.value;
    };

    $scope.isCopyPasteWidget = function() {
      return $scope.widgetConfig.type === Enums.COPY_PASTE.value;
    };

    $scope.isNewsletterWidget = function() {
      return $scope.widgetConfig.type === Enums.NEWSLETTER.value;
    };

    $scope.isMobileWidget = function() {
      return $scope.widgetConfig.type === Enums.MOBILE.value;
    };

    $scope.isOriginButtonsWidget = function() {
      return $scope.widgetConfig.type === Enums.ORIGIN_BUTTONS.value;
    };

    $scope.isCircularMobileWidget = function() {
      return $scope.widgetConfig.type === Enums.CIRCULAR_MOBILE.value;
    };

    $scope.widgetTitle = function() {
      if ($scope.isMobileWidget()) {
        return 'Mobile Widget';
      }

      if ($scope.isCircularMobileWidget()) {
        return 'Circular Mobile Widget';
      }

      if ($scope.isNewsletterWidget()) {
        return 'Newsletter widget';
      }

      if ($scope.isCopyPasteWidget()) {
        return 'Copy-Paste Widget';
      }

      if ($scope.isSharingButtonsWidget()) {
        return 'Sharing Buttons Widget';
      }

      if ($scope.isFollowWidget()) {
        return 'Follow Widget';
      }

      if ($scope.isVerticalFloatWidget()) {
        return 'Vertical Float Widget';
      }

      if ($scope.isOriginButtonsWidget()) {
        return 'Original Buttons Widget';
      }

      return 'Configuration Widget';
    };

    $scope.cancel = function() {
      $modalInstance.dismiss('cancel');
    };

    $scope.submitAddPage = function() {
      ErrorHandler.flushServerErrors($scope.form, $scope.errors);

      if ($scope.form.$invalid) {
        return;
      }

      if ($scope.isEdit()) {
        WidgetService.editConfiguration(siteId,
          $scope.widgetConfig.id, $scope.widgetConfig).then(
          function() {
            $modalInstance.close({widgetConfig: $scope.widgetConfig, edit: true});
          },

          function(data) {
            $scope.errors = ErrorHandler.parseResponse(data.status, data.data, $scope.form, null);
          }

        );
      } else {
        WidgetService.addConfiguration(siteId,
          $scope.widgetConfig).then(
          function(data) {
            $scope.widgetConfig.id = data.data.id;
            $modalInstance.close({widgetConfig: $scope.widgetConfig, edit: false});
          }

        ).catch(
          function(data) {
            $scope.errors = ErrorHandler.parseResponse(data.status, data.data, $scope.form, null);
          }

        );
      }
    };

    $scope.errors = {};
    $scope.widgetConfig = angular.copy(widgetConfig);

    if (!widgetConfig.id) {
      $scope.widgetConfig.buttons = [];
      $scope.widgetConfig.isActive = true;
      if ($scope.isFollowWidget()) {
        $scope.widgetConfig.orientation = 'horizontal';
        $scope.widgetConfig.buttons = angular.copy(Enums.FOLLOW_BUTTONS);
      } else if ($scope.isVerticalFloatWidget()) {
        $scope.widgetConfig.buttons = angular.copy(Enums.VERTICAL_FLOAT_BUTTONS);
      }
    } else {
      if ($scope.isFollowWidget()) {
        $scope.widgetConfig.buttons = this.mergeButtons($scope.widgetConfig.buttons, Enums.FOLLOW_BUTTONS);
      }
    }

    $scope.socialNetworks = socialNetworks;
    $scope.trimKey = trimKey;
  }

  angular.module('angulardash.widget')
    .constant('moment', moment)
    .controller('AddEditWidgetCtrl', ['$scope', '$modalInstance', 'widgetConfig', 'siteId', 'trimKey',
      'WidgetService', 'ErrorHandler', 'Enums', '$filter', 'hashId', 'AppSettings',
      'CdnSettings', 'socialNetworks', AddEditWidgetCtrl]);
})();
