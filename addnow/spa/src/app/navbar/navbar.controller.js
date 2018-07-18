(function() {
  'use strict';

  function NavbarCtrl($scope, MenuService, $location, $localStorage, $routeParams) {
    $scope.$storage = $localStorage;
    $scope.showUserMenu = false;
    $scope.showEdit = $location.path().indexOf('/site/dashboard') !== -1;
    $scope.showDashboard = $location.path().indexOf('/site/edit') !== -1;

    $scope.links = {
      userMenu: [
        {
          label: 'Settings',
          href: '/settings/'
        },
        {
          label: 'Sign out',
          href: '/logout/'
        }
      ]
    };
    $scope.toggleUserMenu = function toggleUserMenu() {
      $scope.showUserMenu = !$scope.showUserMenu;
    };

    this.selectMenuItem = function selectMenuItem() {
      MenuService.getMenu().then(function(sites) {
        $scope.sites = sites;
        if ($routeParams.siteId) {
          angular.forEach($scope.sites, function(site) {
            if (site.id === parseInt($routeParams.siteId)) {
              $scope.selectedSite = site;
            }
          });
        }
      });
    };

    this.selectMenuItem();

    $scope.siteChange = function siteChange(id) {
      if (id > 0) {
        $location.search('');
        $location.path('/site/dashboard/' + id);
      }
    };

    $scope.$watch('$storage.menuUpdatedTs', function(newValue, oldValue) {
      if (oldValue !== newValue && newValue !== undefined) {
        MenuService.uploadMenuItems();
      }
    });

    if (!$scope.$storage.token || !$scope.$storage.email) {
      $location.path('/signin/');
    }
  }

  angular.module('angulardash.navbar')
    .controller('NavbarCtrl', ['$scope', 'MenuService', '$location', '$localStorage', '$routeParams', NavbarCtrl]);
})();
