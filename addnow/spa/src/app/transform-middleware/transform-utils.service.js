(function() {
  'use strict';

  /**
   * @ngdoc Service tranformed camelCase objects to snake_case and vice versa.
   * @name app.tranform:TransformUtils
   *
   * @description
   *
   *
   * */

  function TransformUtils() {
    var transformer = function transformer(obj, transformFn) {
      var key;
      var resultObj;
      if (!obj) {
        return obj;
      }

      if (angular.isArray(obj)) {
        resultObj = obj.map(function(element) {
          return transformer(element, transformFn);
        });
      } else if ((typeof obj === 'object')) {
        resultObj = {};
        for (key in obj) {
          if (typeof obj[key] === 'object') {
            resultObj[transformFn(key)] = transformer(obj[key], transformFn);
          } else {
            resultObj[transformFn(key)] = obj[key];
          }
        }
      } else {
        resultObj = obj;
      }

      return resultObj;
    };

    this.toCamelCase = function(obj) {
      return transformer(obj, Case.camel);
    };

    this.toSnakeCase = function(obj) {
      return transformer(obj, Case.snake);
    };
  }

  angular.module('angulardash.transform-middleware')
    .service('TransformUtils', TransformUtils);
})();
