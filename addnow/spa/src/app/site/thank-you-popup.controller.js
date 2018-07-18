(function() {
  'use strict';

  function ThankYouPopupCtrl($scope, $modalInstance, SiteService, ErrorHandler, thankYouData, siteId) {
    $scope.thankYouData = thankYouData;
    $scope.siteId = siteId;
    $scope.errors = {};

    $scope.submit = function() {
      var site = {};
      var nestedInputs = {};

      ErrorHandler.flushServerErrors($scope.form, $scope.errors);
      nestedInputs.socialUrls = [];

      if ($scope.form.$invalid) {
        return;
      }

      site.socialUrls = [];
      site.thankYouMessage = $scope.thankYouData.message;
      site.thankYouAdvertImageUrl = $scope.thankYouData.advertImageUrl;
      site.thankYouAdvertUrl = $scope.thankYouData.advertUrl;
      site.thankYouAdvertTitle = $scope.thankYouData.advertTitle;

      $scope.thankYouData.socialNetworks.forEach(function(socialNetwork) {
        if (socialNetwork.url) {
          site.socialUrls.push({service: socialNetwork.service, url: socialNetwork.url});
          nestedInputs.socialUrls.push({name: socialNetwork.service});
        }
      });

      if (site.socialUrls.length === 0) {
        delete nestedInputs.socialUrls;
      }

      SiteService.patchSite($scope.siteId, site)
        .success(function() {
          ErrorHandler.flushServerErrors($scope.form, $scope.errors);
          $modalInstance.close($scope.thankYouData);
        })
        .error(function(data, status) {
          $scope.errors = ErrorHandler.parseResponse(status, data, $scope.form, nestedInputs);
        });
    };

    $scope.cancel = function() {
      $modalInstance.dismiss('cancel clicked');
    };

    $scope.hasUrl = function(item) {
      return !!item.url;
    };
  }

  angular.module('angulardash.site')
    .controller('ThankYouPopupCtrl',
      ['$scope', '$modalInstance', 'SiteService', 'ErrorHandler', 'thankYouData', 'siteId', ThankYouPopupCtrl]);
})();
