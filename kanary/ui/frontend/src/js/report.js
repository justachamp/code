define([
    'logger', 'js/reports.ui', 'utils', 'strategy'
], function(logger, reports_ui, utils, strategy) {

    // Configurable parameters
    var DEFAULT_END_DELTA = 7,  // in days
        DEFAULT_HOUR = '00:00',
        // Digits after separator
        FLOAT_PRECISION = 4;
        // Shortcuts for externals

    //
    // Object representing report in presentation-ready extended form
    //
    function Report() {

        // Internals
        var self = {};

        self.loaded = false;
        self.level = null;  // 'Campaign' or 'Strategy'
        self.name = null;
        self.slug = null;

        // Template view observables
        self.reportDateRange = ko.observable();
        self.dateRangePicker = new reports_ui.DateRangePicker(self);

        self.reportDimensions = ko.observableArray();
        self.dimension = ko.observable();
        self.dimension_from_targeting = ko.observable(false);
        // Eg. 'target_value' in Device OS report
        // or 'segment_proximic_maturity_rating' in Proximic Maturity report
        self.report_related_field = ko.observable(false);
        self.dimension.subscribe(function(dimension) {
            if (self.loaded) {
                self.reload();
            }
        });

        self.hasMoreItems = ko.observable(false);
        self.limit = CONFIG.REPORT_ITEMS_LIMIT;
        self.start_date = self.dateRangePicker.start_date;
        self.end_date = self.dateRangePicker.end_date;

        // Render hours only for periods lower than 6 days.
        // We cannot put this function to Chart because Chart does not know
        // its parent upon creation.
        self.hours_matter = ko.computed(function() {
            var delta = moment.duration(
                self.end_date() - self.start_date()
            );
            return delta.asDays() < 6;
        });

        self.overview = ko.observable({});
        self.table = new reports_ui.Table(self);
        self.chart = reports_ui.Chart(self);
        // Set true when animating completed:
        self.show_chart = ko.observable(false);
        self._query_dfd = null;  // Deferred of the current report query.

        // Based on data range and related campaign or strategy
        // return current backend API url
        self.report_data_params = function() {
            var slug = self.slug,
                params = {};

            params.end_date = utils.format_dt(self.end_date(),
                                              CONFIG.JS_DATE_FORMAT_URL);
            params.start_date = utils.format_dt(self.start_date(),
                                                CONFIG.JS_DATE_FORMAT_URL);

            params.sort = self.table.sort_column();
            params.dim = self.dimension();
            params.limit = self.limit;

            return params;
        };

        self.report_url = function(params) {
            if (!params) {
                params = self.report_data_params();
            }
            var reverse_url = (self.level === 'Campaign') ?
                'report_campaign_overview' : 'report_strategy_overview';
            return Urls[reverse_url](self.slug) + '?' + $.param(params);
        };

        // Build query URL and update the report.
        //
        // @param {Object} params - GET params to query for
        // @return promise
        self.update_report_query = function(params) {
            var url = self.report_url(params);

            if (self._query_dfd) {
                // If a request had already been going on, reject it.
                //
                // Otherwise, if the user clicks faster than the requests
                // complete, the report may end up in the state when there are
                // 2 awaiting report requests for different drills and
                // self.dimension with the value of the last clicked drill.
                // The first request completes, changing self.dimension to
                // its dimension which triggers third drill request.
                // Then the second request completes and does the same, causing
                // 4th request, etc.
                //
                // This does not happen if we always abort the previous request
                // if it has not completed yet.
                self._query_dfd.abort();
            }

            self._query_dfd = $.getJSON(url);
            return self._query_dfd.then(self.update_report);
        };

        // Interpret retrieved report data and apply them to controls.
        //
        // @param {Object} raw_report_data - JSON response of report resource
        // @return promise
        self.update_report = function(raw_report_data) {
            var response = raw_report_data.response;

            // Initializing in depedency order.
            // Source components.
            self.dateRangePicker.fill(response.date_range);
            self.dimension(response.dimension);
            self.dimension_from_targeting(response.dimension_from_targeting);
            self.report_related_field(response.report_related_field);
            self.hasMoreItems(response.table.length >= self.limit);

            // Dependent components.
            self.overview(response.overview);
            self.table.update({rows: response.table});

            self.loaded = true;
            self._query_dfd = null;
            // The chart will load on its own:
            logger.info('Report fully prepared and displayed');
        };

        // Reloads report data with changed params and updates its
        // observables, forcing report refresh
        //
        // @param {Integer} limit - number of rows to get. If not given, default
        //      number of rows is returned.
        //
        self.reload = function(limit) {
            self.limit = limit || CONFIG.REPORT_ITEMS_LIMIT;
            return self.update_report_query(self.report_data_params());
        };

        // Initial loading of report data from API based on given url.
        // @param {Object} params - GET query params to glue to base query URL
        //     using $.param ({start_date: moment(sth), end_date: moment(sth)})
        self.load = function(params) {
            var dimensions;
            params = ko.utils.extend(params, {sort: '~imp'});
            self.loaded = false;

            self.overview({});

            dimensions = [{
                Campaign: {slug: 'strategy', name: 'Strategy', is_mobile: false},
                Strategy: {slug: 'advert', name: 'Advert', is_mobile: false}
            }[self.level]];

            dimensions = dimensions.concat(CONFIG.REPORT_DIMENSIONS);

            if (self.level == 'Strategy') {
                type = strategy.strategyVM.fields().type();
                if (type == 'Web') {
                    // hide dimensions related to mobile strategy
                    dimensions = _.where(dimensions, { is_mobile: false });
                }
            }


            self.reportDimensions(dimensions);

            return self.update_report_query(params).then(function() {
                // Register this callback after first load that involves
                // filling defaults in date range.
                self.dateRangePicker.range.subscribe(function() {
                    self.reload();
                });
            });
        };

        self.loadMore = function() {
            var limit = self.limit + CONFIG.REPORT_ITEMS_LIMIT;
            return self.reload(limit);
        };

        return self;
    }

    // Public interface
    return {
        Report: Report,
        FLOAT_PRECISION: FLOAT_PRECISION
    };
});
