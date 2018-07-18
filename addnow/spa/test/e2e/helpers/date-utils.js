'use strict';

var moment = require('moment');
var PICKER_DATE_FORMAT = 'YYYY-MM-DD';

exports.buildDatePickerValue = function buildDatePickerValue(period) {
  var start;
  var end;
  var label;
  if (period === 'day') {
    start = moment().utc().startOf('day');
  } else {
    start = moment().utc().subtract(1, period);
  }

  end = moment().utc().endOf('day');
  label = start.format(PICKER_DATE_FORMAT) + ' - ' + end.format(PICKER_DATE_FORMAT);
  return label;
};
