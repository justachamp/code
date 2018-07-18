define(['ui.components', 'utils', 'localStoragePolyfill'], function(components, utils) {
    /**
    Module contains all constructors/objects cconnected with reports
    user interface.
    **/

    // Available colors of row checkboxes.
    var CHECKBOX_COLOR_NAMES = [
            'red',
            'blue-light',
            'green-light',
            'yellow',
            'indian-red',
            'blue',
            'orange',
            'celadon',
            'violet',
            'gray',
            'green'
        ],
        CHECKBOX_COLORS = {
            // Copied from less.
            'red': '#d93b3b',
            'blue-light': '#03aeef',
            'green-light': '#79c421',
            'yellow': '#f4da2c',
            'indian-red': '#d05589',
            'blue': '#234bb0',
            'orange': '#ee720e',
            'celadon': '#3ac1a6',
            'violet': '#7f4fa1',
            'gray': '#999999',
            'green': '#0c9736'
        };


    /*
     * Defines a metrics checkbox which is used later for enabling available
     * metrics in table, charts, etc.
     */
    function Metric(parent) {
        var self = new components.Component(parent);

        self.init = self.update = function(metric) {
            self.checked = ko.observable(metric.checked);
            self.slug = ko.observable(metric.slug);
            self.short_name = ko.observable(metric.short_name);
            self.name = ko.observable(metric.name);
            self.blacklist = ko.observable(metric.blacklist);
        };

        return self;
    }

    /*
     * Describes a single cell of table with data
     */
    var TableRowCell = function(parent) {
        var self = new components.Component(parent);

        self.header = null;
        self.slug = null;
        self.value = ko.observable();

        self.init = self.update = function(cell) {
            self.header = cell.header;
            self.slug = cell.slug;
            self.value = cell.value;
        };

        return self;
    };


    /*
     * A row of table, contains data about assigned series, their id,
     * level of nesting, checkbox for marking chart series, etc.
     */
    var TableRow = function(parent) {
        var self = new components.Component(parent);
        self.id = ko.observable(null);
        self.tableSort = null;

        // Defined if we can drill down this row more and display drill-down
        // widget after label name.
        self.extensible = ko.observable(false);
        self.checked = ko.observable(false);
        self.color = ko.observable(null);
        self.disabled = ko.observable(false);
        self.blacklist = ko.observable(false);

        self.whitelist_blacklist = ko.computed( function() {
            if (self.parent.parent.dimension_from_targeting() && self.id() != null) {
                return true;
            }
            return false;
        });

        /* Pick or release color.
         * @return new color name from CHECKBOX_COLOR_NAMES if picked new color
         *     or null if not.
         */
        self.set_checked = function(checked) {
            var color;
            if (checked) {
                color = self.parent.pick_checkbox_color();
                if (color === false) {
                    throw Error('Ran out of colors.');
                }
            } else {
                self.parent.free_checkbox_color(self.color());
                color = null;
            }

            self.color(color);
            self.checked(checked);
            return color;
        };

        self.label = null;
        self.cells = new components.ComponentSet(self, 'slug', TableRowCell);
        self.cells_columns = null;

        /*
         * Return array of column values.
         */
        self.values = ko.computed(function() {
            return _.pluck(self.cells.elements(), 'value');
        });

        self.whitelist_blacklist_click = function() {
            if (self.blacklist()) {
                var url = Urls.report_whitelist(slug=self.parent.parent.slug);
            } else {
                var url = Urls.report_blacklist(slug=self.parent.parent.slug);
            }

            $.post(
                url,
                {
                    report_related_field: self.parent.parent.report_related_field(),
                    id: self.id()
                }
            ).always(function (data, status, jqXHR) {
                if (jqXHR.status == 200) {
                    self.blacklist(data == 'whitelist');
                }
            });
            return;
        };

        /** Function initializes object, based on data given from
        backend/master class **/
        self.init = self.update = function(item) {
            var cells = _.map(item.headers.elements(),
                function(header) {
                    return {
                        header: header,
                        slug: header.slug,
                        value: item.cells[header.slug()]
                    };
                });
            self.id(item.info.pk);
            self.label = item.info.label;
            self.is_running = item.info.is_running;
            self.blacklist(item.info.blacklist);
            self.report_related_field = self.parent.parent.report_related_field();
            self.cells.update(cells);
            self.cells_columns = item.cells;
        };

        return self;
    };

    /*
     * Represents data from tabular backend reports.
     */
    var Table = function(parent) {
        var self = new components.Component(parent);
        self.headers = new components.ComponentSet(self, 'slug', Metric);
        self.headers.update(CONFIG.METRICS);

        self.rows = new components.ComponentSet(self, 'id', TableRow);
        self.sort_column = ko.observable('~imp');

        // Return first available checkbox color.
        // The length of CHECKBOX_COLOR_NAMES is the maximum number
        // of selected table items (=== max number of visible chart series).
        self.get_free_checkbox_color = function() {
            return _.difference(CHECKBOX_COLOR_NAMES,
                                self.used_checkbox_colors)[0];
        };
        self.used_checkbox_colors = [];
        self.max_checked_checkboxes = CHECKBOX_COLOR_NAMES.length;
        self.checkboxes_disabled = ko.observable(false);

        /* Get a free color from the pool.
         * Return color name or false if the pool got empty.
         */
        self.pick_checkbox_color = function() {
            var color;
            if (_.isUndefined(self.get_free_checkbox_color())) {
                return false;
            }
            color = self.get_free_checkbox_color();
            self.used_checkbox_colors.push(color);

            // Lock the checkboxes if there are no colors left
            if (self.used_checkbox_colors.length ===
                self.max_checked_checkboxes) {
                self.checkboxes_disabled(true);
            }
            return color;
        };

        /* Release the color and return it to the pool.
         * @throws Error if no such color had been in use
         */
        self.free_checkbox_color = function(color) {
            if (self.used_checkbox_colors.indexOf(color) === -1) {
                throw Error(
                        'Color does not exist in self.used_checkbox_colors: ' +
                        color);
            }
            self.used_checkbox_colors =
                _.without(self.used_checkbox_colors, color);

            // There must be at least one available color now (we just
            // freed one).
            self.checkboxes_disabled(false);
        };

        /* Return list of checked rows ids and colors, like:
         * [{color: color, id: 1212}]
         */
        self.checked_rows = ko.computed(function() {
            var checked = _.filter(
                self.rows.elements(),
                function(row) { return row.checked(); }
            );
            return _.map(
                checked,
                function(row) {
                    return {
                        id: row.id,
                        label: row.label,
                        color: row.color()
                    };
                }
            );
        });

        self.clear = function() {
            self.rows.elements([]);
        };

        self.check_default_rows = function() {
            // Activate default checkboxes.
            var rows_to_select = CONFIG.REPORTS_DEFAULT_SELECTED_ENTRIES;
            _.each(
                self.rows.elements().slice(0, rows_to_select),
                function(el) {
                    el.set_checked(true);
            });
        };

        self.uncheck_all_rows = function() {
            _.each(self.rows.elements(), function(el) {
                if (el.checked()) {
                    el.set_checked(false);
                }
            });
        };
        self.parent.dimension.subscribe(self.uncheck_all_rows);

        self.update = function(item) {
             var checked_rows = {},
                 rechecked_rows_count = 0;

            // Save checked rows.
            _.each(
                self.rows.elements(),
                function(row) {
                    checked_rows[row.id] = row.checked();
                }
            );

            self.clear();
            if (!item.rows) {
                // no data from backend
                return;
            }

            var selectedMetrics = localStorage.getItem('selected-metrics');
            if (selectedMetrics) {
                selectedMetrics = selectedMetrics.split(',');
            }
            _.each(self.headers.elements(), function(metric) {
                if (selectedMetrics) {
                    /* restore selected metrics */
                    metric.checked(selectedMetrics.indexOf(
                        metric.slug()) != -1);
                }
                metric.checked.subscribe(self.save_selected_metrics);
            });

            _.each(self.used_checkbox_colors.slice().reverse(),
                    self.free_checkbox_color);

            if (item.rows) {
                var map_row = function(row) {
                        return {
                            headers: self.headers,
                            info: row[0],
                            cells: row[1]
                        };
                    };
                var values = _.map(item.rows, map_row);
                self.rows.update(values);

            }

            // Recheck recognised rows.
            _.each(
                self.rows.elements(),
                function(row) {
                    if (checked_rows[row.id] === true) {
                        row.set_checked(true);
                        rechecked_rows_count += 1;
                    }
                }
            );
            if (rechecked_rows_count === 0) {
                self.check_default_rows();
            }
        };


        self.save_selected_metrics = function() {
            var selectedMetrics = [];
            _.each(self.headers.elements(), function(metric) {
                if (metric.checked()) {
                    selectedMetrics.push(metric.slug());
                }
            });
            localStorage.setItem('selected-metrics', selectedMetrics.join(','));
        };

        return self;
    };

    /*
     * Chart VM.
     * glossary:
     *      data, series - morris' data parameter, contains graph values
     *      metric - one of use-picked metrics - imp, clk, etc.
     */
    var Chart = function(parent) {
        var self = new components.Component(parent);
        self.metric = ko.observable('imp');

        /*
         * Retrieve arrays of checked rows' keys, corresponding colors and
         * labels.
         */
        self.table_state = ko.computed(function() {
            var rows = self.parent.table.checked_rows(),
                keys = _.map(rows, function(row) {return row.id()}),
                colors = _.map(
                    _.pluck(rows, 'color'), function(color_name) {
                        // Pick color code.
                        return CHECKBOX_COLORS[color_name];
                    }
                ),
                labels = _.pluck(rows, 'label');

            return {
                keys: keys,
                colors: colors,
                labels: labels
            };
        });

        /*
         * Request chart series for provided ids.
         */
        self.query = function(related_ids) {
            var start_date = self.parent.start_date(),
                end_date = self.parent.end_date(),
                url;
            if (!(start_date.isValid() && end_date.isValid())) {
                return $.Deferred().reject();
            }

            url = Urls.report_chart(
                self.parent.level, self.parent.slug) + '?' +
                    $.param({
                        related_ids: related_ids,

                        start_date: utils.format_dt(
                            start_date,
                            CONFIG.JS_DATE_FORMAT_URL
                        ),

                        end_date: utils.format_dt(
                            end_date,
                            CONFIG.JS_DATE_FORMAT_URL
                        ),

                        chart_metric: self.metric(),
                        dim: self.parent.dimension()
                    });
            return $.getJSON(url).then(function(data) {
                return data.series;
            });
        };

        // Render hours only for periods lower than 6 days.
        self.hours_matter = ko.computed(function() {
            var delta = moment.duration(
                self.parent.end_date() - self.parent.start_date()
            );
            return delta.asDays() < 6;
        });

        /*
         * Generate phantom points to force graph date range reflect selected
         * date range even if there is no data.
         */
        self.generate_phantom_points = function() {
            var limits = [];

            if (self.parent.start_date()) {
                limits.push(
                    {'dt': utils.format_dt(self.parent.start_date(),
                                           'YYYY-MM-DD')});
            }
            if (self.parent.end_date()) {
                limits.push(
                    {'dt': utils.format_dt(self.parent.end_date(),
                                           'YYYY-MM-DD')
                });
            }

            return limits;
        };

        self.set_morris_params = function(series) {
            var table = self.table_state(),
                series_data,
                morris_series,
                props;

            props = {
                // Chart data records -- each entry in this array
                // corresponds to a point on the chart.
                data: null,
                // A list of names of data record attributes that contain
                // y-values.
                ykeys: table.keys,
                // Labels for the ykeys -- will be displayed when you hover
                // over the chart.
                labels: table.labels,
                lineColors: table.colors,
                hideHover: 'auto',
                xLabelFormat: function(timestamp) {
                    // Depending on date range, produce the desired datetime
                    // format.
                    var start = self.parent.start_date(),
                        end = self.parent.end_date(),
                        format =
                            // Always show month and day:
                            'MMM DD' +
                            // Render years only if year changed during the
                            // period:
                            (start.year() !== end.year() ? ' YYYY' : '') +
                            (self.hours_matter() ? ' HH:mm' : '');

                    return moment(timestamp).format(format);
                },
                // Reformat on-hover legend HTML. Hacks on hacks.
                hoverCallback: function(index, options, content) {
                    var html,
                        series_labels_containers, no_values_given,
                        date_container, raw_date, dt, legend_dt_format;

                    // content is html string like:
                    // <div class='morris-hover-row-label'>
                    //     2014-05-19 00:00:00
                    // </div>
                    // <div class='morris-hover-point' style='color: red'>
                    //     Image One: 77,616
                    // </div>
                    // <div class='morris-hover-point' style='color: grey'>
                    //     Image One: 208,984
                    // </div>
                    // All those divs are split by jQuery as separate array
                    // elements.
                    html = $(content);

                    // Check if the legend would display any values by parsing
                    // the HTML and searching for placeholders (hyphens).
                    series_labels_containers = html.slice(1);
                    no_values_given = _.all(
                        series_labels_containers,
                        function value_is_missing(dom_element) {
                            var text = dom_element.innerHTML
                                    // Remove newlines:
                                    .replace(/\n/g, '')
                                    // Remove multi whitespace:
                                    .replace(/ +/g, ' ')
                                    // Remove leading whitespace:
                                    .replace(/^ */, '')
                                    // Remove trailing whitespace:
                                    .replace(/ *$/, ''),
                                // Search for trailing hyphen.
                                hyphen_match = / -$/.test(text);

                            return hyphen_match;
                        }
                    );
                    if (no_values_given) {
                        // Apply JS that when injected, hides the legend.
                        // Helpful in case of empty data caused by phantom
                        // points we use to force x axis range.
                        //
                        // We cannot remove this DOM because it gets reused
                        // instead of being destroyed and created for each
                        // hover. Also, we cannot use 'display: none' because
                        // it is used by morris. So, 'visibility' is left for
                        // us.
                        return '' +
                            '<script type="application/javascript">' +
                            "$('.morris-hover').css('visibility', 'hidden');" +
                            '</script>';
                    }

                    // So now we know there are some values to show.
                    // Re-show the legend if hidden.
                    $('.morris-hover').css('visibility', 'visible');

                    // Find the date in the html, parse it and replace with
                    // formated version.
                    date_container = html[0];
                    if (date_container.attributes['class'].value !==
                        'morris-hover-row-label') {
                        throw Error(
                            'Incompatible HTML passed to hoverCallback: ' +
                            content
                        );
                    }

                    legend_dt_format =
                            // Always show month, day and year:
                            'MMM DD YYYY' +
                            // Hours only if needed.
                            (self.hours_matter() ? ' HH:mm' : '');

                    raw_date = date_container.innerHTML;
                    dt = moment(raw_date);

                    // Mutating innerHTML has side effects in html variable.
                    date_container.innerHTML = dt.format(legend_dt_format);

                    return html;
                }
            };

            // Morris complains about empty ykeys array.
            if (props.ykeys.length === 0) {
                props.ykeys = [''];
                props.hideHover = 'always'; // Don't show the legend.
            }

            series_data = _.map(series, function(row, dt) {
                return _.extend({'dt': dt}, row);
            });

            morris_series = series_data.concat(self.generate_phantom_points());
            props.data = morris_series;

            self.morris_data(props);
        };

        // Observable listened in binding.
        self.morris_data = ko.observable(null);

        // One throttled computed that listens to everything and sets
        // morris_data observable that is them listened in binding.
        // https://github.com/knockout/knockout/wiki/
        //                                  asynchronous-dependent-observables
        self.trigger = ko.computed(function() {
            /* Call all observed values. This ensures we really listen to
             * them. Knockout's computeds work like that:
             * 1. Computed is created. A function is provided as an
             *    argument.
             * 2. Knockout calls the function. Knockout registers all other
             *    called observables/computed observables and makes newly
             *    created computed listen to them.
             * 3. When one of subscribed observables change, Knockout calls
             *    the function again.
             *
             * This is disastrous because:
             * 1. Subscriptions are implicit (=== hell).
             * 2. You cannot use auto-subscribed observables conditionally.
             *    That's because not called observables will be not
             *    listened to.
             * 3. You cannot auto-subscribe in async callbacks - for the
             *    same reason as above.
             *
             * Unless you call all the subscribed values, like we do below:
             */
            self.metric();
            self.parent.table.checked_rows();
            self.parent.dimension();
            self.parent.start_date();
            self.parent.end_date();

            self.query(self.table_state().keys).then(self.set_morris_params);

        }).extend({throttle: 200});

        return self;
    };

    /*
     * Datepicker for report data range
     */
    var DateRangePicker = function(parent) {
        var self = new components.Component(parent);

        self.start_date = ko.observable(moment(''));
        self.end_date = ko.observable(moment(''));
        self.separator = ko.bindingHandlers.daterangepicker.separator;

        self.date_formated = function(date) {
            if (!date) {
                return '';
            }
            return moment(date).format(CONFIG.JS_DATE_FORMAT);
        };

        self.range = ko.computed({
            read: function() {
                return self.date_formated(self.start_date()) + self.separator +
                       self.date_formated(self.end_date());
            },
            write: function(newDateRange) {
                // update from datepicker
                var dateRange = newDateRange.split(self.separator);
                self.start_date(
                    moment(dateRange[0], CONFIG.JS_DATE_FORMAT_SHORT)
                );
                self.end_date(
                    moment(dateRange[1], CONFIG.JS_DATE_FORMAT_SHORT)
                );
            }
        });

        /* Replace invalid dates with ones from given daterange object.
         * @param {object} range - object with 'start' and 'end' keys
         *     referencing strings with ISO format datetimes
         */
        self.fill = function(range) {
            if (!self.start_date().isValid()) {
                self.start_date(moment(range.start));
            }
            if (!self.end_date().isValid()) {
                self.end_date(moment(range.end));
            }
        };

        self.label = null;
        self.value = ko.observable();

        return self;
    };

    /*
     * Is responsible for managing data of cells
     */
    return {
        Table: Table,
        Chart: Chart,
        DateRangePicker: DateRangePicker
    };
});
