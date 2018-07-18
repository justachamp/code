(function() {
  'use strict';

  angular.module('ngMockE2E').factory('loginBackend', ['$httpBackend', function($httpBackend) {
    return {
      _register: {},
      config: function(requestIdGetter, sessionGetter, responseOverride, sessionFactory) {
        this.requestIdGetter = requestIdGetter;
        this.responseOverride = responseOverride;
        this.sessionGetter = sessionGetter;
        this.sessionFactory = sessionFactory;
      },

      session: function(username) {
        var expectedHeaders = this._session(username);

        return function(headers) {
          var result = true;
          var headerName;
          for (headerName in expectedHeaders) {
            if (expectedHeaders[headerName] !== headers[headerName]) {
              result = false;
              break;
            }
          }

          return result;
        };
      },

      _session: function(username) {
        var session = this._register[username];

        if (session) {
          return this.sessionFactory(session);
        }

        throw new Error('Unexpected login "' + username + '"');
      },

      when: function(method, url, data, headers) {
        var username = this.requestIdGetter(method, url, data, headers);
        var _this = this;
        var connection;

        connection = $httpBackend.when(method, url, data, headers);

        return {
          respond: function(status, data, headers, statusText) {
            _this._register[username] = _this.sessionGetter(status, data, headers, statusText);

            return connection.respond.call(connection, status, data, headers, statusText);
          }
        };
      }
    };
  }]);
})();
