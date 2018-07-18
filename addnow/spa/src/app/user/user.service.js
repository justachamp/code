(function() {
  'use strict';

  function UserService($http, AppSettings, MenuService) {
    var backendApi = AppSettings.backendApi;

    this.signUp = function signUp(email, password) {
      return $http.post(backendApi + 'users', {email: email, password: password});
    };

    this.verify = function verify(email) {
      return $http.put(backendApi + 'users/verify', {email: email});
    };

    this.confirmEmail = function confirmEmail(token) {
      return $http.get(backendApi + 'users/verify/' + token);
    };

    this.remindersUnsubscribe = function remindersUnsubscribe(token) {
      return $http.get(backendApi + 'reminders/mute/' + token);
    };

    this.signIn = function signIn(email, password) {
      return $http.post(backendApi + 'tokens', {email: email, password: password}).success(function(data) {
        MenuService.uploadMenuItems();
        return data;
      });
    };

    this.forgotPass = function forgotPass(email) {
      return $http.post(backendApi + 'users/reset_password', {email: email});
    };

    this.resetPass = function resetPass(token, password) {
      return $http.post(backendApi + 'users/change_password',
        {token: token, password: password});
    };
  }

  angular.module('angulardash.user')
    .service('UserService', ['$http', 'AppSettings', 'MenuService', UserService]);
})();
