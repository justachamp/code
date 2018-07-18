'use strict';

describe('Service: TransformUtils', function() {

  // load the service's module
  beforeEach(module('angulardash.transform-middleware'));

  // instantiate service
  var service;

  //update the injection
  beforeEach(inject(function(_TransformUtils_) {
    service = _TransformUtils_;
  }));

  it('should transform snake_case object to camelCase', function() {
    // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
    var obj = {
      property_a: 1,
      property_b: 'aaa',
      props_my: [
        {
          keyAbc: 'abc',
          key_b: 'qwe'
        }
      ]
    };
    var expected = {
      propertyA: 1,
      propertyB: 'aaa',
      propsMy: [
        {
          keyAbc: 'abc',
          keyB: 'qwe'
        }
      ]
    };

    // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
    expect(service.toCamelCase(obj)).toEqual(expected);
  });

  it('should transform snake_case array to camelCase', function() {
    // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
    var obj = [
      {
        keyAbc: 'abc',
        key_b: 'qwe'
      }, {
        title: 'abc',
        name_value: 'qwe'
      }
    ];
    var expected = [{
        keyAbc: 'abc',
        keyB: 'qwe'
      }, {
        title: 'abc',
        nameValue: 'qwe'
      }];

    // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
    expect(service.toCamelCase(obj)).toEqual(expected);
  });
});
