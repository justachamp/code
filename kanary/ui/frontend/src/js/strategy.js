define(['router', 'notifications', 'utils', 'exchange', 'validation',
        'publisher_set', 'audience', 'creative', 'storage',
        'mixins/validation', 'mixins/toggle_state'],
function(router, notifications, utils, exchange, validation,
         publisher_set, audience, creative, storage,
         ValidationMixin, ToggleStateMixin) {

    var data_costs = CONFIG.TARGETING_ADDITIONAL_DATA_COSTS;
    var data_providers = {
        'proximic': 'proximic',
        'peer39': 'peer39',
        'lotame': 'lotame'
    }

    function setViewModel(model, model_data) {
        for (var key in model_data) {
            if (model_data.hasOwnProperty(key) &&
                model.hasOwnProperty(key)) {
                // Write to normal fields and observables but not to computeds.
                if (ko.isWriteableObservable(model_data[key])) {
                    model[key](model_data[key]());
                } else if (!ko.isObservable(model_data[key])) {
                    model[key] = model_data[key];
                }
            }
        }
    };

    function Site(site_data) {
        var self = this;
        self.weight = ko.observable(1);
        self.url = ko.observable('');
        self.custom_variable = ko.observable('');

        self.validation = {
            url: {
                rules: {
                    required: true,
                    customValidator: validation.isUrl
                }
            }
        };

        ValidationMixin.apply(self, arguments);

        if (site_data) {
            setViewModel(self, site_data);
        }
    };

    var AdvertType = {
        'image': 'Image',
        'flash': 'Flash',
        'video': 'Video'
    }

    function Advert(advert_data) { 
        var self = this;

        self.advert_id = ko.observable(0);
        //self.strategy = ko.observable('');
        self.creative_id = ko.observable(0);
        self.creative_name = ko.observable('');
        self.creative_path = ko.observable('');
        self.creative_type = ko.observable('');
        self.creative_destination = ko.observable('');
        
        self.isCreativeDestination = function(type) { 
          return type === self.creative_destination();
        };
      
        self.creative_fb_title = ko.observable('');
        self.creative_fb_body = ko.observable('');
        
        self.creative_fb_brand_page_access = ko.observable('');
        
        self.landing_page_url = ko.observable('');
        self.custom_variable = ko.observable('');
        self.bid_type = ko.observable('');
        self.bid_custom = ko.observable(0);
        self.bid_day_parting = ko.observableArray();
        self.is_deleted = ko.observable(false);
        self.state = {
            audited: ko.observable(false),
            pending: ko.observable(true),
            blocked: ko.observable(false),
            rejected: ko.observable(false),
            expired: ko.observable(false)
        };

        // Only one at time can be non-blank. We treat input containing
        // only whitespaces as blank.
        self.js_code = ko.observable('');
        self.custom_pixel = ko.observable('');

        // Indicates that textarea is shown. One textarea can be shown
        // at a time. If a shown textarea is empty, the user can toggle between
        // the textareas by selecting the other one.
        self.js_code_input_shown = ko.observable(false);
        self.custom_pixel_input_shown = ko.observable(false);

        /**
         * Check if the argument is a meaningful string (contains something
         * else than whitespace).
         * @param {String, Object} text - value of an observable bound to
         *                                a textarea
         * @return {boolean} true if the argument is not null and contains
         *                   non-whitespace chars.
         */
        self.is_text_nonblank = function(text) {
            return text !== null && text.trim() !== '';
        };

        // Only one tracking method is allowed
        self.js_code_disabled = ko.computed(function() {
            // Custom js code is disabled for video ads
            return (self.is_text_nonblank(self.custom_pixel())
                    || self.creative_type() == AdvertType.video);
        });

        self.custom_pixel_disabled = ko.computed(function() {
            return self.is_text_nonblank(self.js_code());
        });

        /**
         * Toggle display of js_code textarea if possible.
         */
        self.js_code_click = function() {
            // If tracking method is disabled, do nothing
            if (self.js_code_disabled()) {
                return;
            }
            // If the other textarea is being displayed, hide it.
            self.custom_pixel_input_shown(false);
            // Toggle visibility of this textarea.
            self.js_code_input_shown(!self.js_code_input_shown());
        };

        self.custom_pixel_click = function() {
            if (self.custom_pixel_disabled()) {
                return;
            }
            self.js_code_input_shown(false);
            self.custom_pixel_input_shown(!self.custom_pixel_input_shown());
        };

        /**
         * Depending on textarea state, return proper label for the control.
         * If the textarea is blank and hidden, display 'Add tracking'.
         * It it is non-blank, display 'Show/Hide tracking'.
         * @param {boolean} textarea_shown
         * @param {boolean} textarea_value
         * @return {string} label for the control that toggles textarea
         */
        self.get_textarea_label = function(textarea_shown, textarea_value) {
            if (textarea_shown) {
                return 'Hide tracking';
            }
            if (self.is_text_nonblank(textarea_value)) {
                return 'Show tracking';
            }
            return 'Add tracking';
        };

        self.custom_pixel_label = ko.computed(function() {
            return self.get_textarea_label(
                self.custom_pixel_input_shown(), self.custom_pixel());
        });

        self.js_code_label = ko.computed(function() {
            return self.get_textarea_label(
                self.js_code_input_shown(), self.js_code());
        });

        /**
         * Clear leading and trailing whitespaces from both tracker textareas
         * for saving.
         */
        self.trim_inputs = function() {
            self.custom_pixel((self.custom_pixel() || '') .trim());
            self.js_code((self.js_code() || '').trim());
        };

        self.validation = {
            landing_page_url: {
                rules: {
                    customValidator: validation.isUrlOrEmpty
                }
            },
            custom_pixel: {
                rules: {
                    customValidator: validation.isUrlOrEmpty
                }
            }
        };

        if (advert_data) {
            setViewModel(self, advert_data);
        }

        ValidationMixin.apply(self, arguments);

        self.addCreativeFromUpload = function(responseJSON, fileName) {
            var new_creative = new creative.Creative();
            new_creative.setImageFromqqUploader(responseJSON, fileName);
            self.receiveFromTray(new_creative);
        };

        /**
        Method receives creative name and id from tray

        NOTE: until pontillo gets removed from strategy,
        please, use here this instead of self. That's because this method gets
        copied into pontillo's created Advert object
         */
        self.receiveFromTray = function(creative) {
            this.creative_id(creative.fields.id());
            this.creative_name(creative.fields.name());
            this.creative_path(creative.fields.api_data());
            this.creative_type(creative.fields.type());
            this.creative_destination(creative.fields.destination());
            this.creative_fb_title(creative.fields.fb_title);
            this.creative_fb_body(creative.fields.fb_body);
            
            if (creative.fb_brand_page_access) {
                this.creative_fb_brand_page_access(creative.fb_brand_page_access());
            }

            if (this.creative_type() == AdvertType.video) {
                // Custom js code is disabled for video ads and should be cleared
                this.js_code(null);
                this.js_code_input_shown(false);
            }
        };

    };


    /*
     * Basic bid period model used in strategy.
     */
    function BidPeriod(data) {
        var self = this;

        self.from = ko.observable(data.from);
        self.to = ko.observable(data.to);

        self.timerange = ko.computed(function() {
            return self.from() + '-' + self.to();
        });
    };


    /*
     * Extended bid period for Advert.
     */
    function AdvertBidPeriod(data) {
        var self = this;

        BidPeriod.apply(self, arguments);

        self.bid_custom = ko.observable(data.bid_custom);
    };


    function strategyVM() {

        var self = this,
            defaultType = 'Web';

        self.status = ko.observable('adding');

        // used during editing to keep validation rules from applying
        // until they got copied into landing_sites and creatives collections
        // created by pontillo
        self.site_validation_ready = ko.observable(true);
        self.campaign_slug = ko.observable('');
        self.strategy_slug = ko.observable('');

        var fields = function() {
            var self = this;

            self.id = ko.observable(0);
            self.campaign = ko.observable(0);
            self.campaign_slug = ko.observable('');
            self.name = ko.observable('Untitled strategy');
            self.type = ko.observable(defaultType);
            self.paused = ko.observable(false);
            self.budget_total = ko.observable(null);
            self.budget_spent_with_commission = ko.observable(0);
            self.budget_daily = ko.observable(null);
            self.budget_daily_spent = ko.observable(0);
            self.budget_bid_CPM = ko.observable(null);

            // To avoid complicating bidder tests, default for this field
            // is False in model, True only in frontend
            self.distributed_evenly = ko.observable(true);

            self.is_automatically_bidded = ko.observable(false);
            self.optimized_metric = ko.observable(null);
            self.capping_total = ko.observable(null);
            self.capping_day = ko.observable(null);
            self.capping_total_spent = ko.observable(0);
            self.capping_day_spent = ko.observable(0);
            self.landing_sites = ko.observableArray();
            self.adverts = ko.observableArray();
            self.utm_tags = ko.observable(false);
            self.day_parted = ko.observable(false);
            self.bidding_periods = ko.observableArray();
            self.bid_on_unknown_users = ko.observable(false);

            // targeting
            var TARGETING_FIELDS = [
                    'Locations',
                    'Devices',
                    'Os',
                    'Carriers',
                    'AgeGroups',
                    'GenderGroups',
                    'Audiences',
                    'Content',
                    'SafetyLevel',
                    'ProximicMaturityRating',
                    'SafetyLevel',
                    'ProximicLanguage',
                    'ProximicPageQuality',
                    'ProximicPageNoticeability',
                    'ProximicPagePlacement',
                    'ProximicContextual',
                    'PeerContextualSegment',
                    'PeerPageQuality',
                    'PeerLanguage',
                    'PeerBrandProtection',
                    'LotameDemographic',
                    'LotameAdvancedDemographic',
                    'LotameBehavioralInterest',
                    'LotameInfluencers',
                    'LotameOffline'

                ],
                TARGETING_SECTIONS = ['Include', 'Exclude'];

            ko.utils.arrayForEach(TARGETING_FIELDS, function(field) {
                ko.utils.arrayForEach(TARGETING_SECTIONS, function(section) {
                     self['targeting' + section + field] = ko.observableArray();
                });
            });

            // Publishers
            self.publisherset = ko.observable(null);
        };
      
        self.isStrategyType = function(type) { 
            return type === self.fields().type();
        };

        // API wrapper
        self.fields = new ko.pontillo.rest.entity(new fields());
        self.fields.newEntity();

        self.toggle_is_automatically_bidded = function() {
            var isEnabled = ! self.fields().is_automatically_bidded(),
                optimized_metric = self.fields().optimized_metric();

            self.fields().is_automatically_bidded(isEnabled);

            if (isEnabled && _.isNull(optimized_metric)) {
                var firstMetric = self.optimizedMetrics[0].short_name;
                self.fields().optimized_metric(firstMetric);
            } else if (! isEnabled) {
                self.fields().optimized_metric(null);
            }
        };

        self.toggle_optimized_metric = function(metric) {
            self.fields().optimized_metric(metric);
        };

        self.validation = {
            name: {
                rules: {
                    required: true
                }
            },
            budget_total: {
                rules: {
                    required: true,
                    customValidator: budgetTotalValidator
                }
            },
            budget_daily: {
                rules: {
                    customValidator: budgetLimitValidator
                }
            },
            budget_bid_CPM: {
                rules: {
                    customValidator: budgetBidValidator
                }
            },
            capping_total: {
                rules: {
                    customValidator: validation.positiveIntegerCheck
                }
            },
            capping_day: {
                rules: {
                    customValidator: validation.positiveIntegerCheck
                }
            }
        };

        ValidationMixin.apply(self, arguments);
        ToggleStateMixin.apply(self, arguments);

        self.inventory = ko.computed(function() {
            var translations = {
                Mobile: 'app',
                Web: 'site',
                Facebook: 'fb'
            };
            return translations[self.fields().type()];
        });
        
        self.isExistRejectedFbPage = ko.computed(function() {
            var bad_creatives = _.filter(self.fields().adverts(), 
                           function(adv){ if(adv.creative_fb_brand_page_access){ return (adv.creative_fb_brand_page_access() == 'rejected')} });  
            return (bad_creatives.length>0)?true:false;
        });

        // Strategy partials
        self.partials = {
            loaded: $.Deferred(),
            publishers: null
        };

        /** Clear publisher set after strategy type is changed */
        self.fields().type.subscribe(function() {
            var setId = self.fields().publisherset;
            setId(null);
        });

        self.partials.reset = function() {

            var partials = self.partials;
            var inventory = self.inventory;
            var setId = self.fields().publisherset;

            publisher_set.create(setId, inventory).done(
                function(publisherSet) {
                    partials.publishers = publisherSet;
                    partials.loaded.resolve();
            });
        };

        self.partials.get = function(name) {
            /**
            Return partial object if it is initialized, else null
            */
            return self.partials[name] || null;
        };

        self.partials.checkUnsaved = function() {
            var deferred = $.Deferred();
            var publishers = self.partials.get('publishers');
            if (_.isNull(publishers)) {
                // Partial hasn't been initialized yet
                return deferred.resolve();
            }
            var selectedTab = publishers.selectedPublishers;
            if (selectedTab.hasUnsavedChanges()) {
                notifications.confirmDialog(
                    'Warning',
                    'There are unsaved changes in publisher set.<br/>' +
                    'Do you want to continue?',
                    deferred.resolve,
                    deferred.reject
                );
            } else {
                deferred.resolve();
            }
            return deferred.promise();
        };

        // Overall Information section
        self.campaignTotalBudget = ko.observable(0);
        self.campaignSpentBudget = ko.observable(0);
        self.campaignBudgetLeft = ko.computed(function() {
            var totalBudget = self.campaignTotalBudget(),
                spentBudget = self.campaignSpentBudget();

            return totalBudget - spentBudget;
        });

        self.campaignTotalBudgetFormatted = ko.computed(function() {
            return utils.formatBudget(self.campaignTotalBudget());
        });

        self.campaignBudgetLeftFormatted = ko.computed(function() {
            return utils.formatBudget(self.campaignBudgetLeft());
        });

        self.campaignBudgetPercentage = ko.computed(function() {
            var totalBudget = self.campaignTotalBudget(),
                leftBudget = self.campaignBudgetLeft();

            return parseInt((leftBudget / totalBudget) * 100, 10);
        });
        
        self.strategyTypes = ['Web', 'Mobile', 'Facebook'];

        self.optimizedMetrics = [
            {short_name: 'CPC', full: 'Cost per click'},
            {short_name: 'ROI', full: 'Return on investment'},
            {short_name: 'CPA', full: 'Cost per action'},
            {short_name: 'CTR', full: 'Click-through rate'}
        ];

        self.sum_of_weights = ko.computed(function() {

            var sites = self.fields().landing_sites();
            var weight_total = 0;

            ko.utils.arrayForEach(sites, function(site) {
                weight_total += parseInt(site.weight(), 10) || 0;
            });

        }, self);

        self.generateTrafficPercent = function(weight) {
            var value = 100 * (weight() / self.sum_of_weights());
            if (self.fields().landing_sites().length <= 1) {
                value = 100;
            }
            return (Math.round(value) || 0) + '%';
        };

        self.addLandingPage = function() {
            var site = ko.mapping.fromJS(new Site());
            self.fields().landing_sites.push(site);
        };

        self.removeLandingPage = function(landingPage) {
            self.fields().landing_sites.remove(landingPage);
        };

        // Creatives & Biding section
        // ####################################################
        self.addAdvert = function() {
            var advert = ko.mapping.fromJS(new Advert());
            if (self.isStrategyType('Facebook')) {
              advert.creative_destination('facebook_sidebar'); 
            }

            var index = self.fields().adverts.push(advert);

            // for each period add day parting
            var periods = self.fields().bidding_periods();
            ko.utils.arrayForEach(periods, function(period) {
                var bid_period = new AdvertBidPeriod({
                    from: period.from(),
                    to: period.to(),
                    bid_custom: self.fields().budget_bid_CPM()
                });
                self.fields().adverts()[index - 1]
                             .bid_day_parting.push(bid_period);
            });
        };

        self.toggleDayParting = function() {

            var bidding_periods = self.fields().bidding_periods,
                adverts = self.fields().adverts();

            // when day parting is enabled, set select on day parting
            if (self.fields().day_parted()) {
                ko.utils.arrayForEach(adverts, function(item) {
                    item.bid_type('day_parting');
                });
                return false;
            }

            // if day parting is not enabled reset all day parting related
            // values in viewmodel
            bidding_periods([]);
            ko.utils.arrayForEach(adverts, function(item) {
                item.bid_day_parting([]);
                item.bid_type('default');
            });
        };

        self.removeCreative = function(creative) {
            self.fields().adverts.remove(creative);
        };

        self.removeBiddingPeriods = function(period) {
            var bidding_periods = self.fields().bidding_periods,
                adverts = self.fields().adverts();

            bidding_periods.remove(period);

            ko.utils.arrayForEach(adverts, function(creative) {
                var periods = creative.bid_day_parting;

                periods.remove(function(item) {
                    return item.timerange() === period.timerange();
                });

                // when last period was removed
                if (periods().length === 0) {
                   creative.bid_type('default');
                }
            });
        };

        // Bidding (time fields)
        self.isDayPartingEnabled = ko.observable(false);
        self.base_time_start = ko.observable('08:00');
        self.base_time_end = ko.observable('10:30');
        self.bid_period_from = ko.observable('08:00');
        self.bid_period_to = ko.observable('10:30');

        self.defaultBidText = function() {
            var text = 'Default CPM bid';

            if (self.fields().budget_bid_CPM()) {
                text += ' ($' + self.fields().budget_bid_CPM() + ')';
            }

            return text;
        };

        self.addBidDayParting = function(data, event) {

            var from = self.bid_period_from(),
                to = self.bid_period_to();

            var new_period = new BidPeriod({from: from, to: to});

            // If such period already exists show error modal
            if (_.find(self.fields().bidding_periods(), function(period) {
                return period.timerange() === new_period.timerange();
            })) {
                notifications.showModal(
                    'Error!',
                    'You cannot add two the same bidding periods.'
                );
                return;
            }

            // add day parting to strategy
            self.fields().bidding_periods.push(new_period);

            // add day parting to all adverts
            var adverts = self.fields().adverts();
            ko.utils.arrayForEach(adverts, function(item) {
                item.bid_day_parting.push(new AdvertBidPeriod({
                    from: from,
                    to: to,
                    bid_custom: self.fields().budget_bid_CPM()
                }));
            });
        };

        // Computed attributes
        // ####################################################

        self.get_spent_percent = function(spent, total) {
            var value = (spent * 100) / total;
            value = isNaN(value) ? 0 : Math.round(value);
            if (value >= 100) {
                value = 100;
            }
            return value;
        };

        self.budget_spent_and_commission = ko.computed(function() {
            return parseFloat(
                self.fields().budget_spent_with_commission(), 10
            ).toFixed(2);
        });

        self.budget_daily_spent_percent = ko.computed(function() {
           return self.get_spent_percent(self.fields().budget_daily_spent(),
                                       self.fields().budget_daily());
        });

        self.budget_spent_percent = ko.computed(function() {
            var spent = self.budget_spent_and_commission(),
                total = self.fields().budget_total();
          return self.get_spent_percent(spent, total);
        });

        self.capping_total_spent_percent = ko.computed(function() {
            var spent = self.fields().capping_total_spent(),
                total = self.fields().capping_total();
          return self.get_spent_percent(spent, total);
        });
        self.capping_day_spent_percent = ko.computed(function() {
            var spent = self.fields().capping_day_spent(),
                total = self.fields().capping_day();
            return self.get_spent_percent(spent, total);
        });
        self.getCampaignTotalBudget = ko.computed(function() {
            var self = this;
            if (self.campaign_slug() === '') {
                return;
            }
            var url = Urls.api_dispatch_detail('campaign',
                                               self.campaign_slug());
            $.getJSON(url, function(data) {
                self.fields().campaign(data.id);
                self.campaignTotalBudget(data.budget_total);
            });
        }, self);

        self.getCampaignBudget = function() {
            var self = this,
                dfd = $.Deferred();

            if (self.campaign_slug() === '') {
                return dfd.reject();
            }

            var url = Urls.api_dispatch_detail('campaign',
                                               self.campaign_slug());

            $.getJSON(url, function(data) {
                self.fields().campaign(data.id);
                self.campaignTotalBudget(data.budget_total);
                self.campaignSpentBudget(
                    parseFloat(data.budget_spent_with_commission, 10)
                );
                dfd.resolve();
            });
            return dfd.promise();
        };

        var SLIDER_PRECISION = 1000;
        self.slider = ko.computed({
            read: function() {
                return parseInt(
                    (self.fields().budget_total() * SLIDER_PRECISION) /
                    self.campaignTotalBudget()
                );
            },
            write: function(value) {
                var value = parseInt(value);
                if (isNaN(value)) {
                    return;
                }
                var budget = self.campaignTotalBudget() *
                                (value / SLIDER_PRECISION);
                self.fields().budget_total(budget);
            },
            owner: this
        });

        self.sliderPercent = ko.computed(function() {
            var value = parseInt(self.slider() / 10, 10);
            value = isNaN(value) ? 0 : value;
            if (value >= 100) {
                value = 100;
            }
            return value;
        }, self);

        self.budgetTotalDifference = ko.computed(function() {
            var campaignTotal = self.campaignTotalBudget();
            return campaignTotal - self.fields().budget_total();
        }, self);

        self.sliderPercentReversed = ko.computed(function() {
            return 100 - self.sliderPercent();
        }, self);

        // Sidebar
        // ####################################################

        self.linkTo = function(path) {
            if (self.status() === 'adding')
                router.routeTo(router.path['new_' + path](
                    {'campaignName': self.campaign_slug()
                }));
            else
                router.routeTo(router.path['edit_' + path]({
                    'campaignName': self.campaign_slug(),
                    'strategyName': self.strategy_slug()
                }));
            return false;
        };

        self.step = ko.observable('newStrategy');

        self.getStep = function() {
            self.step(hasher.getHash().split('/').pop());
        };
        self.leaveStep = function(step) {
            if (step == 'publishers') {
                return self.partials.checkUnsaved();
            } else {
                return $.Deferred().resolve();
            }
        };
        self.visitStep = function(step) {
            var current = self.step();
            self.leaveStep(current).done(function() {
                self.step(step);
                var step_text = '';
                if (step !== 'newStrategy') {
                    step_text = '_' + step;
                }
                if (self.status() === 'adding') {
                    route = router.path['new_strategy' + step_text]({
                        campaignName: self.campaign_slug()
                    });
                } else {
                    route = router.path['edit_strategy' + step_text]({
                        campaignName: self.campaign_slug(),
                        strategyName: self.strategy_slug()
                    });
                }
                router.routeTo(route);
            });

        };

        // Validation logic
        self.errorOverall = ko.observable(false);
        self.errorTargeting = ko.observable(false);
        self.errorLandingPages = ko.observable(false);
        self.errorPublishers = ko.observable(false);
        self.errorCreatives = ko.observable(false);
        self.errorBidding = ko.observable(false);

        self.errorMessages = ko.observableArray();

        self.fieldsNameMapping = {
            budget_total: {name: 'Total strategy budget', error: self.errorOverall},
            budget_daily: {name: 'Strategy daily budget', error: self.errorOverall},
            name: {name: 'Strategy name', error: self.errorOverall},
            capping_total: {name: 'Total impression limit', error: self.errorOverall},
            capping_day: {name: 'Daily impression limit', error: self.errorOverall},
            audiences: {name: 'Audience', error: self.errorTargeting},
            location: {name: 'Location', error: self.errorTargeting},
            device: {name: 'Device', error: self.errorTargeting},
            category: {name: 'Category', error: self.errorTargeting},
            os: {name: 'Operating system', error: self.errorTargeting},
            carrier: {name: 'Carrier', error: self.errorTargeting},
            gender: {name: 'Gender', error: self.errorTargeting},
            'age_group': {name: 'Age group', error: self.errorTargeting},
            budget_bid_CPM: {name: 'Default CPM bid', error: self.errorBidding},
            is_automatically_bidded: {name: 'Automatic bid price', error: self.errorBidding},
            adverts_video: {name: 'Video adverts', error: self.errorCreatives},
            adverts: {name: 'Adverts', error: self.errorCreatives},

            'proximic_safety_level': {name: 'Proximic safety level', error: self.errorTargeting},
            'proximic_maturity_rating': {name: 'Proximic maturity rating', error: self.errorTargeting},
            'proximic_page_quality': {name: 'Proximic page quality', error: self.errorTargeting},
            'proximic_page_placement': {name: 'Proximic page placement', error: self.errorTargeting},
            'proximic_contextual': {name: 'Proximic contextual', error: self.errorTargeting},
            'proximic_language': {name: 'Proximic language', error: self.errorTargeting},
            'proximic_page_noticeability': {name: 'Proximic page noticeability', error: self.errorTargeting},

            'lotame_demographic': {name: 'Lotame demographic', error: self.errorTargeting},
            'lotame_influencers': {name: 'Lotame influencers', error: self.errorTargeting},
            'lotame_advanced_demographic': {name: 'Lotame advanced demographic', error: self.errorTargeting},
            'lotame_offline': {name: 'Lotame offline', error: self.errorTargeting},
            'lotame_behavioral_interest': {name: 'Lotame behavioral interest', error: self.errorTargeting},

            'peer_brand_protection': {name: 'Peer brand protection', error: self.errorTargeting},
            'peer_contextual': {name: 'Peer contextual', error: self.errorTargeting},
            'peer_page_quality': {name: 'Peer page quality', error: self.errorTargeting},
            'peer_page_language': {name: 'Peer page language', error: self.errorTargeting},

            // Default error message for not mapped fields
            'default': {name: 'Error', error: self.errorOverall}
        };

        self.checkOverall = function() {
            var isValid = self.is_valid(),
                mapping = self.fieldsNameMapping,
                validationScheme = self.validation,
                message = '';

            if (isValid) {
                self.clearStepsErrors();
                return false;
            }

            for (field in validationScheme) {
                if (!validationScheme[field].error()) {
                    continue;
                }
                message = validationScheme[field].errorMsg();
                field_name = mapping[field].name;
                section_error = mapping[field].error;
                self.errorMessages.push(field_name + ': ' + message);
                section_error(true);
            }
            return true;
        };

        self.checkLandingPages = function() {
            var landingSites = self.fields().landing_sites,
                message = 'Landing pages: ';

            // Check if urls are not empty and in correct format
            var invalidFields = _.filter(landingSites(), function(item) {
                return item.is_valid() === false;
            });

            if (invalidFields.length > 0) {
                message += 'some landing pages are in incorrect format.';
                self.errorMessages.push(message);
                self.errorLandingPages(true);
                return true;
            }
          
            if (self.isStrategyType('Facebook')&&self.fields().landing_sites().length>1) {
                message += 'Facebook creative can have only one landing page.';
                self.errorMessages.push(message);
                self.errorLandingPages(true);
                return true;
            }

            self.errorLandingPages(false);
            return false;
        };

        self.checkPublishers = function() {
            var publishers = self.partials.get('publishers');
            if (_.isNull(publishers)) {
                // Partial hasn't been initialized yet
                self.errorPublishers(false);
                return false;
            }
            var publisherType = publishers.type;
            var strategyInventory = self.inventory();
            var publishersInventory = publisherType.inventory();

            if (strategyInventory != publishersInventory) {
                var message = 'Publishers: You have chosen a ' +
                    publishersInventory + ' publisher set to ' +
                    self.fields().type() + ' strategy';
                self.errorMessages.push(message);
                self.errorPublishers(true);
                return true;
            }
            self.errorPublishers(false);
            return false;
        };

        self.checkCreatives = function() {
            var adverts = self.fields().adverts,
                messageEmpty = 'Creatives: at least one creative is required.',
                messageUrl = 'Creatives: some urls have incorrect format';

            if (adverts().length === 0) {
                    self.errorMessages.push(messageEmpty);
                    self.errorCreatives(true);
                    return true;
            }

            // when widgets are on we find if there is any which is
            // not empty, and has url in correct format
            var errors = _.map(adverts(), function(item) {
                return !item.is_valid();
            });

            // no errors array, nothing to has been added
            if (!errors.length) {
                self.errorMessages.push(messageEmpty);
                self.errorCreatives(true);
                return true;
            }

            // filter all errors
            if (_.reject(errors, function(item) { return !item}).length) {
                self.errorMessages.push(messageUrl);
                self.errorCreatives(true);
                return true;
            }

            self.errorCreatives(false);
            return false;
        };

        self.checkBidding = function() {
            var periods = self.fields().bidding_periods,
                has_error = false,
                areOverlapping = false,
                isPeriodOrderInvalid = false,
                isMinutePartInvalid = false,

            arePeriodsOverlapping = utils.arePeriodsOverlapping(periods);
            isPeriodOrderInvalid = utils.isPeriodOrderInvalid(periods);
            isMinutePartInvalid = utils.isMinutePartInvalid(periods);

            if (arePeriodsOverlapping) {
                var msg = "Bidding: bidding periods can't overlap each other.";
                self.errorMessages.push(msg);
                has_error = true;
            }

            if (isPeriodOrderInvalid) {
                var msg = "Bidding: period start can't be later than end.";
                self.errorMessages.push(msg);
                has_error = true;
            }

            if (isMinutePartInvalid) {
                var msg = 'Bidding: Minutes must be multiples of ' +
                ' quarter of an hour.';
                self.errorMessages.push(msg);
                has_error = true;
            }

            if (has_error == true) {
                self.errorBidding(has_error);
            }
            return has_error;
        };

        self.appendErrorMessages = function(json) {
            self.errorMessages([]);

            for (field in json.strategy) {
                var mapping = self.fieldsNameMapping[field] || self.fieldsNameMapping['default'];
                var sectionHasError = mapping.error || self.errorOverall;
                sectionHasError(true);
                var message = mapping.name + ': ' + json.strategy[field];
                self.errorMessages.push(message);
            }
        };

        self.validate = function() {

            self.errorMessages([]);

            var overallErrors = self.checkOverall(),
                landingPageErrors = self.checkLandingPages(),
                creativeErrors = self.checkCreatives(),
                publisherErrors = self.checkPublishers(),
                biddingErrors = self.checkBidding();

            if (overallErrors || landingPageErrors || creativeErrors ||
                publisherErrors || biddingErrors) {
                return true;
            }

            return false;
        };

        function budgetTotalValidator(value) {
            var strategyBudget = parseFloat(self.fields().budget_total()),
                campaignBudget = parseFloat(self.campaignTotalBudget());

            if (strategyBudget > campaignBudget) {
                return 'Strategy budget cannot be larger ' +
                       'than campaign budget.';
            }
        };

        function budgetLimitValidator(value) {
            var strategyBudget = parseFloat(self.fields().budget_total()),
                dailyBudget = parseFloat(self.fields().budget_daily());

            if (dailyBudget > strategyBudget) {
                return 'Daily budget cannot be larger ' +
                       'than strategy budget.';
            }
        };

        function budgetBidValidator(value) {
            var is_automatically_bidded = self.fields().is_automatically_bidded(),
                bid = self.fields().budget_bid_CPM();

            if (!is_automatically_bidded && (_.isNull(bid) || _.isEmpty(bid))) {
                return 'This field is required.';
            }
        };


        // Applying validation to self.fields
        // ####################################################

        self.pickAndExtend = function(baseObj, fields, targetObj) {
            var pickedFields = _.pick(baseObj, fields);
            _.each(targetObj, function(target) {
                _.extend(target, pickedFields);
            });
        };

        self.applySitesMapping = function() {
            var landing_sites = self.fields().landing_sites(),
                updated = [];

            ko.utils.arrayForEach(landing_sites, function(site) {
                updated.push(new Site(site));
            });

            self.fields().landing_sites(updated);
        };

        self.applyAdvertsMapping = function() {
            var adverts = self.fields().adverts(),
                mapped = [];

            ko.utils.arrayForEach(adverts, function(advert) {
                var mapped_advert = new Advert(advert),
                    advert_periods = mapped_advert.bid_day_parting(),
                    mapped_periods = [];

                ko.utils.arrayForEach(advert_periods, function(period) {
                    var mapped_period = new AdvertBidPeriod({
                        from: period.from(),
                        to: period.to(),
                        bid_custom: period.bid_custom()
                    });
                    mapped_periods.push(mapped_period);
                });

                mapped_advert.bid_day_parting(mapped_periods);
                mapped.push(mapped_advert);
            });

            self.fields().adverts(mapped);
        };

        self.applyBidPeriodsMapping = function() {
            var periods = self.fields().bidding_periods(),
                mapped = [];

            ko.utils.arrayForEach(periods, function(period) {
                var mapped_period = new BidPeriod({
                    from: period.from(),
                    to: period.to()
                });
                mapped.push(mapped_period);
            });

            self.fields().bidding_periods(mapped);
        };

        /*
         * Maps JSON fetched from server to our custom models
         */
        self.applyCustomMapping = function() {
            self.applySitesMapping();
            self.applyAdvertsMapping();
            self.applyBidPeriodsMapping();
            self.site_validation_ready(true);
        };

        // Save / Delete / Reset
        // ####################################################

        self.save = function() {
            ko.utils.arrayForEach(self.fields().adverts(), function(advert) {
                advert.trim_inputs();
            });
            var errors = self.validate(),
                newStrategy = (self.status() === 'adding'),
                method = undefined,
                text = '',
                url = '';

            if (errors) {
                notifications.showModal(
                    'Error!',
                    ko.unwrap(self.errorMessages)
                );
                return false;
            }

            if (newStrategy) {
                method = 'Post';
                url = Urls.api_dispatch_list('strategy');
                text = 'Strategy added succesfully!';
            } else {
                var strategy_id = self.fields().id();
                method = 'Put';
                text = 'Strategy updated';
                url = Urls.api_dispatch_detail_id('strategy', strategy_id);
            }

            var save = self.fields[method](url);

            // turn off validation
            self.site_validation_ready(false);

            save.done(function() {
                var redirectUrl = router.path.strategy({
                    campaignName: self.campaign_slug(),
                    strategyName: self.fields().slug()
                });
                router.routeTo(redirectUrl);
                notifications.show(text, 2);
            }).fail(function(response) {
                var json = $.parseJSON(response.responseText);
                // turn on validation
                self.applyCustomMapping();
                self.showApiErrors(json, 'strategy');
                self.appendErrorMessages(json);
                notifications.showModal(
                    'Error!',
                    ko.unwrap(self.errorMessages)
                );
            });
        };

        self.deleteStrategy = function(strategy) {
            var url = Urls.api_dispatch_detail('strategy', strategy.slug());
            return self.fields.Delete(url).done(function() {
                var path = router.path.campaign({
                    'campaignName': strategy.campaign_slug()
                });
                router.routeTo(path);
                notifications.show('Strategy was removed', 2);
            });
        };

        self.delete = function(strategy) {

            notifications.confirmDialog(
                'Warning!',
                'Are you sure to remove this strategy?',
                function() { self.deleteStrategy(strategy) }
            );
        };

        self.reset = function() {
            var default_strategy = new strategyVM();
            for (field_name in default_strategy.fields()) {
                var default_val = default_strategy.fields()[field_name]();
                if (self.fields()[field_name] !== undefined) {
                    self.fields()[field_name](default_val);
                }
            }
            self.bid_period_from('08:30');
            self.bid_period_to('10:30');
            self.isDayPartingEnabled(false);
        };

        self.clearStepsErrors = function() {
            self.errorOverall(false);
            self.errorTargeting(false);
            self.errorLandingPages(false);
            self.errorPublishers(false);
            self.errorCreatives(false);
            self.errorBidding(false);
        };

        // targeting
        // ####################################################

        self.targetingWidgets = [{
                name: 'Location',
                type: 'Location',
                'class': 'location',
                template: 'targeting-widget-simple-search',
                api: Urls.api_dispatch_list('targeting/location'),
                include: 'targetingIncludeLocations',
                exclude: 'targetingExcludeLocations'
            }, {
                name: 'Device',
                type: 'Device',
                'class': 'devices',
                template: 'targeting-widget-simple-search',
                api: Urls.api_dispatch_list('targeting/device'),
                include: 'targetingIncludeDevices',
                exclude: 'targetingExcludeDevices'
            }, {
                name: 'Operating system',
                type: 'Os',
                'class': 'os',
                template: 'targeting-widget-simple-search',
                api: Urls.api_dispatch_list('targeting/os'),
                include: 'targetingIncludeOs',
                exclude: 'targetingExcludeOs'
            }, {
                name: 'Carrier',
                type: 'Carrier',
                'class': 'carrier',
                template: 'targeting-widget-simple-search',
                api: Urls.api_dispatch_list('targeting/carrier'),
                include: 'targetingIncludeCarriers',
                exclude: 'targetingExcludeCarriers'
            }, {
                name: 'User profile',
                type: 'UserProfile',
                'class': 'userprofile',
                template: 'targeting-widget-checkbox-groups',
                include: [{
                        name: 'Age Group',
                        rows: 'targetingAgeGroups',
                        data: 'targetingIncludeAgeGroups',
                        type: 'AgeGroup'
                    }, {
                        name: 'Gender',
                        rows: 'targetingGenderGroups',
                        data: 'targetingIncludeGenderGroups',
                        type: 'GenderGroup'
                    }],
                exclude: [{
                        name: 'Age Group',
                        rows: 'targetingAgeGroups',
                        data: 'targetingExcludeAgeGroups',
                        type: 'AgeGroup'
                    }, {
                        name: 'Gender',
                        rows: 'targetingGenderGroups',
                        data: 'targetingExcludeGenderGroups',
                        type: 'GenderGroup'
                    }]
            }, {
                name: 'Audience',
                type: 'Audiences',
                'class': 'audiences',
                template: 'targeting-widget-tray',
                api: Urls.api_dispatch_list('storage/audience'),
                include: 'targetingIncludeAudiences',
                exclude: 'targetingExcludeAudiences'
            }, {
                name: 'Content',
                type: 'Content',
                'class': 'content',
                template: 'targeting-widget-tree',
                include: [{
                   data: 'targetingIncludeContent',
                   rows: 'targetingCategories',
                   type: 'Content'
                }],
                exclude: [{
                    data: 'targetingExcludeContent',
                    rows: 'targetingCategories',
                    type: 'Content'
                }]
            }, {
                name: 'Proximic Brand Protection',
                type: 'ProximicBrandProtection',
                'class': 'quality',
                template: 'targeting-widget-brand-protection',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['brand_protection']
                },
                include: [{
                    name: 'Maturity',
                    data: 'targetingIncludeProximicMaturityRating',
                    rows: 'targetingProximicMaturityRating',
                    type: 'ProximicMaturityRating'
                },{
                    name: 'Safety level',
                    data: 'targetingIncludeSafetyLevel',
                    rows: 'targetingProximicSafetyLevel',
                    type: 'SafetyLevel'
                }],
                exclude: [{
                    name: 'Maturity',
                    data: 'targetingExcludeProximicMaturityRating',
                    rows: 'targetingProximicMaturityRating',
                    type: 'ProximicMaturityRating'
                },{
                    name: 'Safety level',
                    data: 'targetingExcludeSafetyLevel',
                    rows: 'targetingProximicSafetyLevel',
                    type: 'SafetyLevel'
                }]
            }, {
                name: 'Proximic Language',
                type: 'ProximicLanguage',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['language']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeProximicLanguage',
                    rows: 'targetingProximicLanguage',
                    type: 'ProximicLanguage'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeProximicLanguage',
                    rows: 'targetingProximicLanguage',
                    type: 'ProximicLanguage'
                }]
            }, {
                name: 'Proximic Page Quality',
                type: 'ProximicPageQuality',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['page_quality']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeProximicPageQuality',
                    rows: 'targetingProximicPageQuality',
                    type: 'ProximicPageQuality'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeProximicPageQuality',
                    rows: 'targetingProximicPageQuality',
                    type: 'ProximicPageQuality'
                }]
            }, {
                name: 'Proximic Page Noticeability',
                type: 'ProximicPageNoticeability',
                'class': 'quality',
                template: 'targeting-widget-tree',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['page_noticeability']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeProximicPageNoticeability',
                    rows: 'targetingProximicPageNoticeability',
                    type: 'ProximicPageNoticeability'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeProximicPageNoticeability',
                    rows: 'targetingProximicPageNoticeability',
                    type: 'ProximicPageNoticeability'
                }]
            }, {
                name: 'Proximic Page Placement',
                type: 'ProximicPagePlacement',
                'class': 'quality',
                template: 'targeting-widget-tree',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['page_placement']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeProximicPagePlacement',
                    rows: 'targetingProximicPagePlacement',
                    type: 'ProximicPagePlacement'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeProximicPagePlacement',
                    rows: 'targetingProximicPagePlacement',
                    type: 'ProximicPagePlacement'
                }]
            }, {
                name: 'Proximic Contextual Categories',
                type: 'ProximicContextual',
                'class': 'quality',
                template: 'targeting-widget-tree',
                additional_costs: {
                    category: data_providers.proximic,
                    value: data_costs['contextual_categories']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeProximicContextual',
                    rows: 'targetingProximicContextual',
                    type: 'ProximicContextual'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeProximicContextual',
                    rows: 'targetingProximicContextual',
                    type: 'ProximicContextual'
                }]
            }, {
                name: 'Peer 39 Contextual segments',
                type: 'PeerContextual',
                'class': 'quality',
                template: 'targeting-widget-tree',
                additional_costs: {
                    category: data_providers.peer39,
                    value: data_costs['peer39']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludePeerContextualSegment',
                    rows: 'targetingPeerContextualSegments',
                    type: 'PeerContextual'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludePeerContextualSegment',
                    rows: 'targetingPeerContextualSegments',
                    type: 'PeerContextual'
                }]
            }, {
                name: 'Peer 39 Page quality',
                type: 'PeerPageQuality',
                'class': 'quality',
                template: 'targeting-widget-tree',
                additional_costs: {
                    category: data_providers.peer39,
                    value: data_costs['peer39']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludePeerPageQuality',
                    rows: 'targetingPeerPageQuality',
                    type: 'PeerPageQuality'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludePeerPageQuality',
                    rows: 'targetingPeerPageQuality',
                    type: 'PeerPageQuality'
                }]
            }, {
                name: 'Peer39 Language',
                type: 'PeerLanguage',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.peer39,
                    value: data_costs['peer39']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludePeerLanguage',
                    rows: 'targetingPeerLanguage',
                    type: 'PeerLanguage'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludePeerLanguage',
                    rows: 'targetingPeerLanguage',
                    type: 'PeerLanguage'
                }]
            }, {
                name: 'Peer39 Brand protection',
                type: 'PeerBrandProtection',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.peer39,
                    value: data_costs['peer39']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludePeerBrandProtection',
                    rows: 'targetingPeerBrandProtection',
                    type: 'PeerBrandProtection'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludePeerBrandProtection',
                    rows: 'targetingPeerBrandProtection',
                    type: 'PeerBrandProtection'
                }]
            }, {
                name: 'Lotame Demographic',
                type: 'LotameDemographic',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.lotame,
                    value: data_costs['lotame_demographic']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeLotameDemographic',
                    rows: 'targetingLotameDemographic',
                    type: 'LotameDemographic'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeLotameDemographic',
                    rows: 'targetingLotameDemographic',
                    type: 'LotameDemographic'
                }]
            }, {
                name: 'Lotame Advanced demographic',
                type: 'LotameAdvancedDemographic',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.lotame,
                    value: data_costs['lotame_advanced_demographic']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeLotameAdvancedDemographic',
                    rows: 'targetingLotameAdvancedDemographic',
                    type: 'LotameAdvancedDemographic'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeLotameAdvancedDemographic',
                    rows: 'targetingLotameAdvancedDemographic',
                    type: 'LotameAdvancedDemographic'
                }]
            }, {
                name: 'Lotame Behavioral interest',
                type: 'LotameBehavioralInterest',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.lotame,
                    value: data_costs['lotame_behavioral_interest']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeLotameBehavioralInterest',
                    rows: 'targetingLotameBehavioralInterest',
                    type: 'LotameBehavioralInterest'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeLotameBehavioralInterest',
                    rows: 'targetingLotameBehavioralInterest',
                    type: 'LotameBehavioralInterest'
                }]
            }, {
                name: 'Lotame Influencer',
                type: 'LotameInfluencer',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.lotame,
                    value: data_costs['lotame_influencer']
                },
                include: [{
                    name: '',
                    data: 'targetingIncludeLotameInfluencers',
                    rows: 'targetingLotameInfluencer',
                    type: 'LotameInfluencer'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeLotameInfluencers',
                    rows: 'targetingLotameInfluencer',
                    type: 'LotameInfluencer'
                }]
            }, {
                name: 'Lotame Offline',
                type: 'LotameOffline',
                'class': 'quality',
                template: 'targeting-widget-checkbox-groups',
                additional_costs: {
                    category: data_providers.lotame,
                    value: data_costs['lotame_offline']
                },
                /* Custom column width in checkboxes widget */
                columns: 8,
                include: [{
                    name: '',
                    data: 'targetingIncludeLotameOffline',
                    rows: 'targetingLotameOffline',
                    type: 'LotameOffline'
                }],
                exclude: [{
                    name: '',
                    data: 'targetingExcludeLotameOffline',
                    rows: 'targetingLotameOffline',
                    type: 'LotameOffline'
                }]
            }];



        // list of widgets in include section
        self.targetingIncludeWidgets = ko.observableArray();
        // list of widgets in include dropdown
        self.targetingIncludeWidgetsList = ko.observableArray();
        // list of widgets in exclude section
        self.targetingExcludeWidgets = ko.observableArray();
        // list of widgets in include dropdown
        self.targetingExcludeWidgetsList = ko.observableArray();

        // get field from "strategyVM.fields"
        self.getField = function(name) {
            return self.fields()[name];
        };

        // link widget target (or targets) with observable array (or arrays)
        self.connectTargetWithField = function(widget) {
            if (_.isString(widget.target)) {
                // widget with single data source
                widget.target = self.getField(widget.target);
            } else {
                // widget with multiple data sources
                ko.utils.arrayFirst(widget.target, function(item) {
                    if (_.isString(item)) {
                        item.data = self.getField(item.data);
                    }
                });
            }
        };

        // select proper observable array for given checkbox group
        // in given section (include/exclude)
        // eg. input:
        //          widget: User profile (section: include),
        //          type: AgeGroup
        //      output:
        //          targetingIncludeAgeGroups
        self.targetingGetArrayForCheckbox = function(widget, type) {
            var targetArray;
            ko.utils.arrayForEach(widget[widget.section], function(item) {
                if (item.type === type) {
                    targetArray = item.data;
                    return;
                }
            });
            return targetArray;
        };

        // returning initial checkbox state for fancyCheckbox
        self.targetingGetCheckboxState = function(element, widget, type) {
            var targetArray = self.targetingGetArrayForCheckbox(widget, type);
            targetArray = self.getField(targetArray);
            var foundElement = _.find(targetArray(), function(checkbox) {
                return ko.unwrap(checkbox.id) == element.id;
            });
            var isChecked = (foundElement !== undefined);
            return ko.observable(isChecked);
        };

        // Return observable array containing checked elements
        self.targetingGetCheckedElements = function(widget, type) {
            var targetArray = self.targetingGetArrayForCheckbox(widget, type);
            targetArray = self.getField(targetArray);
            return targetArray;
        };

        // get checkbox data (for generating checkbox group) from API
        self.getCheckboxDataFromAPI = function(obsArray, resourceName) {
            obsArray.removeAll();
            var url = Urls.api_dispatch_list('targeting/' + resourceName);
            url += '?limit=0';

            var wait = $.Deferred();
            var defered = $.getJSON(url, function(data) {
                obsArray(_.map(data.objects, function(el) {
                    return {
                        id: el.id,
                        name: el.name,
                        description: el.description
                    };
                }));
            }).complete(wait.resolve);
            return defered;
        };

        self.getTreeDataFromAPI = function(obsArray, resourceName) {
            var url = Urls.api_get_tree(resourceName);
            return $.getJSON(url, function(data) {
                obsArray(data.tree);
            });
        };


        // used as fancyCheckbox onclick action (modify proper observable array)
        self.targetingChangeCheckboxState = function(elem, widget, type) {
            var targetArray = self.targetingGetArrayForCheckbox(widget, type);
            if (_.isString(targetArray)) {
                targetArray = self.getField(targetArray);
            }

            var foundElement = _.find(targetArray(), function(checkbox) {
                return ko.unwrap(checkbox.id) == elem.id;
            });

            if (_.isUndefined(foundElement)) {
                targetArray.push(elem);
            } else {
                targetArray.remove(foundElement);
            }
        };

        // get initial fancyCheckbox state (tree version)
        self.targetingGetTreeCheckboxState = function(elem, widget, type) {
            function isChecked(elem) {
                return self.targetingGetCheckboxState(elem, widget, type);
            }

            var targetArray = self.targetingGetArrayForCheckbox(widget, type);

            if (_.isString(targetArray)) {
                targetArray = self.getField(targetArray);
            }

            var childrenChecked = 0;
            var children = elem.children || [];

            children.forEach(function(child) {
                var isChildChecked = isChecked(child);
                if (isChildChecked()) {
                    childrenChecked += 1;
                }
            });

            var allChildrenChecked = (childrenChecked == children.length);

            var isParentChecked = isChecked(elem);

            if (allChildrenChecked !== isParentChecked()) {
                self.targetingChangeCheckboxState(elem, widget, type);
            }
            return ko.observable(allChildrenChecked);
        };

        // used as fancyCheckbox onclick action (tree version)
        self.targetingChangeTreeCheckboxState = function(elem, widget, type) {
            function isChecked(elem) {
                return self.targetingGetCheckboxState(elem, widget, type);
            }

            var oldState = isChecked(elem);
            var isParentChecked = ! oldState();
            self.targetingChangeCheckboxState(elem, widget, type);

            var children = elem.children || [];

            children.forEach(function(child) {
                var isChildChecked = isChecked(child);
                if (isParentChecked !== isChildChecked()) {
                    self.targetingChangeTreeCheckboxState(child, widget, type);
                }
            });
        };

        // get from API: age groups
        self.targetingAgeGroups = ko.observableArray();
        self.getTargetingAgeGroups = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingAgeGroups,
                'age_group'
            );
        };

        // get from API: genders
        self.targetingGenderGroups = ko.observableArray();
        self.getTargetingGenderGroups = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingGenderGroups,
                'gender'
            );
        };

        // get from API: audiences
        self.targetingAudiences = ko.observableArray();
        self.getTargetingAudiences = function() {
            audience.get().done(function(audiences) {
                self.targetingAudiences(audiences);
            });
        };

        // get from API: content categories
        self.targetingCategories = ko.observableArray();
        self.getTargetingCategories = function() {
            return self.getTreeDataFromAPI(
                self.targetingCategories,
                'categories_tree'
            );
        };

        // get from API: proximic maturity rating
        self.targetingProximicMaturityRating = ko.observableArray();
        self.getTargetingProximicMaturityRating = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingProximicMaturityRating,
                'proximic_maturity_rating'
            );
        };

        // get from API: proximic safety levels
        self.targetingProximicSafetyLevel = ko.observableArray();
        self.getTargetingProximicSafetyLevel = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingProximicSafetyLevel,
                'proximic_safety_level'
            );
        };

        // get from API: proximic languages
        self.targetingProximicLanguage = ko.observableArray();
        self.getTargetingProximicLanguage = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingProximicLanguage,
                'proximic_language'
            );
        };

        // get from API: page quality
        self.targetingProximicPageQuality = ko.observableArray();
        self.getTargetingProximicPageQuality = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingProximicPageQuality,
                'proximic_page_quality'
            );
        };

        // get from API: page noticeability
        self.targetingProximicPageNoticeability = ko.observableArray();
        self.getTargetingProximicPageNoticeability = function() {
            return self.getTreeDataFromAPI(
                self.targetingProximicPageNoticeability,
                'proximic_page_noticeability'
            );
        };

        // get from API: page_placement
        self.targetingProximicPagePlacement = ko.observableArray();
        self.getTargetingProximicPagePlacement = function() {
            return self.getTreeDataFromAPI(
                self.targetingProximicPagePlacement,
                'proximic_page_placement'
            );
        };

        // get from API: contextual categories
        self.targetingProximicContextual = ko.observableArray();
        self.getTargetingProximicContextual = function() {
            return self.getTreeDataFromAPI(
                self.targetingProximicContextual,
                'proximic_contextual'
            );
        };

        self.targetingPeerContextualSegments = ko.observableArray();
        self.getTargetingPeerContextualSegments = function() {
            return self.getTreeDataFromAPI(
                self.targetingPeerContextualSegments,
                'peer_contextual_segments_tree'
            );
        };

        self.targetingPeerPageQuality = ko.observableArray();
        self.getTargetingPeerPageQuality = function() {
            return self.getTreeDataFromAPI(
                self.targetingPeerPageQuality,
                'peer_page_quality_tree'
            );
        };

        self.targetingPeerLanguage = ko.observableArray();
        self.getTargetingPeerLanguage = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingPeerLanguage,
                'peer_language'
            );
        };

        self.targetingPeerLanguage = ko.observableArray();
        self.getTargetingPeerLanguage = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingPeerLanguage,
                'peer_language'
            );
        };

        self.targetingPeerBrandProtection = ko.observableArray();
        self.getTargetingPeerBrandProtection = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingPeerBrandProtection,
                'peer_brand_protection'
            );
        };

        self.targetingLotameDemographic = ko.observableArray()
        self.getTargetingLotameDemographic = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingLotameDemographic,
                'lotame_demographic'
            );
        };

        self.targetingLotameAdvancedDemographic = ko.observableArray()
        self.getTargetingLotameAdvancedDemographic = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingLotameAdvancedDemographic,
                'lotame_advanced_demographic'
            );
        };

        self.targetingLotameBehavioralInterest = ko.observableArray()
        self.getTargetingLotameBehavioralInterest = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingLotameBehavioralInterest,
                'lotame_behavioral_interest'
            );
        };

        self.targetingLotameInfluencer = ko.observableArray()
        self.getTargetingLotameInfluencer = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingLotameInfluencer,
                'lotame_influencers'
            );
        };

        self.targetingLotameOffline = ko.observableArray()
        self.getTargetingLotameOffline = function() {
            return self.getCheckboxDataFromAPI(
                self.targetingLotameOffline,
                'lotame_offline'
            );
        };

        // load all needed data from API and load initial widgets
        self.loadDataFromTargeting = function(deferred) {
            self.targetingIncludeWidgets([]);
            self.targetingExcludeWidgets([]);
            self.targetingIncludeWidgetsList([]);
            self.targetingExcludeWidgetsList([]);

            self.addItemsToDropdown();

            // deferreds
            var deferreds = [
                self.getTargetingAgeGroups(),
                self.getTargetingGenderGroups(),
                self.getTargetingAudiences(),
                self.getTargetingCategories(),
                self.getTargetingProximicMaturityRating(),
                self.getTargetingProximicSafetyLevel(),
                self.getTargetingProximicLanguage(),
                self.getTargetingProximicPageQuality(),
                self.getTargetingProximicPageNoticeability(),
                self.getTargetingProximicPagePlacement(),
                self.getTargetingProximicContextual(),
                self.getTargetingPeerContextualSegments(),
                self.getTargetingPeerPageQuality(),
                self.getTargetingPeerLanguage(),
                self.getTargetingPeerBrandProtection(),
                self.getTargetingLotameDemographic(),
                self.getTargetingLotameAdvancedDemographic(),
                self.getTargetingLotameBehavioralInterest(),
                self.getTargetingLotameInfluencer(),
                self.getTargetingLotameOffline()
            ];

            $.when.apply($, deferreds).done(function() {
                self.targetingInitialWidgets();
                deferred.resolve();
            });
        };

        // add items to drop down lists
        self.addItemsToDropdown = function() {
            ko.utils.arrayForEach(this.targetingWidgets, function(element) {
                var newElement = _.clone(element);
                element.visible = ko.observable(true);
                element.section = 'include';
                element.target = element.include;
                self.targetingIncludeWidgetsList.push(element);
                newElement.visible = ko.observable(true);
                newElement.section = 'exclude';
                newElement.target = newElement.exclude;
                self.targetingExcludeWidgetsList.push(newElement);
            });
        };

        // edit mode: load inital widgets
        // (search if there is any data in widgets data fields,
        // if there is than show that widget)
        self.targetingInitialWidgets = function() {
            var sectionList = [
                'targetingIncludeWidgetsList', 'targetingExcludeWidgetsList'
            ];
            ko.utils.arrayForEach(sectionList, function(section) {

                ko.utils.arrayForEach(self[section](), function(widget) {
                    if (_.isString(widget.target)) {
                        var data = self.getField(widget.target);
                        if (data().length > 0) {
                            self.targetingInsertWidget(widget, false);
                        }
                    } else {
                        var insertedTemplates = [];
                        ko.utils.arrayFirst(widget.target, function(item) {
                            if (_.isString(item.data)) {
                                var data = self.getField(item.data);
                            } else {
                                var data = item.data;
                            }
                            if (data().length > 0) {
                                self.targetingInsertWidget(widget, false);
                                insertedTemplates.push(widget.template);
                                return true;
                            }
                        });

                        var onlyCheckboxes = 'targeting-widget-checkbox-groups';
                        var inArray = $.inArray(widget.template,
                                                insertedTemplates) !== -1;
                        if (inArray && widget.template === onlyCheckboxes) {
                            ko.utils.arrayForEach(widget.target,
                            function(item) {
                                if (item.hasOwnProperty('rows')) {
                                    var dataDict = self[item.rows]();
                                    var idList = {};
                                    ko.utils.arrayForEach(dataDict,
                                    function(dict) {
                                        idList[dict.id] = dict.name;
                                    });
                                }
                            });
                        }
                    }
                });
            });
        };

        // inserting widget
        self.targetingInsertWidget = function(widget, event) {
            self.connectTargetWithField(widget);
            widget.visible(false);
            if (widget.section === 'include') {
                self.targetingIncludeWidgets.push(widget);
            } else {
                self.targetingExcludeWidgets.push(widget);
            }
        };

        // delete widget event
        self.targetingRemoveWidget = function(widget, event) {

            if (!widget) {
                return false;
            }

            widget.visible(true);
            if (widget.section === 'include') {
                self.targetingIncludeWidgets.remove(widget);
            } else {
                self.targetingExcludeWidgets.remove(widget);
            }
            // clear data field (or fields)
            if (widget.hasOwnProperty('target')) {
                if (_.isArray(widget.target)) {
                    ko.utils.arrayForEach(widget.target, function(target) {
                        if (_.isString(target.data)) {
                            var field = self.getField(target.data);
                        } else {
                            var field = target;
                        }
                        field.removeAll();
                    });
                } else {
                    if (_.isString(widget['target'])) {
                        var field = self.getField(widget['target']);
                    } else {
                        var field = widget['target'];
                    }
                    field.removeAll();
                }
            }
        };

        // Removes proper targeting widgets when strategy type is changed
        self.strategyType = '';
        self.strategyTypeChange = ko.computed(function() {

            var type = self.fields().type();
            var isChanged = (type != self.strategyType);

            if (!isChanged) {
                return;
            }
            self.strategyType = type;
            if (self.strategyType == 'Web') {
                self.targetingRemoveWidget(
                    _.find(self.targetingIncludeWidgets(), function(widget) {
                        return widget.name === 'Device';
                    })
                );
                self.targetingRemoveWidget(
                    _.find(self.targetingExcludeWidgets(), function(widget) {
                        return widget.name === 'Device';
                    })
                );
            }
        });

        // bind typeahead with input (widgets with autocomplete)
        self.targetingAutocompleteWidget = function(domElement, koObj) {
            var element = $(domElement[1]),
                widgetType = element.data('widget'),
                api = element.data('api'),
                section = element.data('section');

            function search_filter(parsedResponse) {
                var results = _.map(parsedResponse.objects, function(item) {
                    var obj = {
                        'id': item.id,
                        'name': item.name
                    };
                    if (item.hasOwnProperty('help')) {
                        obj['help'] = item.help;
                    }
                    return obj;
                });
                return results;
            }

            element.find('.typeahead').typeahead({
                name: widgetType,
                valueKey: 'name',
                remote: {
                    url: api + 'search/?q=%QUERY',
                    cache: false,
                    filter: function(parsedResponse) {
                        return search_filter(parsedResponse);
                    }
                },
                template: [
                    '<p class="tt-value -t-value-' +
                    widgetType + '">{{name}}</p>',
                    '<p class="tt-helper">{{help}}</p>'
                ].join(''),
                limit: 10,
                engine: Hogan
            }).on('typeahead:selected typeahead:autocompleted',
            function(event, object) {
                if (_.isFunction(koObj.target)) {
                    target = koObj.target;
                } else {
                    if (_.isString(koObj.target[0].data)) {
                        target = self.getField(koObj.target[0].data);
                    } else {
                        target = koObj.target[0].data;
                    }
                }
                target.push({
                    id: object.id,
                    name: object.name
                });
                $(this).val('');
            }).blur(function(e) {
                $(this).val('');
            });
        };

        // widgets with input without autocomplete
        self.targetingNoAutocompleteWidget = function(domElement, koObj) {
            $(domElement[1]).find('input[type="text"]')
            .keypress(function(e) {
                if (e.which == 13) {
                    if (koObj.target.length > 0) {
                        target = koObj.target[0].data;
                    } else {
                        target = koObj.target;
                    }
                    target.push($(this).val());
                    $(this).val('');
                }
            });
        };

        self.targetingTrayWidget = function(domElement, koObj) {

            koObj.receiveFromTray = function(audience) {
                var audience = ko.toJS(audience.fields);
                var duplicate = _.find(koObj.target(), function(element) {
                    return element.id == audience.id;
                });
                if (_.isUndefined(duplicate)) {
                    koObj.target.push(audience);
                }
            };
            $(domElement[1]).find('.-t-add-audience').click(function(event) {
                storage.showAudiencesTrayFor(koObj);
                event.preventDefault();
            });
        };

        // connect js plugins after widget is rendered
        self.targetingWidgetPostRender = function(domElement, koObj) {
            if (koObj.template.indexOf('search') !== -1) {
                // bind typeahead with input (widgets with autocomplete)
                self.targetingAutocompleteWidget(domElement, koObj);
            } else if (koObj.template.indexOf('input') !== -1) {
                // widgets with input without autocomplete
                self.targetingNoAutocompleteWidget(domElement, koObj);
            } else if (koObj.template.indexOf('tray') !== -1) {
                // Tray selection widget
                self.targetingTrayWidget(domElement, koObj);
            }
        };

        // checking if widget have any data in a target resource
        self.isWidgetNotEmpty = function(widget) {
            if (_.isArray(widget.target)) {
                // for multi data widgets
                var is_not_empty = false;
                ko.utils.arrayForEach(widget.target, function(target) {
                    if (self.fields()[target.data]().length > 0) {
                        is_not_empty = true;
                        return;
                    }
                });
                return is_not_empty;
            } else {
                // for single data widgets
                return self.fields()[widget.target.data]().length != 0;
            }
        };

        self.getCheckedElementCount = function(widget) {
            var name = self.targetingGetArrayForCheckbox(widget, widget.type);
            return self.fields()[name]().length;
        };

        self.targetingWidgetsAdditionalCosts = ko.computed(function() {
            /*
                Calculate maximum additional cost of data providers

                For Proximic and Peer segments, the overall cost is the
                cost of the most expensive segment.

            */
            var cost_max = {},
                cost_sum = 0;

            // Loop over every section (include, exclude)
            var widget_lists = [
                    'targetingIncludeWidgets',
                    'targetingExcludeWidgets'
                ];
            ko.utils.arrayForEach(widget_lists, function(widget_list) {
                // And over every widget added to section
                ko.utils.arrayForEach(self[widget_list](), function(widget) {
                    if (_.has(widget, 'additional_costs')) {
                        var cost_value = widget.additional_costs.value;
                            cost_category = widget.additional_costs.category;
                        if (self.isWidgetNotEmpty(widget)) {
                            if (cost_max.hasOwnProperty(cost_category)) {
                                if (cost_value > cost_max[cost_category]) {
                                    cost_max[cost_category] = cost_value;
                                }
                            } else {
                                cost_max[cost_category] = cost_value;
                            }
                        }
                    }
                });
            });

            // Sum Peer and Proximic
            var sum = cost_sum;
            _.each(_.keys(data_providers), function(category) {
                if (cost_max.hasOwnProperty(category)) {
                    sum += cost_max[category];
                }
            });
            return (sum == 0) ? '-' : '$' + sum.toFixed(2);
        });

    };

    return {
        strategyVM: new strategyVM(),
        Site: Site,
        Advert: Advert
    };
});