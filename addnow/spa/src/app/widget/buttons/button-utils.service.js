(function() {
  'use strict';

  function ButtonUtils() {
    this.mapButtonWithSiteUrl = function(buttons, socialUrls) {
      var matched;
      var result;
      result = buttons.map(function(button) {
        matched = socialUrls.filter(function(item) {
          return button.service === item.service;
        });

        if (matched.length > 0) {
          button.followUrl = matched[0].url;
          return matched[0];
        }
      });

      return result.filter(function(elem) {
        return elem !== null;
      });
    };

    this.mapButtonWithSocial = function(buttons, socials) {
      var matched;
      var result;
      result = buttons.map(function(button) {
        matched = socials.filter(function(item) {
          return button.service === item.service;
        });

        if (matched.length > 0) {
          button.service = matched[0].service;
          button.placeholder = matched[0].placeholder;
          return matched[0];
        }
      });

      return result.filter(function(elem) {
        return elem !== null;
      });
    };

    this.getMainButtons = function(buttons) {
      return buttons.filter(function(element) {
        return !element.isExtraButton;
      });
    };

    this.getExtraButtons = function(buttons) {
      return buttons.filter(function(element) {
        return element.isExtraButton;
      });
    };
  }

  angular.module('angulardash.widget').service('ButtonUtils', ButtonUtils);
})();
