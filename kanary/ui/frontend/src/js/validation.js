define(['utils'], function(utils) {

   // This module contains only custom validation rules.
   // For validation mechanism please refer to mixins/validation.js

   // custom validators
    function dateRelationIsValid(VM) {
        var start = VM.fields().start() + VM.fields().start_hour(),
            end = VM.fields().end() + VM.fields().end_hour();

        return utils.dateRelationCheck(start, end);
    }

    function dateValidator(value, viewModel) {

        if (!utils.dateFormatMatch(value)) {
            return 'Date must be in DD-MM-YYYY format';
        } else if (!utils.dateIsValid(value)) {
            return 'This is not a valid date';
        } else if (!dateRelationIsValid(viewModel)) {
            return 'Start date cannot be later than end';
        }
    };

    function hourValidator(value, viewModel) {

        if (!utils.hourFormatMatch(value)) {
            return 'Hour must be in HH:mm format';
        } else if (!utils.hourIsValid(value)) {
            return 'This is not a valid hour';
        } else if (!dateRelationIsValid(viewModel)) {
            return 'Start date cannot be later than end';
        }
    };

    function positiveIntegerCheck(value, viewModel) {

        if (value === '') {
            return false;
        }

        if (!utils.isPositiveInt(value)) {
            return 'Value must be a positive integer.';
        }
    };

    var url_re = new RegExp('(http|https):\\/\\/(\\w+:{0,1}\\w*@)?(\\S+)' +
            '(:[0-9]+)?(\\/|\\/([\\w#!:.?+=&%@!\\-\\/]))?');

    /*
     * Validate URL. Return error message if URL is invalid, false otherwise.
     */
    function isUrl(string) {
        if (!url_re.test(string)) {
            return 'Url is invalid';
        }
        return false;
    };

    /*
     * Validate URL. Return error message if URL is invalid, false otherwise.
     * URL may be empty.
     */
    function isUrlOrEmpty(string) {
        if (utils.isEmpty(string)) {
            return false;
        }
        return isUrl(string);
    };


    return {
        dateValidator: dateValidator,
        hourValidator: hourValidator,
        positiveIntegerCheck: positiveIntegerCheck,
        isUrl: isUrl,
        isUrlOrEmpty: isUrlOrEmpty
    };

});
