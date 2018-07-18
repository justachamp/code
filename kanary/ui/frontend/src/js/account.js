define(['notifications', 'utils'], function(notifications, utils) {

    function User() {

        var self = this;

        var fields = function() {
            this.id = ko.observable(null);
            this.username = ko.observable('');
            this.unread_events_count = ko.observable(0);
            this.timezone = ko.observable('');
            this.account_number = ko.observable(null);
            this.account_balance = ko.observable(null);
            this.email = ko.observable('');
        };

        self.fields = new ko.pontillo.rest.entity(new fields());
        self.fields.newEntity();

        // Change passsword related fields
        self.showPassForm = ko.observable(false);
        self.password = ko.observable('');
        self.new_password = ko.observable('');
        self.repeat_password = ko.observable('');

        // Computeds
        self.unread_events = ko.computed({
            owner: this,
            read: function() {
                return self.fields().unread_events_count() || 0;
            },
            write: function(value) {
                if (self.fields().unread_events_count() === value) {
                    return;
                }
                self.fields().unread_events_count(value);
                self.update_events_counter();
            }
        });

        self.account_balance = ko.computed({
            read: function() {
                var val = self.fields().account_balance(),
                    prefix = (val < 0) ? '-$' : '$';
                return prefix + utils.formatBudget(Math.abs(val));
            }
        });

        // Methods
        self.setFields = function(fieldsData) {
            for (fieldName in fieldsData) {
                var value = fieldsData[fieldName];
                if (ko.isObservable(self.fields()[fieldName])) {
                    self.fields()[fieldName](value);
                }
            }
        };

        self.togglePassForm = function() {
            self.showPassForm(!self.showPassForm());
        };

        self.clearPassFields = function() {
            self.password('');
            self.new_password('');
            self.repeat_password('');
        };

        // CRUD related
        self.load = function() {
            var url = Urls.api_dispatch_detail_id('account/user',
                                               loggedUser.fields().id());

            return self.fields.Get(url);
        };

        self.update_events_counter = function() {
            var url = Urls.update_counter(),
                counter_data = {counter: self.fields().unread_events_count()};

            return $.post(url, counter_data);
        };

        self.saveChanges = function() {
            var url = Urls.change_password(),
                passFields = {
                    password: self.password(),
                    new_password: self.new_password(),
                    repeat_password: self.repeat_password()
                };

            if (self.new_password() !== self.repeat_password()) {
                notifications.showModal(
                    'Error!',
                    "New passwords didn't match each other."
                );
                return;
            }

            var savePromise = $.post(url, passFields);

            savePromise.done(function(resp) {
                notifications.show('Password changed succesfully!', 3);
                self.showPassForm(false);
                self.clearPassFields();
            });

            savePromise.fail(function(resp) {
                notifications.showModal('Error!', resp.responseText);
            });
        };

    }

    // globally available object which is constantly updated
    // used mainly to detect changes in unread events in real-like manner
    var loggedUser = new User({});

    var getLoggedUser = function() {
        var users_url = Urls.api_dispatch_list('account/user');

        return $.getJSON(users_url).done(function(resp) {
            loggedUser.setFields(resp.objects[0]);
        });
    };

    function TransactionRow(tr_data) {
        var self = this;

        self.date = ko.observable(tr_data.date);
        self.number = ko.observable(tr_data.number || '-');
        self.event = ko.observable(tr_data.event);
        self.status = ko.observable(tr_data.status || '-');
        self.amount = ko.observable(tr_data.amount);
        self.download_url = ko.observable(tr_data.download_url || null);

    };

    function BillingInfo() {
        var self = this;

        self.account_balance = ko.observable(0);
        self.last_payment = ko.observable('-');
        self.transactions = ko.observableArray([]);

        self.load = function() {
            var url = Urls.billing_info();

            return $.getJSON(url, function(response) {
                self.account_balance(response.account_balance);

                if (response.last_payment) {
                    self.last_payment(response.last_payment);
                } else {
                    self.last_payment('-');
                }

                self.transactions([]);
                _.forEach(response.transactions, function(transaction) {
                    self.transactions.push(new TransactionRow(transaction));
                });
            });
        };
    };

    var init = function() {
        getLoggedUser().done(function() {
            ko.applyBindings({user: loggedUser}, $('#header')[0]);
        });
    };

    return {
        // user model used in account info view
        user: new User({}),
        BillingInfo: new BillingInfo(),
        loggedUser: loggedUser,
        getLoggedUser: getLoggedUser,
        init: init
    };

});
