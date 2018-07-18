define(
['storage', 'notifications', 'logger', 'mediator', 'utils', 'router'],
function(storage, notifications, logger, mediator, utils, router) {

    ///////////////////
    /**
        qqFileUploader binding. Binds FileUploaderBasic to DOM element.
        - callback: callback to be called after successful upload.
        - element: element to be passed to callback

        Apart from element, callback have to accept:
        - responseJSON: FileUploader response
        - fileName: name of the file that has just been uploaded
        - element: element passed to binding

        callback
     */
    /* Default creatives support all types of files (img, video, flash). FB creatives support only JPG, PNG, GIF */
    function qqFileUploader(file_type, element, valueAccessor) {
        var csrf_token = utils.getCookie('csrftoken');

            var options = ko.utils.unwrapObservable(valueAccessor());

            var creativeUploader = new qq.FileUploaderBasic({
                action: Urls.storage_creatives_add_image(),
                allowedExtensions: (file_type=='img') ? ['jpg', 'jpeg', 'png', 'gif'] : [],
                button: $(element)[0],
                multiple: false,
                onSubmit: function() {
                    window['file_is_uploaded'] = true;
                },
                onComplete: function(id, fileName, responseJSON) {
                    if (! responseJSON.success) {
                        var message = 'Upload failed.';
                        if (responseJSON.errors) {
                            message = responseJSON.errors;
                        }
                        notifications.showModal('Error!', message);
                    } else {
                        options.callback(responseJSON, fileName);
                        window['file_is_uploaded'] = false;
                    }
                },
                params: {
                    'csrf_token': csrf_token,
                    'csrf_name': 'csrfmiddlewaretoken',
                    'csrf_xname': 'X-CSRFToken',
                },
                showMessage: function(message) {
                    notifications.showModal('Error!', message);
                },
            });
            // required, since by default qqFileUploader
            // can move button way off the website
            $(element).attr('style', '');
    }
    
    ko.bindingHandlers.fileUploader = {
        init: function(element, valueAccessor) {
            qqFileUploader('def', element, valueAccessor);
        }
    };
    
    ko.bindingHandlers.imageUploader = {
        init: function(element, valueAccessor) {
            qqFileUploader('img', element, valueAccessor);
        }
    };


    ////////////////////////
    ko.bindingHandlers.datepicker = {

        init: function(element, valueAccessor) {

            var value = ko.utils.unwrapObservable(valueAccessor()),
                element = $(element);

            element.data('date', valueAccessor()());

            element.datepickermobile({
                format: CONFIG.JS_DATE_FORMAT_DATEPICKER,
                weekStart: 1
            }).on('changeDate', function(ev) {
                valueAccessor()(
                    moment(ev.date).format(CONFIG.JS_DATE_FORMAT_URL)
                );
                element.datepickermobile('hide');
            });
        },
        update: function(element, valueAccessor) {
            var value = ko.unwrap(valueAccessor());
            $(element).datepickermobile('setValue', value);
            // setValue changed input's value and set data in
            // datepickermobile format so we must again set input's value
            // with propper format
            $(element).find('input').val(
                moment(
                    value,
                    CONFIG.JS_DATE_FORMAT_URL
                ).format(CONFIG.JS_DATE_FORMAT)
            );
        }
    };


    ////////////////////////
    ko.bindingHandlers.timepicker = {

        init: function(element, valueAccessor) {

            var value = ko.utils.unwrapObservable(valueAccessor());

            $(element).val(value);

            $(element).timepicker({
                defaultTime: 'value',
                showMeridian: false,
                showInputs: false
            });

            $(element).change(function() {
                valueAccessor()($(element).val());
            });
        },

        update: function(element, valueAccessor) {
            var value = ko.utils.unwrapObservable(valueAccessor());
            $(element).val(value);
        }
    };

    var DateRangePicker = function() {
        var self = this,
            settings = {
                opens: 'left',
                format: CONFIG.JS_DATE_FORMAT_DATERAGEPICKER,
                separator: ' - ',
                range: true,
                ranges: {
                    'Today': [
                        moment().format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ],
                    'Yesterday': [
                        moment().subtract(1, 'days')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().subtract(1, 'days')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ],
                    'Last 7 days': [
                        moment().subtract(7, 'days')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ],
                    'Last 30 days': [
                        moment().subtract(30, 'days')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ],
                    'This month': [
                        moment().startOf('month')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ],
                    'Last month': [
                        moment().subtract(1, 'months').startOf('month')
                                        .format(CONFIG.JS_DATE_FORMAT_SHORT),
                        moment().subtract(1, 'months').endOf('month')
                                    .format(CONFIG.JS_DATE_FORMAT_SHORT)
                    ]
                }
            };

        function attachDaterangePicker(element, valueAccessor, isUpdate) {
            var rawValue = ko.utils.unwrapObservable(valueAccessor()),
                dateRange = null,
                dateRangeAccessor = null,
                $input = $('input', element),
                $wrapper = $(element);

            if (_.isObject(rawValue)) {
                dateRange = ko.utils.unwrapObservable(rawValue['value']);
                dateRangeAccessor = rawValue['value'];

                var date_tab = dateRange.split(self.separator);
                var startDate = date_tab[0];
                var endDate = date_tab[1];

                if (startDate !== '') {
                    settings['startDate'] =
                        moment(startDate, CONFIG.JS_DATE_FORMAT).toDate();
                }
                if (endDate !== '') {
                    settings['endDate'] =
                        moment(endDate, CONFIG.JS_DATE_FORMAT).toDate();
                }
            } else {
                dateRange = rawValue;
                dateRangeAccessor = valueAccessor;
            }

            if (isUpdate) {
                // removing previously attached picker
                // See github.com/dangrossman/bootstrap-daterangepicker/pull/62
                $wrapper.data('daterangepicker').container.remove();
                $wrapper.off('.daterangepicker');
                $wrapper.data('daterangepicker', null);
            }

            $wrapper.daterangepicker(
                settings,
                function() {
                    var newDateRange = $input.val();
                    if (newDateRange !== dateRange) {
                        dateRangeAccessor(newDateRange);
                    }
                }
            );

            $input.val(dateRange);
        }

        self.separator = settings.separator;

        self.init = function(element, valueAccessor) {
            attachDaterangePicker(element, valueAccessor, false);
        };

        self.update = function(element, valueAccessor) {
            attachDaterangePicker(element, valueAccessor, true);
        };
    };
    ko.bindingHandlers.daterangepicker = new DateRangePicker();

    ////////////////////////
    ko.bindingHandlers.fancyCheckbox = {

        init: function(element, valueAccessor) {
            var $element = $(element);
            // wrap element with label.checkbox
            if (!$element.parents('label.checkbox').length) {
                $element.wrap('<label class="checkbox"></label>');
            }
        },

        update: function(element, valueAccessor, bindingsAccessor, viewModel,
                         bindingContext) {

            var rawValue = valueAccessor(),
                valueFunc = rawValue['value'] || rawValue,
                onclickFunc = rawValue['onclick'] || null,
                $element = $(element),
                $label = $element.parent('label.checkbox');

            var updateCheckboxState = function() {
                var isChecked = ko.utils.unwrapObservable(valueFunc);
                if (isChecked) {
                    $label.addClass('checked');
                } else {
                    $label.removeClass('checked');
                }
            };

            // for not binding event handler more than once
            $label.off('click.fancyCheckbox');

            $label.on('click.fancyCheckbox', function() {
                if ($element.attr('disabled')) {
                    return false;
                }

                // update observable
                var isChecked = !($label.hasClass('checked'));
                valueFunc(isChecked);

                if (_.isFunction(onclickFunc)) {
                    onclickFunc(isChecked, bindingContext.$data);
                }
                updateCheckboxState();
                return false;
            });
            updateCheckboxState();
        }
    };

    /**
     * Something like fancy checkbox, with BG color support
     */
    ko.bindingHandlers.coloredCheckbox = {
        /**
         * Initializer - wraps checkbox label
         */
        init: function(element, valueAccessor) {
            var $element = $(element);
            // wrap element with label.checkbox
            if (!$element.parents('label.checkbox').length) {
                $element.wrap('<label class="checkbox"></label>');
            }
        },

        /**
         * Updates checkbox state basing on current accessor value
         */
        update: function(element, valueAccessor) {
            // Bound value must be an object with 3 properties: value, color
            // (observables) and optional onclick (event handler)
            var rawValue = valueAccessor(),
                checkedFunc = rawValue['checked'],
                colorFunc = rawValue['color'],
                onclickFunc = rawValue['onclick'],
                $element = $(element),
                $label = $element.parent('label.checkbox');

            // Internal click handler
            function updateCheckboxState() {
                var toBeChecked = ko.utils.unwrapObservable(checkedFunc),
                    newColor = ko.utils.unwrapObservable(colorFunc);
                // Toggling checkbox state and BG color
                // (empty value removes CSS property)
                //
                // Why so strange code?
                // That's because Knockout calls update (which calls this
                // function) each time anything related to this binding
                // changes. There is no good way to make changes atomic.
                // This is pure madness because, assuming we have 2
                // observables, instead of being called once with both
                // observables updated, we are called 2 times: first with new
                // value of the first one and stale value of the other one,
                // then with the new values of both. This cripples the logic
                // we have here because it must work in both cases or at least
                // do nothing if observables get updated only partially.
                if (toBeChecked) {
                    $label.addClass('checked').addClass(newColor || '');
                    // Add info about previous color class for future css
                    // class removal.
                    if (newColor !== null) {
                        $label.data('color', newColor);
                    }
                } else {
                    // Also remove the color class.
                    $label.removeClass('checked')
                        .removeClass($label.data('color'));
                }
            };

            // For not binding event handler more than once
            $label.off('click.fancyCheckbox');

            // Click handler executed on KO update
            $label.on('click.fancyCheckbox', function() {
                if ($element.attr('disabled')) {
                    return false;
                }

                // Determining new color
                var toBeChecked = !($label.hasClass('checked')),
                    newColor = onclickFunc(toBeChecked);
                if (_.isString(newColor)) {
                    colorFunc(newColor);
                }

                // Update observable and checkbox state
                updateCheckboxState();
                return false;
            });

            // Setting initial checkbox state
            updateCheckboxState();
        }
    };

    // Selectpicker plugin
    ko.bindingHandlers.selectpicker = {
        init: function(element, valueAccessor) {
            var $element = $(element),
                rawBindingData = $element.attr('data-bind');

            // Selectpicker problem workaround - normally plugin tries to
            // treat all data-* attributes as JSONs which causes a JS error
            $element.removeAttr('data-bind')
                .selectpicker()
                .attr('data-bind', rawBindingData);
        },

        update: function(element, valueAccessor, allBindingsAccessor,
                         viewModel, bindingContext) {
            var $element = $(element),
                newValue = ko.utils.unwrapObservable(valueAccessor());
            $element.selectpicker('val', newValue);
        }
    };

    /**
     * Typeahead custom binding, to kanary api routes (tastypie)
     *
     * There properties are required for valueAccessor:
     *
     * cache_key - typeahead's cache_key
     * value - value key, which allows to retrieve value
     * target - ko.observable, where the value is to be stored
     * resource_name - tastypie resource that'll be queried
     *
     * Optional:
     *
     * display - datum key, that will be displayed in dropdown.
     *          defaults to 'value'
     *
     */
    ko.bindingHandlers.typeahead = {
        init: function(element, valueAccessor) {
            var values = ko.utils.unwrapObservable(valueAccessor());
            var cache_key = values['cache_key'],
                value_key = values['value'],
                display_key = values['value'],
                target = values['target'],
                url = Urls.api_get_search(values['resource_name']);
            if (values['display_key']) {
                display_key = values['display'];
            }

            $(element).typeahead({
                name: cache_key,
                valueKey: value_key,
                template: '<p class="tt-value">{{' + display_key + '}}</p>',
                engine: Hogan,
                remote: {
                    url: url + '?q=%QUERY',
                    cache: false,
                    filter: function(parsedResponse) {
                        if (parsedResponse.objects) {
                            return parsedResponse.objects;
                        }
                        return parsedResponse;
                    }
                },
                limit: 10
            }).on('typeahead:selected typeahead:autocompleted',
                function(event, object) {
                   target(object[value_key]);
                    /*   This forces refreshing of bound observable
                        After user selects option from dropdown
                    */
                   e = jQuery.Event('keydown');
                   e.keyCode = 13;
                   $(element).trigger(e);
            });
            // Disable clearing input on blur
            $(element).typeahead('setQuery', target());
        }
    };

    /**
     * Sort order bidding for a table.
     * Assigned valueAccessor must be an object with 2 properties:
     * item - raw value containing an identifier for current element
     * value - KO observable assigned to current element
     * Both of them are required.
     * Same observable should be usually assigned to many elements
     * responsible for each possible sort order toggling.
     */
    var SortBy = function() {
        // TODO: CSS class assignments are to be consulted with UI team
        var self = this,
            ascClassName = 'sort-asc',
            descClassName = 'sort-desc';

        // If current value (of observable) starts with this sign,
        // it means descending sort order
        self.desc = '~';

        // Initially we assign click handler for bound element
        // Which is responsible for changing assigned observable's value
        self.init = function(element, valueAccessor) {
            var rawValue = ko.utils.unwrapObservable(valueAccessor()),
                item = rawValue['item'],
                accessor = rawValue['value'],
                $element = $(element);

            $element.click(function() {
                var isDesc = false,
                    value = ko.utils.unwrapObservable(accessor);
                if (_.isString(value) && value[0] == self.desc) {
                    value = value.substr(1);
                    isDesc = true;
                }
                // If we change accessor's (observable) value,
                // update method will be triggered - it will do the rest
                if (item() === value) {
                    // sort order already matches to current element
                    // so we only change sort direction
                    accessor((isDesc) ? item() : self.desc + item());
                } else {
                    // switching from other sort order
                    accessor(item());
                }
            });
        };

        // This is called once assigned observable value changes
        self.update = function(element, valueAccessor) {
            var rawValue = ko.utils.unwrapObservable(valueAccessor()),
                item = rawValue['item'],
                accessor = rawValue['value'],
                value = ko.utils.unwrapObservable(accessor),
                $element = $(element);

            if (value === item()) {
                // sort by current item, ascending
                $element.removeClass(descClassName).addClass(ascClassName);
            } else if (value === self.desc + item()) {
                // sort by current item, descending
                $element.removeClass(ascClassName).addClass(descClassName);
            } else {
                // sort by other item
                $element.removeClass(ascClassName).removeClass(descClassName);
            }
        };
    };
    ko.bindingHandlers.sortBy = new SortBy();

    // making routes from HTML views
    ko.bindingHandlers.linkTo = {

        init: function(element, valueAccessor) {

                $(element).hover(
                    function() { document.body.style.cursor = 'pointer' },
                    function() { document.body.style.cursor = '' }
                );
        },
        update: function(element, valueAccessor) {

            var val = ko.utils.unwrapObservable(valueAccessor()),
                route = undefined;

            if (val === 'back') {
                route = 'back';
            } else if (_.isString(val)) {
                route = router.path[val]();
            } else {
                route = router.path[val.route](val.args);
            }

            // to avoid multiple event handler bindings
            $(element).off('click.linkTo');

            $(element).on('click.linkTo', function(e) {
                e.preventDefault();
                e.stopPropagation();
                router.routeTo(route, null, val.noHashChange || false);
            });
         }
    };

    // Static / media image shortcuts for HTML views
    var imgHandlerFactory = function(baseImgUrlRoute) {

        this.init = function(element, valueAccessor) {

            var imgSrc = ko.utils.unwrapObservable(valueAccessor());
            $(element).attr('src', Urls[baseImgUrlRoute]() + imgSrc);
        };
    };

    ko.bindingHandlers.staticImg = new imgHandlerFactory('static_url');
    ko.bindingHandlers.mediaImg = new imgHandlerFactory('media_url');

    ////////////////////////
    ko.bindingHandlers.noUiSliderPercent = {

        init: function(element, valueAccessor) {

            var value = ko.utils.unwrapObservable(valueAccessor());

            $(element).noUiSlider('init', {
                handles: 1,
                start: 0,
                scale: [0, 1000],
                change: function() {
                    var sliderValue = $(this).noUiSlider('value');
                    valueAccessor()(sliderValue[1]);
                    var intValue = parseInt(sliderValue[1] / 10);
                    if (isNaN(sliderValue[1])) {
                        return;
                    }
                    $(this).find('.noUi-handle div')
                        .html('<span class="infoBox">' + intValue + '%</span>');
                }
            });

        },

        update: function(element, valueAccessor) {

            var value = ko.utils.unwrapObservable(valueAccessor());

            $(element).noUiSlider('move', {to: value});

        }

    };


    ko.bindingHandlers.pluralize = {
        update: function(element, valueAccessor, allBindingsAccessor,
                         viewModel, bindingContext) {
        // http://fiddle.jshell.net/jessegavin/wamfw/
        // valueAccessor() should return an object that looks like this...
        // {
        //   data : [array or number], // can be observable or not
        //   singular : [string],
        //   plural : [string],
        // }
            function count(data) {
                var value = ko.utils.unwrapObservable(data);
                if (typeof value === 'object' && value.length > 0) {
                    return value.length;
                } else if (typeof value === 'number') {
                    return value;
                }
            }

            var settings = valueAccessor();
            if (count(settings.data) === 1) {
                var text = settings.singular;
            } else {
                var text = settings.plural;
            }
            $(element).text(ko.utils.unwrapObservable(text));
        }
    };

    // adds niceScroll knockout binding
    ko.bindingHandlers.niceScroll = {
        init: function(element) {
            $(element).niceScroll();
        }
    };

    ko.bindingHandlers.formatBudget = {
        init: function(element, valueAccessor) {
            var value = ko.utils.unwrapObservable(valueAccessor());
            $(element).val(utils.formatBudget(value));
        },
        update: function(element, valueAccessor) {
            var field = valueAccessor(),
                value = ko.utils.unwrapObservable(valueAccessor());

            $(element).change(function() {
                var inputValue = $(element).val(),
                    parsedInput = parseFloat(inputValue, 10),
                    valuePresented = undefined,
                    allowZero = _.isUndefined($(element).data('allowzero')) ?
                                true :
                                $(element).data('allowzero');

                if ((inputValue === '') ||
                    ((!allowZero) && (parsedInput == 0))) {
                    field(null);
                    valuePresented = '';
                } else if (isNaN(parsedInput) || parsedInput < 0) {
                    // if input is invalid, display last valid value
                    valuePresented = utils.formatBudget(field());
                } else {
                    // if input is valid, update observable underneath
                    field(parsedInput.toString());
                    valuePresented = utils.formatBudget(parsedInput);
                }

                $(element).val(valuePresented);
            });

            $(element).val(utils.formatBudget(value));
        }
    };

    ko.bindingHandlers.trimFloat = {
        update: function(element, valueAccessor) {
            var options = valueAccessor(),
                value = ko.utils.unwrapObservable(options.value),
                precision = options.precision;
                policy = options.policy;

            $(element).text(utils.formatFloat(value, precision, policy));
        }
    };

    ko.bindingHandlers.container = {
        init: function(element, valueAccessor, bindingsAccessor, viewModel) {
            var role = ko.utils.unwrapObservable(valueAccessor());
            if (!_.isFunction(viewModel.registerContainer)) {
                throw 'Can not register container `' + role +
                    '` for given view model';
            }
            viewModel.registerContainer(element, role);
        }
    };

    // htmlBind:

    //private template source that is simply a string
    var stringTemplateSource = function(template) {
        this.template = template;
    };

    stringTemplateSource.prototype.text = function() {
        return this.template;
    };

    //a private template engine that just deals with string templates
    var stringTemplateEngine = new ko.nativeTemplateEngine();
    stringTemplateEngine.makeTemplateSource = function(template) {
      return new stringTemplateSource(template);
    };

    //a custom binding that uses the private stringTemplateEngine
    ko.bindingHandlers.htmlBind = {
        init: function() {
            return { 'controlsDescendantBindings': true };
        },
        update: function(element, valueAccessor, allBindingsAccessor, data,
                         context) {
            var options = function() {
                return {
                    templateEngine: stringTemplateEngine,
                    name: ko.utils.unwrapObservable(valueAccessor())
                };
            };
            ko.bindingHandlers.template.update(element, options,
                allBindingsAccessor, data, context);
        }
    };

    // a custom tooltip binding
    // that's a wrapper over bootstrap tooltip
    ko.bindingHandlers.tooltip = {
        update: function(element, valueAccessor, allBindingsAccessor, data,
                         context) {
            var e, opt;

            opt = ko.utils.unwrapObservable(valueAccessor());
            e = $(element);

            // defaults from bootstrap
            e.data('tooltip');

            e.tooltip(opt);
        }
    };
    // copy to clipboard binding
    ko.bindingHandlers.copyToClipboard = {
        init: function(element, valueAccessor, allBindingsAccessor, data,
                         context) {

            /* This is the only way the clipboard plugin works
            when attached to multiple elements one after another, eg:
            new ZeroClipboard($(element1)), new ZeroClipboard($(element2)) */
            $(element).attr('data-clipboard-target', ko.utils.unwrapObservable(valueAccessor()).source);

            var clip = new ZeroClipboard($(element), {
                moviePath: '/static/libs/zeroclipboard/zeroclipboard.swf',
                hoverClass: 'hover',
                activeClass: 'active'
            });

            clip.on('complete', function(client, args) {
                notifications.show('Code was copied into clipboard.', 2);
            });

        },
        update: function(element, valueAccessor, allBindingsAccessor, data,
                         context) {

        }
    };

    ko.bindingHandlers.displayError = {
        init: function(element, valueAccessor) {
            var errorState = valueAccessor();

            // Remove error class when typing into input
            $(element).on('focus', function() {
                if ($(element).hasClass('input-error')) {
                    $(element).removeClass('input-error');
                    errorState(false);
                }
            });
        },
        update: function(element, valueAccessor) {
            var value = ko.utils.unwrapObservable(valueAccessor());

            if (value) {
                $(element).addClass('input-error');
            } else {
                $(element).removeClass('input-error');
            }
        }
    };

    ko.bindingHandlers.collapseHandle = {
        init: function(element, valueAccessor) {
            var options = _.extend({
                show: '',
                hide: ''
            }, ko.utils.unwrapObservable(valueAccessor()));
            $(element).click(function() {
                var isCollapsed = $(element).hasClass('collapsed');
                var collapsible = $(element).data('target');
                if (isCollapsed) {
                    $(element).removeClass('collapsed').text(options.hide);
                    $(collapsible).collapse('show');
                } else {
                    $(element).addClass('collapsed').text(options.show);
                    $(collapsible).collapse('hide');
                }
            });

        }
    };

    ko.bindingHandlers.chart = {
        update: function(element, dataAccessor) {
            var $element = $(element),
                chartVM = dataAccessor(),
                chart_data = chartVM.morris_data(),
                unique_id = _.uniqueId('chart-'),
                chart,
                props;


            // The same HTML is loaded in different places so assign
            // unique id to the element. Normally we wouldn't need the ids
            // at all but that's Morris requirement.
            $element.data('chart', undefined);
            $element.attr('id', unique_id);

            // We're changing more than just data so we have to destroy
            // previous chart and create a new one.
            $element.empty();

            if (!_.isNull(chart_data)) {
                props = _.extend(
                    {
                        // ID of the element in which to draw the chart.
                        element: unique_id,
                        smooth: false,
                        parseTime: true,
                        // The name of the data record attribute that contains
                        // x-values.
                        xkey: 'dt'
                    },
                    chart_data
                );
                chart = new Morris.Line(props);
                $element.data('chart', chart);
            }
        }
    };
});
