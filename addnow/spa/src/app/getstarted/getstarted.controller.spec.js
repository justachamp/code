'use strict';

describe('GetStartedCtrl', function() {
  beforeEach(module('angulardash.getstarted'));

  var $scope;
  var $controller;
  var $location;
  var $localStorage;
  var GetStartedCtrl;

  function createController() {
    GetStartedCtrl = $controller('GetStartedCtrl', {
      $scope: $scope,
      $location: $location,
      $localStorage: $localStorage
    });
  }

  beforeEach(inject(function($rootScope, _$controller_) {
    $scope = $rootScope.$new();
    $controller = _$controller_;

    $location = jasmine.createSpyObj('$location', ['path', 'search', 'url']);
    $location.path.and.returnValue('/');
    $location.search.and.returnValue({website:'ww.pl'});
    $localStorage = {};
  }));

  describe('GetStartedCtrl - submitform', function() {
    beforeEach(function() {
      createController();
    });

    it('should set website to localstorage when form has no errors', function() {
      $scope.submitform(true);
      expect($localStorage.website).toEqual('ww.pl');
    });

    it('should not set website to localstorage when form has errors', function() {
      $scope.submitform(false);
      expect($localStorage.website).toEqual(undefined);
    });
  });
});
