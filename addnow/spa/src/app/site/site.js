(function() {
  'use strict';

  function configureRoutes($routeProvider) {
    $routeProvider
      .when('/site/add', {
        templateUrl: 'app/site/addSite.html',
        controller: 'SiteCtrl'
      })
      .when('/site/edit/:siteId', {
        templateUrl: 'app/site/addSite.html',
        controller: 'SiteCtrl'
      })
      .when('/site/dashboard/:siteId', {
        templateUrl: 'app/site/dashboard-site.html',
        controller: 'DashboardSiteCtrl'
      })
      .when('/page/:pageId', {
        templateUrl: 'app/site/static-page.html',
        controller: 'StaticCtrl'
      });
  }

  angular.module('angulardash.site', ['ngRoute', 'ngResource', 'angularSpinner', 'daterangepicker', 'ui.sortable',
      'sprintf', 'ngTable', 'ngTableExport', 'ngScrollSpy', 'toggle-switch', 'ui.bootstrap', 'smoothScroll',
      'iso-3166-country-codes', 'angular-capitalize-filter', 'angulardash.common', 'angulardash.configuration',
      'angulardash.transform-middleware'])
    .config(['$routeProvider', configureRoutes]);
})();
