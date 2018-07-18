define(['account', 'storage', 'utils', 'router', 'validation', 'StrategyState',
        'notifications', 'mixins/validation', 'mixins/toggle_state'],
    function(account, storage, utils, router, validation, StrategyState,
             notifications, ValidationMixin, ToggleStateMixin) {

    // model for single strategy in list
    // strategy is a single object from campaign.fields().strategies() array
    function Strategy(strategy) {
        var self = this;

        self.id = ko.observable(strategy.id());
        self.name = ko.observable(strategy.name());
        self.slug = ko.observable(strategy.slug());
        self.paused = ko.observable(strategy.paused());

        self.state = new StrategyState(strategy.state);

        ToggleStateMixin.apply(self, arguments);
    };


    function campaignVM() {
        var self = this,
            is_empty = utils.isEmpty,
            defaultStart = utils.todayString(),
            defaultEnd = utils.nextMonthString(),
            defaultHour = '17:00',
            cap_period = 'hour',
            loggedUser = account.loggedUser,
            validationSteps = {
                untouched: 'untouched',
                draft: 'draft',
                validated: 'validated'
            },
            stepName = {
                overall: 'overall',
                budget: 'budget',
                conversion: 'conversion',
                capping: 'capping'
            },
            modeName = {
                newCampaign: 'new',
                editCampaign: 'edit'
            };

        // fields corresponding with API model
        var fields = function() {
            var self = this;

            self.id = ko.observable(0);

            self.paused = ko.observable(null);
            self.archived = ko.observable(null);

            self.budget_left = ko.observable('0');
            self.budget_spent_with_commission = ko.observable('0');
            self.budget_total = ko.observable(null);

            // Conversion tracker parameters
            self.conversion_active = ko.observable(false);
            self.conversion_name = ko.observable('New conversion');
            self.conversion_value = ko.observable('1');
            self.conversion_code = ko.observable('');

            // Actual capping parameters
            self.cap_campaign = ko.observable(null);
            self.cap_strategy = ko.observable(null);
            self.cap_creative = ko.observable(null);
            self.cap_campaign_period = ko.observable(null);
            self.cap_strategy_period = ko.observable(null);
            self.cap_creative_period = ko.observable(null);

            // State of activation checkboxes in capping step
            self.cap_campaign_selected = ko.observable(false);
            self.cap_strategy_selected = ko.observable(false);
            self.cap_creative_selected = ko.observable(false);

            // Capping parameters that are presented in form.
            // Actual parameters are computed by analyzing state of presented
            // ones and state of activation checkboxes
            self.cap_campaign_presented = ko.observable(null);
            self.cap_strategy_presented = ko.observable(null);
            self.cap_creative_presented = ko.observable(null);
            self.cap_campaign_period_presented = ko.observable(cap_period);
            self.cap_strategy_period_presented = ko.observable(cap_period);
            self.cap_creative_period_presented = ko.observable(cap_period);

            self.default_landing_page_url = ko.observable('');

            self.name = ko.observable('Untitled campaign');
            self.resource_uri = ko.observable('');
            self.slug = ko.observable('');

            self.account_timezone = ko.observable(
                loggedUser.fields().timezone()
            );
            self.start = ko.observable(defaultStart);
            self.start_hour = ko.observable(defaultHour);

            self.end = ko.observable(defaultEnd);
            self.end_hour = ko.observable(defaultHour);

            self.seconds_left = ko.observable();

            self.strategies = ko.observableArray();
        };

        // Initialize REST API wrapper for fields
        self.fields = new ko.pontillo.rest.entity(new fields());
        self.fields.newEntity();

        self.loadStrategies = function() {
            var list = self.fields().strategies();

            self.fields().strategies([]);

            self.fields().strategies(
                _.map(list, function(strategy) {
                    return new Strategy(strategy);
                })
            );
        };

        self.validation = {
            name: {
                rules: {
                    required: true
                }
            },
            start: {
                rules: {
                    required: true,
                    customValidator: validation.dateValidator
                }
            },
            end: {
                rules: {
                    required: true,
                    customValidator: validation.dateValidator
                }
            },
            start_hour: {
                rules: {
                    required: true,
                    customValidator: validation.hourValidator
                }
            },
            end_hour: {
                rules: {
                    required: true,
                    customValidator: validation.hourValidator
                }
            },
            default_landing_page_url: {
                rules: {
                    required: true,
                    customValidator: validation.isUrl
                }
            },
            budget_total: {
                rules: {
                    required: true
                }
            },
            conversion_name: {
                rules: {
                    required: true
                }
            },
            conversion_value: {
                rules: {
                    required: true
                }
            },
            cap_campaign_presented: {
                rules: {
                    customValidator: validation.positiveIntegerCheck
                }
            },
            cap_strategy_presented: {
                rules: {
                    customValidator: validation.positiveIntegerCheck
                }
            },
            cap_creative_presented: {
                rules: {
                    customValidator: validation.positiveIntegerCheck
                }
            }
        };

        ValidationMixin.apply(self, arguments);

        self.mode = ko.observable(modeName.newCampaign);
        self.step = ko.observable(stepName.overall);


        // for displaying ie. January 1st instead of 2013-01-01
        self.startVerbose = ko.computed(function() {
            return utils.dateVerbose(self.fields().start());
        });

        self.endVerbose = ko.computed(function() {
            return utils.dateVerbose(self.fields().end());
        });

        self.dateFormatConversion = function(field) {
            // field - date field from fields() (start or end)
            return moment(field, CONFIG.JS_DATE_FORMAT_URL)
                    .format(CONFIG.JS_DATE_FORMAT);
        };

        self.startVerboseDatepicker = ko.computed(function() {
            return self.dateFormatConversion(self.fields().start());
        });

        self.endVerboseDatepicker = ko.computed(function() {
            return self.dateFormatConversion(self.fields().end());
        });

        /**
         * A humanized representation of campaign duration left
         * like: '(a minute left)', or '(finished)'.
         */
        self.timeLeft = ko.computed(function() {
            var seconds_left = self.fields().seconds_left(),
                diff = moment.duration(seconds_left, 'seconds').humanize();

            return (seconds_left == 0) ? 'finished' : diff + ' left'
        });

        self.budgetTotalFormatted = ko.computed(function() {
            return utils.formatBudget(self.fields().budget_total());
        });

        self.budgetSpentFormatted = ko.computed(function() {
            return utils.formatBudget(
                 parseFloat(
                    self.fields().budget_spent_with_commission(), 10
                )
            );
        });

        self.budgetSpentPercent = ko.computed(function() {
            var spent, total;

            spent = parseFloat(
                self.fields().budget_spent_with_commission(), 10
            );
            total = self.fields().budget_total();
            return ((spent / total) * 100).toFixed(2);
        });

        //
        self.updateStrategiesToggleMessage = ko.computed(function() {
            var isActive;
            _.each(self.fields().strategies(), function(strategy) {
                if (!strategy.hasOwnProperty('toggleText')) {
                    isActive = !strategy.paused();
                    if (isActive) {
                        strategy.toggleText =
                            ko.observable('Deactivate strategy');
                    } else {
                        strategy.toggleText =
                            ko.observable('Activate strategy');
                    }
                }
            });
        });

        // URL of this campaign object
        self.url = ko.computed(function() {
            if (self.fields().slug() === '') {
                return;
            }
            return router.path.campaign_overview({campaignName:
                                                  self.fields().slug()});
        });

        // CAPPING LOGIC

        self.cappingOptions = ['hour', 'day', 'month', 'year'];

        self.computeCappingValues = function(capping_attributes) {
        /* update fields involved in capping based on value of fields
           presented in form and checkbox state

           capping attributes - object containing following keys that
           represents NAMES of attributes in fields() instance that provide
           given information:
               cap_value - actual capping value
               cap_period - actual capping period value
               cap_value_presented - value of capping presented in form
               cap_period_presented - value of capping period presented in form
               cap_selected - checkbox state
        */
            var attrs = capping_attributes,
                value_presented = self.fields()[attrs.cap_value_presented](),
                period_presented = self.fields()[attrs.cap_period_presented](),
                selected = self.fields()[attrs.cap_selected]();

            if (selected) {
                self.fields()[attrs.cap_value](value_presented);
                self.fields()[attrs.cap_period](period_presented);
            } else {
                self.fields()[attrs.cap_value](null);
                self.fields()[attrs.cap_period](null);
            }
        };

        var campaign_capping_attrs = {
                cap_value: 'cap_campaign',
                cap_period: 'cap_campaign_period',
                cap_value_presented: 'cap_campaign_presented',
                cap_period_presented: 'cap_campaign_period_presented',
                cap_selected: 'cap_campaign_selected'
            },
            strategy_capping_attrs = {
                cap_value: 'cap_strategy',
                cap_period: 'cap_strategy_period',
                cap_value_presented: 'cap_strategy_presented',
                cap_period_presented: 'cap_strategy_period_presented',
                cap_selected: 'cap_strategy_selected'
            },
            creative_capping_attrs = {
                cap_value: 'cap_creative',
                cap_period: 'cap_creative_period',
                cap_value_presented: 'cap_creative_presented',
                cap_period_presented: 'cap_creative_period_presented',
                cap_selected: 'cap_creative_selected'
            };

        // Observer reacts when any of field in form is updated and counts
        // the value of capping attributes
        self.campaignCappingObserver = ko.computed(function() {
            self.computeCappingValues(campaign_capping_attrs);
            return false;
        });

        self.strategyCappingObserver = ko.computed(function() {
            self.computeCappingValues(strategy_capping_attrs);
            return false;
        });

        self.creativeCappingObserver = ko.computed(function() {
            self.computeCappingValues(creative_capping_attrs);
            return false;
        });

        // VALIDATION LOGIC
        self.errorOverall = ko.observable(false);
        self.errorBudget = ko.observable(false);
        self.errorConversion = ko.observable(false);
        self.errorCapping = ko.observable(false);

        self.errorMessages = ko.observableArray();

        self.fieldsNameMapping = {
            name: 'Campaign name',
            start: 'Start date',
            start_hour: 'Start hour',
            end: 'End date',
            end_hour: 'End hour',
            default_landing_page_url: 'Default landing page',
            budget_total: 'Total budget',
            conversion_name: 'Conversion name',
            conversion_value: 'Conversion value',
            cap_campaign_presented: 'Campaign capping',
            cap_strategy_presented: 'Strategy capping',
            cap_creative_presented: 'Creative capping'
        };

        self.fieldsStepMapping = {
            name: 'errorOverall',
            start: 'errorOverall',
            start_hour: 'errorOverall',
            end: 'errorOverall',
            end_hour: 'errorOverall',
            default_landing_page_url: 'errorOverall',
            budget_total: 'errorBudget',
            conversion_name: 'errorConversion',
            conversion_value: 'errorConversion',
            cap_campaign_presented: 'errorCapping',
            cap_strategy_presented: 'errorCapping',
            cap_creative_presented: 'errorCapping'
        };

        self.validate = function() {
            if (self.is_valid()) {
                return true;
            }

            var fieldMapping = self.fieldsNameMapping,
                stepMapping = self.fieldsStepMapping,
                message = '';

            self.errorMessages([]);
            self.clearStepsErrors();

            for (var field in self.validation) {
                if (!self.validation[field].error()) {
                    continue;
                }
                message = self.validation[field].errorMsg();
                self.errorMessages.push(fieldMapping[field] + ': ' + message);
                self[stepMapping[field]](true);

            }
            return false;
        };

        self.displayBackendErrors = function(json) {
            var mapping = self.fieldsNameMapping,
                stepMapping = self.fieldsStepMapping,
                message = '';

            self.errorMessages([]);

            for (field in json.campaign) {
                message = mapping[field] + ': ' + json.campaign[field][0];
                self[stepMapping[field]](true);
                self.errorMessages.push(message);
            }
        };

        self.clearStepsErrors = function() {
            self.errorOverall(false);
            self.errorBudget(false);
            self.errorConversion(false);
            self.errorCapping(false);
        };

        self.landingPageValidation = ko.computed(function() {
            var landingPage = self.fields().default_landing_page_url();
        });

        // Go to selected step
        self.visitStep = function(step) {
            // step: overall, budget, capping
            self.step(stepName[step]);
            var step_text = '';
            if (step !== 'overall') {
                step_text = '_' + step;
            }
            if (self.mode() === modeName.newCampaign) {
                route = router.path['new_campaign' + step_text]();
            } else {
                route = router.path['edit_campaign' + step_text]({
                    campaignName: self.fields().slug()
                });
            }
            router.routeTo(route);
        };

        self.getStepFromHash = function() {
            var stepName = hasher.getHash().split('/').pop();
            self.step(stepName);
        };

        self.removeCampaign = function() {
            notifications.confirmDialog(
                'Warning!',
                'Are you sure to remove this campaign?',
                function() {
                    return self.fields.Delete(self.fields().resource_uri())
                        .done(function() {
                            router.routeTo(router.path.campaigns());
                            notifications.show('Campaign was removed.', 2);
                        });
                }
            );
        };

        self.clearCampaign = function() {
            router.routeTo(router.path.campaigns(), function() {
                self.reset();
            });
        };

        self.removeStrategy = function(strategy, event) {
            // Tell the backend to remove a strategy, then delete that strategy
            // entry from Campaign.
            var url, promise;
            url = Urls.api_dispatch_detail('strategy', strategy.slug());
            event.stopPropagation();
            notifications.confirmDialog(
                'Warning!',
                'Are you sure to remove this strategy?',
                function() {
                    promise = $.ajax(url, {type: 'delete'}).then(
                        function ok() {
                            self.fields().strategies.remove(strategy);
                        },
                        function error() {
                            notifications.show('Error removing strategy.', 2);
                        }
                    );
          
                    return promise;
                }
            );
        };

        self.loadData = function(url, callback) {
            self.fields.Get(url, function() {
                if (_.isFunction(callback)) {
                    callback();
                }
            });
        };

        self.submit = function() {
            var isValid = self.validate(),
                errorMsg = self.errorMessages,
                newCampaign =
                    self.mode() === modeName.newCampaign ? true : false,
                text = '',
                url = '',
                method;

            if (newCampaign) {
                method = 'Post';
                url = Urls.api_dispatch_list('campaign');
                text = 'New campaign added succesfully!';
            } else {
                method = 'Put';
                url = self.fields().resource_uri();
                text = 'Campaign updated';
            }

            if (!isValid) {
                notifications.showModal(
                    'Error!', ko.unwrap(errorMsg)
                );
                return;
            }

            // function for pushing data on server
            var save = self.fields[method](url);

            save.done(function() {
                notifications.show(text, 2);
                if (newCampaign) {
                    router.routeTo(self.url(), self.reset());
                    return;
                }
                router.routeTo(self.url());
            }).fail(function(response) {
                var json = $.parseJSON(response.responseText);
                self.showApiErrors(json, 'campaign');
                self.displayBackendErrors(json);
                notifications.showModal('Error!',
                                        ko.unwrap(errorMsg));
            });

        };
        
        self.adxopen = function() {
        	window.open("http://www.google.com/dfa")
        };

        self.reset = function() {
            /* Reseting form
             * (filling campaignVM with default values)
             */
            var cleanCampaign = new campaignVM();

            for (p in cleanCampaign.fields()) {
                self.fields()[p](cleanCampaign.fields()[p]());
            }

            // unfortunately, not all fields should be updated :(
            self.fields().cap_campaign_selected(false);
            self.fields().cap_strategy_selected(false);
            self.fields().cap_creative_selected(false);
            self.fields().cap_campaign_presented('0');
            self.fields().cap_strategy_presented('0');
            self.fields().cap_creative_presented('0');
            self.fields().default_landing_page_url('');

        };

        self.activeToggle = function() {
            var newState = ! self.fields().paused(),
                slug = self.fields().slug(),
                url = Urls.api_dispatch_detail('campaign', slug);

            self.fields().paused(newState);
            return $.patchObject(url, { paused: newState }).done(function() {
                if (!newState) {
                    notifications.show('Campaign activated', 2);
                } else {
                    notifications.show('Campaign deactivated', 2);
                }
            });
        };

        self.toggleText = ko.computed(function() {
            var isActive = !self.fields().paused();
            return isActive ? 'Deactivate Campaign' : 'Activate Campaign';
        });

    };

    return {
        newCampaignVM: new campaignVM(),
        editedCampaignVM: new campaignVM(),
        router: router
    };

});
