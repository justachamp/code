define(['validation', 'utils'], function(validation, utils) {

    /**
     * This is a mixin that provides basic validation mechanism for ViewModels
     * It is based on validation schema object that all VM must have if we want
     * to validate it.
     *
     * Mixin extends viewmodel by adding functions for checking individual
     * field for set of rules given in validation schema or for
     * checking all fields at once.
     *
     * For further documentation please refer to:
     * kanarydocs.jenkins.thearoom.clearcode.cc/front-end/validation.html
     */
    function ValidationMixin() {
        var self = this,
            fieldsLocation;

        self.errors = {};

        if (self.hasOwnProperty('fields')) {
            fieldsLocation = self.fields;
        } else {
            fieldsLocation = self;
        }

        // Add fields to validation and subscribes to validated fields
        $.each(self.validation, function(field) {
            self.validation[field].error = ko.observable(false);
            self.validation[field].errorApi = ko.observable(false);
            self.validation[field].visited = ko.observable(false);
            self.validation[field].errorMsg = ko.observable('');

            // Groups error in one object (stores references to
            // observables in validation object of ViewModel)
            // This should be read only.
            self.errors[field] = self.validation[field].error;
        });

        self.is_valid = function() {
            // validate all fields
            for (var field in self.validation) {
                self.checkField(field);
            }

            // Check if there are any errors
            for (var field in self.validation) {
                if (self.validation[field].error()) {
                    return false;
                }
            }

            // If all correct
            return true;
        };

        self.checkField = function(field) {
            var rules = self.validation[field].rules,
                fields = ko.utils.unwrapObservable(fieldsLocation),
                value = fields[field]();

            var showError = function(message) {
                self.validation[field].error(true);
                self.validation[field].errorMsg(message);
            };

            // check each rule
            if (rules.required && utils.isEmpty(value)) {
                showError('This field is required.');
                return;
            }

            if (rules.hasOwnProperty('minLength')) {
                if (value.length < rules.minLength) {
                    showError('Please enter at least ' +
                        rules.minLength + ' characters.');
                    return;
                }
            }

            if (rules.hasOwnProperty('maxLength')) {
                if (value.length > rules.maxLength) {
                    showError('Please enter no more than ' +
                        rules.maxLength + ' characters.');
                    return;
                }
            }

            if (rules.number) {
                value = parseFloat(value, 10);
                if (_.isNaN(value) || !_.isNumber(value)) {
                    showError('Please enter a number.');
                    return;
                }
            }

            if (rules.hasOwnProperty('min')) {
                if (value <= rules.min) {
                    showError('Please enter a value greater than ' +
                        rules.min + '.');
                    return;
                }
            }

            if (rules.hasOwnProperty('max')) {
                if (value >= rules.max) {
                    showError('Please enter a value less than ' +
                        rules.max + '.');
                    return;
                }
            }

            // custom validation
            if (rules.hasOwnProperty('customValidator')) {
                var customError = rules.customValidator(value, self);
                if (customError) {
                    showError(customError);
                    return;
                }
            }

            // show errors from API
            if (self.validation[field].errorApi()) {
                showError(self.validation[field].errorMsg());
                self.validation[field].errorApi(false);
                return;
            }

            // validation done, no errors fund
            self.validation[field].error(false);
            self.validation[field].errorMsg('');
        };

        self.showApiErrors = function(json, model_name) {

            $.each(json[model_name], function(field, errorMessage) {
                if (self.validation[field]) {
                    self.validation[field].errorApi(true);
                    self.validation[field].errorMsg(errorMessage);
                }
            });

            self.is_valid();
        };

        self.clearInputsErrors = function() {
            // removes error classes from inputs by setting errors to false
            for (field in self.validation) {
                self.validation[field].error(false);
                self.validation[field].errorApi(false);
                self.validation[field].visited(false);
                self.validation[field].errorMsg('');
            }
        };
    }

    return ValidationMixin;
});
