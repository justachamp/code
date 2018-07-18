(function() {
  'use strict';

  function SiteCtrl($scope, $location, $routeParams, $modal, ErrorHandler, Enums, SiteService, MenuService,
                    WidgetService, AnalyticsService, AccountSettingsService, VanityDomainService) {
    var nestedInputs = {};
    var _this = this;

    this.getSite = function getSite(id) {
      AccountSettingsService.getSettings()
        .then(function(data) {
          $scope.hasAnalytics = data.data.hasAnalytics;
          return SiteService.getSiteById(id);
        })
        .then(function(data) {
          $scope.site = data.data;

          if ($scope.site.socialUrls) {
            $scope.site.socialUrls.forEach(function(socialUrl) {
              var matched = $scope.socialNetworks.filter(function(item) {
                return item.service === socialUrl.service;
              });

              if (matched.length > 0) {
                matched[0].url = socialUrl.url;
              }
            });
          }

          $scope.getVanityDomains();
          return WidgetService.getConfigurations($scope.site.id);
        })
        .then(function(data) {
          data.data.forEach(function(elem) {
            _this.addWidget(elem);
          });
        })
        .then(function() {
          if ($scope.hasAnalytics) {
            return AnalyticsService.getAccounts();
          }

          return null;
        })
        .then(function(data) {
          if (!data) {
            return;
          }

          var allAnalyticsAccounts = data.data;
          var propName;
          $scope.accounts = allAnalyticsAccounts.map(function(item) {
            return {id: item.id, name: item.name};
          });

          allAnalyticsAccounts.forEach(function(accountItem) {
            accountItem.properties.forEach(function(propItem) {
              if ($scope.site.analyticsProperty === propItem.id) {
                propName = propItem.name;
              }

              var items = propItem.profiles.map(function(viewItem) {
                var obj = {
                  id: viewItem.id,
                  name: viewItem.name,
                  propId: propItem.id,
                  propName: propItem.name,
                  accId: accountItem.id
                };
                if ($scope.site.analyticsProfile === obj.id &&
                  $scope.site.analyticsAccount === obj.accId &&
                  $scope.site.analyticsProperty === obj.propId) {
                  $scope.analyticsView.selected = obj;
                }

                return obj;
              });

              $scope.analyticsView.all = $scope.analyticsView.all.concat(items);
            });
          });
        });
    };

    this.addSite = function() {
      $scope.site.socialUrls = _this.prepareSocialUrls(nestedInputs);

      SiteService.addSite($scope.site)
        .success(function(data) {
          ErrorHandler.flushServerErrors($scope.form, $scope.errors);
          $scope.site.id = data.id;
          $location.path('/site/edit/' + $scope.site.id);
        })
        .error(function(data, status) {
          if (data.trimApiKey) {
            data.trimKey = data.trimApiKey;
          }

          $scope.errors = ErrorHandler.parseResponse(status, data, $scope.form, nestedInputs);
        });
    };

    this.updateSite = function() {
      $scope.site.socialUrls = _this.prepareSocialUrls(nestedInputs);

      SiteService.editSite($scope.site.id, $scope.site)
        .success(function() {
          ErrorHandler.flushServerErrors($scope.form, $scope.errors);
          $location.path('/site/dashboard/' + $scope.site.id);
        })
        .error(function(data, status) {
          if (data.trimApiKey) {
            data.trimKey = data.trimApiKey;
          }

          $scope.errors = ErrorHandler.parseResponse(status, data, $scope.form, nestedInputs);
        });
    };

    this.prepareSocialUrls = function(nestedInputs) {
      var socialUrls = [];
      nestedInputs.socialUrls = [];

      $scope.socialNetworks.forEach(function(socialNetwork) {
        if (socialNetwork.url) {
          socialUrls.push({
            service: socialNetwork.service,
            url: socialNetwork.url
          });
          nestedInputs.socialUrls.push({
            name: socialNetwork.service
          });
        }
      });

      if (socialUrls.length === 0) {
        delete nestedInputs.socialUrls;
      }

      return socialUrls;
    };

    this.addWidget = function(widget) {
      if (!$scope.selectedWidgets[widget.type]) {
        $scope.selectedWidgets[widget.type] = [];
      }

      $scope.selectedWidgets[widget.type].push(widget);
      $scope.allSelectedWidgets.push(widget);
    };

    this.replaceWidget = function(widgetArray, widgetToReplace) {
      var widgetIndex = widgetArray.map(function(item) {
        return item.id;
      }).indexOf(widgetToReplace.id);
      widgetArray[widgetIndex] = widgetToReplace;
    };

    $scope.getVanityDomains = function(reset) {
      if (reset) {
        $scope.site.vanityDomain = '';
        $scope.domains = null;
      }

      if ($scope.site.trimApiKey) {
        VanityDomainService.getDomains($scope.site.trimApiKey).then(function(data) {
          $scope.domains = data.data.vanityDomains;
        });
      }
    };

    $scope.vanityDomainFormatter = function vanityDomainFormatter(domain) {
      if (!domain || domain === '') {
        return 'Default';
      }

      return domain;
    };

    $scope.isSharingButtons = function isSharingButtons(widget) {
      return widget.type === Enums.SHARING_BUTTONS.value;
    };

    $scope.isOriginButtons = function isOriginButtons(widget) {
      return widget.type === Enums.ORIGIN_BUTTONS.value;
    };

    $scope.isNewsletter = function isNewsletter(widget) {
      return widget.type === Enums.NEWSLETTER.value;
    };

    $scope.isMobile = function isMobile(widget) {
      return widget.type === Enums.MOBILE.value;
    };

    $scope.isCircularMobile = function(widget) {
      return widget.type === Enums.CIRCULAR_MOBILE.value;
    };

    $scope.isCopyPaste = function(widget) {
      return widget.type === Enums.COPY_PASTE.value;
    };

    $scope.isFollow = function isFollow(widget) {
      return widget.type === Enums.FOLLOW_BUTTON.value;
    };

    $scope.isVerticalFloat = function isVerticalFloat(widget) {
      return widget.type === Enums.VERTICAL_FLOAT.value;
    };

    $scope.openWidget = function openWidget(widget, widgetType) {
      var modalInstance = $modal.open({
        animation: true,
        templateUrl: 'app/widget/addedit-widget.html',
        controller: 'AddEditWidgetCtrl',
        resolve: {
          widgetConfig: function() {
            if (!widget) {
              widget = {
                type: widgetType,
                isActive: true,
                buttons: []
              };
            }

            return widget;
          },

          siteId: function() {
            return $scope.site.id;
          },

          hashId: function() {
            return $scope.site.hashId;
          },

          trimKey: function() {
            return $scope.site.trimApiKey;
          },

          socialNetworks: function() {
            return $scope.socialNetworks;
          }
        }
      });

      modalInstance.result.then(function(result) {
        var widget = result.widgetConfig;
        if (result.edit) {
          _this.replaceWidget($scope.selectedWidgets[widget.type], widget);
          _this.replaceWidget($scope.allSelectedWidgets, widget);
        } else {
          _this.addWidget(widget);
        }
      });
    };

    $scope.submitAddPage = function submitAddPage() {
      ErrorHandler.flushServerErrors($scope.form, $scope.errors);
      if ($scope.form.$valid) {
        if ($scope.analyticsView.selected) {
          $scope.site.analyticsAccount = $scope.analyticsView.selected.accId;
          $scope.site.analyticsProperty = $scope.analyticsView.selected.propId;
          $scope.site.analyticsProfile = $scope.analyticsView.selected.id;
        }

        if ($scope.edit) {
          _this.updateSite();
        } else {
          _this.addSite();
        }

        MenuService.markMenuItemsForUpdate();
      }
    };

    $scope.updateWidgetState = function updateWidgetState(widget, isActive) {
      widget.isActive = isActive;
      WidgetService.editConfiguration($scope.site.id, widget.id, widget);
    };

    $scope.isCreateButtonExists = function isCreateButtonExists(widgetType) {
      if (widgetType in $scope.selectedWidgets) {
        var maxWidgets = $scope.widgetTypes.filter(function(el) {
          return el.value === widgetType;
        })[0].maxWidgets;
        return maxWidgets === 0 || $scope.selectedWidgets[widgetType].length < maxWidgets;
      }

      return true;
    };

    $scope.openThankYouPopup = function() {
      var modalInstance = $modal.open({
        animation: true,
        templateUrl: 'app/site/thank-you-popup.html',
        controller: 'ThankYouPopupCtrl',
        size: 'lg',
        resolve: {
          thankYouData: function() {
            return {
              message: $scope.site.thankYouMessage,
              advertImageUrl: $scope.site.thankYouAdvertImageUrl,
              advertUrl: $scope.site.thankYouAdvertUrl,
              advertTitle: $scope.site.thankYouAdvertTitle,
              socialNetworks: $scope.socialNetworks
            };
          },

          siteId: function() {
            return $scope.site.id;
          }
        }
      });
      var oldSocialNetworkUrls = angular.copy($scope.socialNetworks);

      modalInstance.result.then(function(result) {
        $scope.site.thankYouMessage = result.message;
        $scope.site.thankYouAdvertImageUrl = result.advertImageUrl;
        $scope.site.thankYouAdvertUrl = result.advertUrl;
        $scope.site.thankYouAdvertTitle = result.advertTitle;
        $scope.socialNetworks = result.socialNetworks;
      }, function() {
        // Restore social network urls when dismissing popup
        $scope.socialNetworks = oldSocialNetworkUrls;
      });
    };

    $scope.widgetTypes = angular.copy(Enums.WIDGET_TYPES);
    $scope.site = {};
    $scope.errors = {};
    $scope.site.id = '';
    $scope.site.domain = $location.search().website || '';
    $scope.site.thankYouMessage = '';
    $scope.site.thankYouAdvertImageUrl = '';
    $scope.site.thankYouAdvertUrl = '';
    $scope.site.thankYouAdvertTitle = '';
    $scope.site.analyticsAccount = '';
    $scope.site.analyticsProperty = '';
    $scope.site.analyticsProfile = '';

    //as we use ngIf we need wrap selected choice into object. ngIf copies parent scope
    $scope.analyticsView = {
      selected: null,
      all: []
    };
    $scope.site.addressBarSharing = true;
    $scope.site.copyPasteSharing = true;
    $scope.edit = false;
    $scope.socialNetworks = angular.copy(Enums.FOLLOW_BUTTONS);
    $scope.selectedWidgets = {};
    $scope.allSelectedWidgets = [];

    if ($routeParams.siteId) {
      this.getSite($routeParams.siteId);
      $scope.edit = true;
    }
  }

  angular.module('angulardash.site')
    .controller('SiteCtrl', [
      '$scope', '$location', '$routeParams', '$modal', 'ErrorHandler', 'Enums', 'SiteService', 'MenuService',
      'WidgetService', 'AnalyticsService', 'AccountSettingsService', 'VanityDomainService', SiteCtrl]);
})();
