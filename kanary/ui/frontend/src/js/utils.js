define([], function() {

    function formatBudget(value) {

        if (value === null) {
            return '';
        }

        var isInt = value % 1 == 0 ? true : false,
            value = parseFloat(value);

       if (isInt) {
            return value;
        } else {
            return value.toFixed(2);
        }
    }

    function formatDate(moment_date) {
        return moment_date.format(CONFIG.JS_DATE_FORMAT);
    }

    function formatTime(moment_time) {
        return moment_time.format(CONFIG.JS_DATE_FORMAT);
    }


    /**
     * Format given moment dt using given format string or return empty string
     * if the dt is empty or invalid.
     * @param {moment() | String} dt - moment dt or empty string.
     * @param {String} format_string - format understood by moment.
     * @return {String} formated datetime or empty string.
     */
    function format_dt(dt, format_string) {
        if (dt !== '' && dt.isValid()) {
            return dt.format(format_string);
        } else {
            return '';
        }

    }


    /**
     * Return true if the number is integer, false otherwise.
     */
    function is_int(num) {
        return num % 1 === 0;
    }

    /**
     * Format number to given precision using given policy.
     * @param {String} policy - how to fromat the number:
     *     'trimmed' - trim all unsignificant numbers (trailing zeros and
     *         decimal point if unsignificant)
     *     'fixed_float' - apply fixed point formating for floats and integer
     *          formating for integers.
     * @return {Number} formated number.
     */
    function formatFloat(value, precision, policy) {
        var fixed, trimmed;
        policy = policy || 'trimmed';

        if (!_.isNumber(value)) {
            value = 0;
        }

        fixed = value.toFixed(precision);

        if (policy === 'fixed_float') {
            if (is_int(value)) {
                return value.toFixed(0);
            } else {
                return fixed;
            }
        } else if (policy === 'trimmed') {
            // Number.toPrecision returns scientific notation for
            // big numbers. Use toFixed and trim '.00000...' if needed.
            trimmed = fixed.replace(/\.?0+$/, '');
            return trimmed;
        }
        return fixed;
    }

    function todayString() {
        return moment().format(CONFIG.JS_DATE_FORMAT_URL);
    };

    function nextMonthString() {
        return moment().add(1, 'M').format(CONFIG.JS_DATE_FORMAT_URL);
    };

    // Changes datestring to verbose name (i.e May 1st)
    function dateVerbose(datestring) {
        if (datestring) {
            return moment(
                datestring,
                CONFIG.JS_DATE_FORMAT_URL
            ).format('MMM Do');
        }
    };

    /**
     * Parses date passed as dd-mm-yyyy string (with optional hh:mm hour)
     * and returns its microtimestamp
     * @param {String} dateStr - parsed date chunk.
     * @param {String} hourStr - optional parsed time chunk.
     * @return {Number} un*x timestamp converted to microseconds.
     */
    function getMicrotime(dateStr, hourStr) {
        var momentWrapper = moment(
            dateStr + hourStr, CONFIG.JS_DATE_FORMAT + ' ' +
                CONFIG.JS_TIME_FORMAT
        );
        return momentWrapper.toDate().getTime();
    }

    function arePeriodsOverlapping(periodsArray) {
       /**
            Checks if provided periods overlap. Handles correctly only periods
            that don't cross midnight.
            @param {observableArray} periodsArray Periods which contain
            from and to observables
            @return {bool} True if periods overlap, otherwise false
        */
        var periods = periodsArray();
        var boundaries = new Array();

        if (periods.length <= 1) {
            return false;
        }

        /**
            Sort periods by start
        */
        periods = _.sortBy(periods, function(period) {
            return moment(period.from(), CONFIG.JS_TIME_FORMAT).unix();
        });

        /**
            Create a list of period boundaries, marked as start and end
        */
        ko.utils.arrayForEach(periods, function(period) {
            var start = {
                    date: moment(period.from(), CONFIG.JS_TIME_FORMAT),
                    start: true
                },
                end = {
                    date: moment(period.to(), CONFIG.JS_TIME_FORMAT),
                    start: false
                };
            boundaries.push(start);
            boundaries.push(end);
        });

        /**
            Sort by datetime.
        */
        boundaries = _.sortBy(boundaries, function(moment) {
            return moment.date.unix();
        });


        /**
            If two subsequent boundaries are starts, periods overlap
        */
        for (var i = 1; i < boundaries.length; i++) {
            var item = boundaries[i],
                previousItem = boundaries[i - 1];
            if (item.start && previousItem.start) {
                return true;
            }
        }

        return false;
    }

    function isPeriodOrderInvalid(periodsArray) {
        /**
            Checks if provided periods cross midnight (from > to)
            @param {observableArray} periodsArray Periods which contain
            from and to observables
            @return {bool} True if periods cross midnight, otherwise false
        */
        var periods = periodsArray();
        for (var i = 0; i < periods.length; i++) {
            var period = periods[i];
            var from = moment(period.from(), CONFIG.JS_TIME_FORMAT),
                to = moment(period.to(), CONFIG.JS_TIME_FORMAT);

            if (from.isAfter(to)) {
                return true;
            }
        }
        return false;
    }

    function isMinutePartInvalid(periodsArray) {
        /**
            Checks if minutes provided periods are multiples of 15 min
            @param {observableArray} periodsArray Periods which contain
            from and to observables
            @return {bool} True if periods are not multiples of quarter,
                otherwise false
        */
        var periods = periodsArray();
        function isDivisibleBy15(number) {
            return (number % 15 == 0);
        }
        for (var i = 0; i < periods.length; i++) {
            var period = periods[i];
            var from = moment(period.from(), CONFIG.JS_TIME_FORMAT),
                to = moment(period.to(), CONFIG.JS_TIME_FORMAT);

            if (!isDivisibleBy15(from.minutes()) ||
                !isDivisibleBy15(to.minutes())) {
                return true;
            }
        }
        return false;
    }

    // Functions check user input against chosen date/hour format
    function dateFormatMatch(datestring) {
        return RegExp('^[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}$').test(datestring);
    };

    function hourFormatMatch(hourstring) {
        return RegExp('^[0-9]{1,2}:[0-9]{2}$').test(hourstring);
    };

    // Functions check if valid numbers are passed into date/hour string
    function dateIsValid(datestring) {
        return moment(datestring, CONFIG.JS_DATE_FORMAT).isValid();
    }

    function hourIsValid(hourstring) {
        return moment(hourstring, CONFIG.JS_TIME_FORMAT).isValid();
    }

    // Return true if start date is not earlier that end
    // start, end - datestrings in DD-MM-YYYYHH:mm format
    function dateRelationCheck(start, end) {
        var fullDate = CONFIG.JS_DATE_FORMAT_URL + CONFIG.JS_TIME_FORMAT;
        return moment(start, fullDate) < moment(end, fullDate);
    }

    function showErrorTooltip(element, message) {
        $(element).attr('data-toggle', 'tooltip');
        $(element).attr('data-original-title', message);
        $(element).addClass('input-error');
    }

    function destroyErrorTooltip(element) {
        $(element).removeClass('input-error');
        $(element).removeAttr('data-original-title');
    }

    // Check value emptiness in terms of user input (all falsy values but empty
    // array and zero are treated empty). Return true if empty.
    function isEmpty(value) {
        return (_.isNaN(value) || value === '' || _.isUndefined(value) ||
                _.isNull(value));
    }

    function isPositiveInt(value) {
        return value % 1 == 0 && value >= 0;
    }

    // Get cookie contents by name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(
                        cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Wrapper for PATCH request
    // Sends in fact POST request with X-HTTP-Method-Override header
    // because of some issues with non-standard methods:
    // http://django-tastypie.readthedocs.org/en/latest/
    //             resources.html#using-put-delete-patch-in-unsupported-places
    $.extend({
        patchObject: function(url, obj) {
            return $.ajax({
                url: url,
                type: 'POST',
                headers: {'X-HTTP-Method-Override': 'PATCH'},
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify(obj)
            });
        }
    });

    // Wrapper for DELETE request
    // Sends in fact POST request with X-HTTP-Method-Override header
    $.extend({
        deleteObject: function(url) {
            return $.ajax({
                url: url,
                type: 'POST',
                headers: {'X-HTTP-Method-Override': 'DELETE'},
                contentType: 'application/json',
                dataType: 'json'
            });
        }
    });

    /**
     * Object reprezenting URL parameter treated as list
     *
     * @param {String} rawParams - comma separated list items passed as string.
     */
    function UrlListParam(rawParams) {
        // Parameter treated as list
        if (_.isUndefined(rawParams)) {
            rawParams = '';
        }

        var lpSelf = this,
            params = (rawParams.length > 0 && rawParams !== '-') ?
                rawParams.split(',') :
                [];

        /**
         * Tells whether item exists on list
         * @param {String} item - checked item.
         * @return {Boolean} true if exists, false otherwise.
         */
        lpSelf.has = function(item) {
            return (params.indexOf(item) !== -1);
        };

        /**
         * Inserts passed item onto the list (if does not exist yet)
         * @param {String} item - inserted item.
         */
        lpSelf.insert = function(item) {
            var currentIndex = params.indexOf(item);
            if (currentIndex === -1) {
                params.push(item);
            }
        };

        /**
         * Removes passed item from the list (if exists)
         * @param {String} item - deleted item.
         */
        lpSelf.remove = function(item) {
            var currentIndex = params.indexOf(item);
            if (currentIndex !== -1) {
                params.splice(currentIndex, 1);
            }
        };

        /**
         * Inserts/removes passed item to/from the list, depending on 2nd param
         * @param {String} item - processed item.
         * @param {Boolean} isInserted - whether item is inserted/deleted.
         */
        lpSelf.toggle = function(item, isInserted) {
            if (isInserted) {
                lpSelf.insert(item);
            } else {
                lpSelf.remove(item);
            }
        };

        /**
         * Removes from the list all items which are not allowed
         * If at least one item has been removed,
         * excludeCallback is called with new list length as a param
         *
         * @param {Array} allowed - list of allowed items (null - no limits).
         * @param {Number} maxSize - maximal length of destination list.
         * @param {Function} excludeCallback - function called after filtering.
         */
        lpSelf.filter = function(allowed, maxSize, excludeCallback) {
            var preLength = params.length,
                newParams = (_.isArray(allowed)) ?
                    _.intersection(params, allowed) :
                    params.slice(0);
            if (newParams.length > maxSize) {
                newParams = newParams.slice(0, maxSize);
            }
            if (!newParams.length || newParams.length < preLength) {
                // replacing contents on same array reference
                params.length = 0;
                Array.prototype.push.apply(params, newParams);
                if (_.isFunction(excludeCallback)) {
                    excludeCallback(params.length);
                }
            }
        };

        /**
         * Returns current lenght of list
         * @return {Number} - list's size.
         */
        lpSelf.count = function() {
            return params.length;
        };

        /**
         * Returns list contents as string with comma-separated items
         * @return {String} result string of unique list items.
         */
        lpSelf.asString = function() {
            return (params.length > 0) ?
                _.uniq(params.sort(), true).join(',') :
                '-';
        };

        /**
         * Returns list contents as array (copy of instance's list)
         * @return {Array} result array of unique list items.
         */
        lpSelf.asArray = function() {
            return _.uniq(params.sort(), true);
        };
    }

    /**
     * Executes passed function whet it is a function
     * @param {Function} func - callback function to be executed.
     */
    function exec(func) {
        if (_.isFunction(func)) {
            func();
        }
    }

    return {
        formatBudget: formatBudget,
        formatDate: formatDate,
        formatTime: formatTime,
        format_dt: format_dt,
        formatFloat: formatFloat,
        nextMonthString: nextMonthString,
        dateVerbose: dateVerbose,
        getMicrotime: getMicrotime,
        dateFormatMatch: dateFormatMatch,
        hourFormatMatch: hourFormatMatch,
        todayString: todayString,
        dateIsValid: dateIsValid,
        hourIsValid: hourIsValid,
        dateRelationCheck: dateRelationCheck,
        arePeriodsOverlapping: arePeriodsOverlapping,
        isPeriodOrderInvalid: isPeriodOrderInvalid,
        isMinutePartInvalid: isMinutePartInvalid,
        showErrorTooltip: showErrorTooltip,
        destroyErrorTooltip: destroyErrorTooltip,
        isEmpty: isEmpty,
        isPositiveInt: isPositiveInt,
        getCookie: getCookie,
        UrlListParam: UrlListParam,
        exec: exec
    };
});
