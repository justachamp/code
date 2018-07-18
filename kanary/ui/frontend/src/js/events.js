define(['utils', 'account', 'text!js/templates/event_object.html'],
    function(utils, account, event_link) {

    /**
     * Day - it contains events
     *
     * @constructor
     * @this {Day}
     * @param {Date} datetime - hour and minutes are irrelevant.
     */
    function Day(datetime) {

        var self = this,
            date_format = 'dddd, MMMM D, YYYY';

        self.datetime = ko.observable(datetime);
        self.events = ko.observableArray([]);

        // Computed

        self.date_formatted = ko.computed(function() {
            return (self.datetime() || datetime).format(date_format);
        });

        /**
         * Computed that returns list of events from active categories.
         *
         * @return {object} - iterable list of filtered events.
         */
        self.events_filtered = ko.computed(function() {
            return _.filter(self.events(), function(event) {
                return event.is_active();
            });
        });

    }

    /**
     * Category - Events category - filters in sidebar
     *
     * @constructor
     * @this {Category}
     * @param {object} - needs to contain values: id, name.
     */
    function Category(category) {

        var self = this;

        self.id = ko.observable(category.id);
        self.name = ko.observable(category.name);
        self.is_active = ko.observable(true);

        // Methods

        self.toggle_active = function() {
            self.is_active(! self.is_active());
            return self.is_active();
        };

    }

    /**
     * Event
     *
     * @constructor
     * @this {Event}
     * @param {object} - needs to contain following values:
     *     id, header, message, category, datetime.
     */
    function Event(event) {

        var self = this,
            full_date = 'DD-MM-YYYYTHH:mm',
            time_format = 'HH:mm';

        var date = moment(event.datetime, full_date);

        self.id = ko.observable(event.id);
        self.header_raw = ko.observable(event.header);
        self.message_raw = ko.observable(event.message);
        self.datetime = ko.observable(date);
        self.category = event.category;

        // Methods

        self.render_link = function(obj) {
            obj.url = obj.object + '_id';
            return _.template(event_link, obj);
        };

        // Computed

        self.is_active = ko.computed(function() {
            return self.category.is_active();
        });

        self.time = ko.computed(function() {
            return (self.datetime() || date).format(time_format);
        });

        self.header = ko.computed(function() {
            if (! self.header_raw()) {
                return {};
            }
            return self.render_link(JSON.parse(self.header_raw()));
        });

        self.message = ko.computed(function() {
            var msg = JSON.parse(self.message_raw() || event.message);
            var links = {};
            _.each(msg.objects, function(obj, name) {
                links[name] = self.render_link(obj);
            });
            return _.template(msg.message, links);
        });

        self._year_month_day = ko.computed(function() {
            return (self.datetime() || date).format('YYYYMMDD');
        });

    }

    /**
     * Events Singleton class - API exposed for other modules
     *
     * @constructor
     * @this {Events}
     */
    function Events() {

        var self = this;

        self.daysArray = ko.observableArray([]);
        self.days = ko.observable();
        self.events = ko.observableArray([]);
        self.categories = ko.observable({});
        self.categoriesArray = ko.observableArray();
        self.has_more = ko.observable();

        // Methods

        /**
         * Loads events and categories via API and cleanups already loaded.
         * @param {boolean} mark_as_read - updates
         *     and saves to backend all events as read.
         */
        self.update = function() {

            // cleanup
            self.daysArray([]);
            self.days({});
            self.events([]);

            return $.when(self.categories_update()).done(function() {
                self.load_more().done(function() {
                    self._mark_all_as_read();
                });
            }).promise();
        };

        self.load_more = function() {
            return $.getJSON(self._events_url()).done(function(resp) {
                _.each(resp.objects, self._add_event);
                self.has_more(!_.isNull(resp.meta.next));
                account.loggedUser.fields()
                    .unread_events_count(resp.meta.unread);
            }).promise();
        };

        /**
         * Loads categories via API and cleanups already loaded.
         */
        self.categories_update = function() {
            var url = Urls.api_dispatch_list('notification/event_category');
            url += '?limit=0';
            return $.getJSON(url).done(function(resp) {
                // cleanup
                self.categories({});
                self.categoriesArray([]);

                _.each(resp.objects, function(category_json) {
                    var cat = new Category(category_json);
                    self.categories()[cat.id()] = cat;
                    self.categoriesArray.push(cat);
                });
            }).promise();
        };

        /**
         * Marks all loaded events as read.
         * (Saves via API most recent event)
         */
        self._mark_all_as_read = function() {
            if (self.events().length === 0) {
                return;
            }
            account.loggedUser.unread_events(0);
        };

        self._add_event = function(event) {
            event.category = self.categories()[event.category_id];
            var ev = new Event(event),
                hash = ev._year_month_day();

            if (_.isUndefined(self.days()[hash])) {
                self.days()[hash] = new Day(ev.datetime());
                self.daysArray.push(self.days()[hash]);
            }
            self.days()[hash].events.push(ev);
            self.events.push(ev);
        };

        // Computed

        /**
         * Computed counter of not readed events
         * @return {integer} not_yet_read.
         */
        self.not_yet_read = ko.computed(function() {
            return account.loggedUser.unread_events() || 0;
        });

        /**
         * Computed that returns list of active categories.
         * @return {object} categories - iterable list of active categories.
         */
        self.categories_active = ko.computed(function() {
            return _.filter(self.categoriesArray(), function(cat) {
                return cat.is_active();
            });
        });

        /**
         * Computed that returns list of days that have events in active
         * categories.
         * @return {object} categories - iterable list of active categories.
         */
        self.days_filtered = ko.computed(function() {
            return _.filter(self.daysArray(), function(day) {
                return day.events_filtered().length !== 0;
            });
        });

        self._most_recent_id = ko.computed(function() {
            var events = self.events();
            return events.length ? events[0].id() : null;
        });

        self._events_url = ko.computed(function() {
            var url = Urls.api_dispatch_list('notification/event');
            url += '?limit=20';

            if (! self.events().length) {
                return url;
            }
            var oldest = self.events()[self.events().length - 1].id();
            return url + '&id__lt=' + oldest;
        });

    }


    return {
        init: function() {
            _.extend(this, new Events());
        }
    };

});
