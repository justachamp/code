(function() {
  'use strict';

  function ErrorHandler($location) {
    this.flushServerErrors = function flushServerErrors(form, errors) {
      if (errors.fieldsWithErrors) {
        errors.fieldsWithErrors.forEach(function(field) {
          form[field].$setValidity('serverError', true);
        });
      }

      errors.nonFieldServerErrors = [];
    };

    this.parseResponse = function parseResponse(code, data, form, nestedInputs) {
      var nestedErr;
      var nonFieldServerErrors = data.nonFieldErrors || [];
      var fieldsWithErrors = [];
      var field;

      delete data.nonFieldErrors;
      nestedInputs = nestedInputs || {};
      if (angular.isString(data)) {
        data = {};
      }

      switch (code){
        case 401:
          nonFieldServerErrors.push('Your session has expired, please login again.');
          $location.path('/signin');
          break;
        case 403:
          nonFieldServerErrors.push('You are unauthorized to see this data');
          break;
        case 429:
          nonFieldServerErrors.push('There were too many requests. Try again tomorrow.');
          break;
        case 500:
        case 404:
          nonFieldServerErrors.push('Internal server error.');
          break;
      }

      // Add server-side errors here
      angular.forEach(data, function(value, key) {
        if (nestedInputs[key]) {
          for (nestedErr in value) {
            if (Object.keys(value[nestedErr]).length > 0) {
              field = nestedInputs[key][nestedErr].name;
              if (form[field]) {
                form[field].$setValidity('serverError', false);
                form[field].$error.serverError = value[nestedErr].url;
                fieldsWithErrors.push(field);
              }
            }
          }
        } else {
          if (key in form) {
            form[key].$setValidity('serverError', false);
            form[key].$error.serverError = value;
            fieldsWithErrors.push(key);
          } else {
            nonFieldServerErrors = nonFieldServerErrors.concat(value);
          }
        }
      });

      return {
        nonFieldServerErrors: nonFieldServerErrors,
        fieldsWithErrors: fieldsWithErrors
      };
    };
  }

  angular.module('angulardash.common').service('ErrorHandler', ['$location', ErrorHandler]);
})();
