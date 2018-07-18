(function() {
  'use strict';

  function AccountSettingsFactory($filter) {
    var factory = {};
    var localDate = new Date();
    var timeZonesOffsets = [14, 13, 12.75, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.75, 8, 7, 6.5, 6, 5.75, 5.5, 5,
      4.5, 4, 3.5, 3, 2, 1, 0, -1, -2, -3, -3.5, -4, -4.5, -5, -6, -7, -8, -9, -9.5, -10, -11, -12];
    var utcName = '';
    var twoDigitNumber = function twoDigitNumber(number) {
      return ('0' + Math.floor(Math.abs(number))).slice(-2);
    };

    factory.timeZones = [];

    timeZonesOffsets.forEach(function(offset) {
      if (offset > 0) {
        utcName = ' UTC+' + twoDigitNumber(offset);
      } else if (offset === 0) {
        utcName = ' UTC';
      } else {
        utcName = ' UTC-' + twoDigitNumber(offset);
      }

      if (offset % 1 !== 0) {
        utcName += ':' + (Math.abs(offset % 1) * 60);
      }

      factory.timeZones.push(
        {
          name: $filter('date')(new Date(localDate.getTime() + (3600000 * offset)), 'HH:mm', 'UTC') +
          utcName,
          value: (offset * 60)
        }
      );
    });

    return factory;
  }

  angular.module('angulardash.account-settings')
    .factory('AccountSettingsFactory', ['$filter', AccountSettingsFactory]);

})();
