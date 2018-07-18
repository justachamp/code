(function() {
  'use strict';

  /* global $ */

  function slider($parse, $timeout) {
    return {
      restrict: 'AE',
      replace: true,
      template: '<div><input class="slider-input" type="text" /></div>',
      require: 'ngModel',
      scope: {
        max: '=',
        min: '=',
        step: '=',
        value: '=',
        ngModel: '=',
        range: '=',
        sliderid: '=',
        formatter: '&',
        onStartSlide: '&',
        onStopSlide: '&',
        onSlide: '&',
        ticks: '=',
        ticksLabels: '='
      },
      link: function($scope, element, attrs, ngModelCtrl) {
        var ngModelDeregisterFn;
        var ngDisabledDeregisterFn;
        var strNbr;
        var decimals;
        var value;
        var slider;
        var updateEvent;
        var sliderEvents;
        var watchers;

        function initSlider() {
          var options = {};

          function setOption(key, value, defaultValue) {
            options[key] = value || defaultValue;
          }

          function setFloatOption(key, value, defaultValue) {
            options[key] = value ? parseFloat(value) : defaultValue;
          }

          function setBooleanOption(key, value, defaultValue) {
            options[key] = value ? String(value) === 'true' : defaultValue;
          }

          function getArrayOrValue(value) {
            return (angular.isString(value) && value.indexOf('[') === 0) ? angular.fromJson(value) : value;
          }

          setOption('id', $scope.sliderid);
          setOption('orientation', attrs.orientation, 'horizontal');
          setOption('selection', attrs.selection, 'before');
          setOption('handle', attrs.handle, 'round');
          setOption('tooltip', attrs.tooltip, 'hide');
          if ($scope.ticksLabels) {
            if (!$scope.ticks) {
              setOption('ticks', $scope.ticksLabels.map(function(el, index) {
                return parseInt(index);
              }));
            } else {
              setOption('ticks', $scope.ticks);
            }

            setOption('ticks_labels', $scope.ticksLabels);
          } else {
            setFloatOption('min', $scope.min, 0);
            setFloatOption('max', $scope.max, 10);
          }

          setOption('tooltipseparator', attrs.tooltipseparator, ':');
          setFloatOption('step', $scope.step, 1);
          strNbr = String(options.step);
          decimals = strNbr.substring(strNbr.lastIndexOf('.') + 1);
          setFloatOption('precision', attrs.precision, decimals);

          setBooleanOption('tooltip_split', attrs.tooltipsplit, false);
          setBooleanOption('enabled', attrs.enabled, true);
          setBooleanOption('naturalarrowkeys', attrs.naturalarrowkeys, false);
          setBooleanOption('reversed', attrs.reversed, false);

          setBooleanOption('range', $scope.range, false);
          if (options.range) {
            if (angular.isArray($scope.value)) {
              options.value = $scope.value;
            } else if (angular.isString($scope.value)) {
              options.value = getArrayOrValue($scope.value);
              if (!angular.isArray(options.value)) {
                value = parseFloat($scope.value);
                if (isNaN(value)) {
                  value = 5;
                }

                if (value < $scope.min) {
                  value = $scope.min;
                  options.value = [value, options.max];
                } else if (value > $scope.max) {
                  value = $scope.max;
                  options.value = [options.min, value];
                } else {
                  options.value = [options.min, options.max];
                }
              }
            } else {
              options.value = [options.min, options.max];

              // This is needed, because of value defined at
              // $.fn.slider.defaults - default value 5 prevents creating range slider
            }

            $scope.ngModel = options.value; // needed, otherwise turns value into [null, ##]
          } else {
            setFloatOption('value', attrs.value, 5);
          }

          if ($scope.formatter) {
            options.formatter = $scope.$eval($scope.formatter);
          }

          slider = $(element).find('.slider-input').eq(0);

          // check if slider jQuery plugin exists
          if ($.fn.bootstrapSlider) {
            // adding methods to jQuery slider plugin prototype
            $.fn.bootstrapSlider.constructor.prototype.disable = function() {
              this.picker.off();
            };

            $.fn.bootstrapSlider.constructor.prototype.enable = function() {
              this.picker.on();
            };

            // destroy previous slider to reset all options
            //slider.bootstrapSlider(options);
            //slider.bootstrapSlider('destroy');
            slider.bootstrapSlider(options);

            // everything that needs slider element
            updateEvent = getArrayOrValue(attrs.updateevent);
            if (angular.isString(updateEvent)) {
              // if only single event name in string
              updateEvent = [updateEvent];
            } else {
              // default to slide event
              updateEvent = ['slide'];
            }

            angular.forEach(updateEvent, function(sliderEvent) {
              slider.on(sliderEvent, function(ev) {
                ngModelCtrl.$setViewValue(ev.value);
                $timeout(function() {
                  $scope.$apply();
                });
              });
            });

            slider.on('change', function(ev) {
              ngModelCtrl.$setViewValue(ev.value.newValue);
              $timeout(function() {
                $scope.$apply();
              });
            });

            // Event listeners
            sliderEvents = {
              slideStart: 'onStartSlide',
              slide: 'onSlide',
              slideStop: 'onStopSlide'
            };
            angular.forEach(sliderEvents, function(sliderEventAttr, sliderEvent) {
              slider.on(sliderEvent, function(ev) {
                if ($scope[sliderEventAttr]) {
                  var invoker = $parse(attrs[sliderEventAttr]);
                  invoker($scope.$parent, {$event: ev, value: ev.value});

                  $timeout(function() {
                    $scope.$apply();
                  });
                }
              });
            });

            // deregister ngDisabled watcher to prevent memory leaks
            if (angular.isFunction(ngDisabledDeregisterFn)) {
              ngDisabledDeregisterFn();
              ngDisabledDeregisterFn = null;
            }

            if (angular.isDefined(attrs.ngDisabled)) {
              ngDisabledDeregisterFn = $scope.$watch(attrs.ngDisabled, function(value) {
                if (value) {
                  slider.bootstrapSlider('disable');
                } else {
                  slider.bootstrapSlider('enable');
                }
              });
            }

            // deregister ngModel watcher to prevent memory leaks
            if (angular.isFunction(ngModelDeregisterFn)) {
              ngModelDeregisterFn();
            }

            ngModelDeregisterFn = $scope.$watch('ngModel', function(value) {
              slider.bootstrapSlider('setValue', value);
            });
          }
        }

        initSlider();

        watchers = ['min', 'max', 'step', 'range', 'ticks', 'ticksLabels'];
        angular.forEach(watchers, function(prop) {
          $scope.$watch(prop, function() {
            initSlider();
          });
        });
      }
    };
  }

  angular.module('angulardash.common')
    .directive('slider', ['$parse', '$timeout', slider]);

})();