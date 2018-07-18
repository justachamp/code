(function() {
  'use strict';

  function configureRoutes($routeProvider) {
    $routeProvider
      .when('/passforgot/', {
        templateUrl: 'app/user/resetpass.html',
        controller: 'UserCtrl'
      })
      .when('/resetpass/:mailToken', {
        templateUrl: 'app/user/resetpass2.html',
        controller: 'UserCtrl'
      })
      .when('/signin/', {
        templateUrl: 'app/user/signin.html',
        controller: 'UserCtrl'
      })
      .when('/logout/', {
        template: '',
        controller: 'LogoutCtrl'
      })
      .when('/signup/', {
        templateUrl: 'app/user/signup.html',
        controller: 'UserCtrl'
      })
      .when('/confirmation/', {
        templateUrl: 'app/user/confirmation.html',
        controller: 'ConfirmationCtrl'
      })
      .when('/confirm/:mailToken', {
        templateUrl: 'app/user/confirmation-done.html',
        controller: 'ConfirmationDoneCtrl'
      })
      .when('/reminders/unsubscribe/:token', {
        templateUrl: 'app/user/reminder-unsubscribe.html',
        controller: 'ReminderUnsubscribeCtrl'
      });
  }

  angular.module('angulardash.user', ['angulardash.common', 'ngStorage', 'ngRoute', 'angulardash.navbar',
    'angulardash.configuration', 'angulardash.transform-middleware']).config(['$routeProvider', configureRoutes]);
})();
