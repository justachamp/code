'use strict';

describe('Service: ErrorHandler', function() {
  beforeEach(module('angulardash.common'));

  var $rootScope;
  var ErrorHandler;
  var form;
  var data;
  var status;
  var nestedInputs;
  var errors;

  beforeEach(inject(function(_$rootScope_, _ErrorHandler_) {
    $rootScope = _$rootScope_;
    ErrorHandler = _ErrorHandler_;
  }));

  describe('validates form without nested inputs', function() {
    beforeEach(function() {
      data = {
        email: ['Email is not verified']
      };
      status = 400;
      form = {};
      form.email = jasmine.createSpyObj(form.email, ['email', '$setValidity']);
      form.email.$error = {};
    });

    it('should process errors in data and put it into form object', function() {
      ErrorHandler.parseResponse(status, data, form);
      expect(form.email.$error.serverError[0]).toBe('Email is not verified');
    });

    it('should run setValidity on input', function() {
      ErrorHandler.parseResponse(status, data, form);
      expect(form.email.$setValidity).toHaveBeenCalled();
    });
  });

  describe('parses response for other HTTP statuses', function() {
    beforeEach(function() {
      data = '';
      status = 400;
      form = {};
    });

    it('401', function() {
      status = 401;
      errors = ErrorHandler.parseResponse(status, data, form);
      expect(errors.nonFieldServerErrors.length).toBe(1);
      expect(errors.fieldsWithErrors.length).toBe(0);
      expect(errors.nonFieldServerErrors[0]).toBe('Your session has expired, please login again.');
    });

    it('403', function() {
      status = 403;
      errors = ErrorHandler.parseResponse(status, data, form);
      expect(errors.nonFieldServerErrors.length).toBe(1);
      expect(errors.fieldsWithErrors.length).toBe(0);
      expect(errors.nonFieldServerErrors[0]).toBe('You are unauthorized to see this data');
    });

    it('429', function() {
      status = 429;
      errors = ErrorHandler.parseResponse(status, data, form);
      expect(errors.nonFieldServerErrors.length).toBe(1);
      expect(errors.fieldsWithErrors.length).toBe(0);
      expect(errors.nonFieldServerErrors[0]).toBe('There were too many requests. Try again tomorrow.');
    });
  });

  describe('parses response on 500 error with string data', function() {
    beforeEach(function() {
      data = '500 Internal Server Error has occured!';
      status = 500;
      form = {};
    });

    it('should process errors in data and return it', function() {
      errors = ErrorHandler.parseResponse(status, data, form);
      expect(errors.nonFieldServerErrors.length).toBe(1);
      expect(errors.fieldsWithErrors.length).toBe(0);
      expect(errors.nonFieldServerErrors[0]).toBe('Internal server error.');
    });
  });

  describe('parses response on 500 error without string data', function() {
    beforeEach(function() {
      data = {
        nonFieldServerErrors: ['An error']
      };
      status = 500;
      form = {};
    });

    it('should process errors in data and put it into existed list', function() {
      errors = ErrorHandler.parseResponse(status, data, form);
      expect(errors.nonFieldServerErrors.length).toBe(2);
      expect(errors.nonFieldServerErrors[0]).toBe('Internal server error.');
      expect(errors.nonFieldServerErrors[1]).toBe('An error');
    });
  });

  describe('parses response on nestedInputs', function() {
    beforeEach(function() {
      data = {
        domain: ['Here be error'],
        socialUrls: [
          {},
          {
            url: ['This url is already entered!'],
            service: ['This field is required.']
          }
        ]
      };
      status = 400;
      form = {};
      form.domain = jasmine.createSpyObj(form.domain, ['domain', '$setValidity']);
      form.domain.$error = {};
      form.linkedin = jasmine.createSpyObj(form.linkedin, ['linkedin', '$setValidity']);
      form.linkedin.$error = {};
      nestedInputs = {
        socialUrls: [{name: 'facebook'}, {name: 'linkedin'}]
      };
    });

    it('should process errors in data and put it into form object - not nested one', function() {
      ErrorHandler.parseResponse(status, data, form, nestedInputs);
      expect(form.domain.$error.serverError[0]).toBe('Here be error');
    });

    it('should run setValidity on input - not nested one', function() {
      ErrorHandler.parseResponse(status, data, form, nestedInputs);
      expect(form.domain.$setValidity).toHaveBeenCalled();
    });

    it('should process errors in data and put it into form object - nested one', function() {
      ErrorHandler.parseResponse(status, data, form, nestedInputs);
      expect(form.linkedin.$error.serverError[0]).toBe('This url is already entered!');
    });

    it('should run setValidity on input -  nested one', function() {
      ErrorHandler.parseResponse(status, data, form, nestedInputs);
      expect(form.linkedin.$setValidity).toHaveBeenCalled();
    });
  });
});
