define(['text!./modules/componentsModule/modalWindow/view.html',
        'text!./modules/componentsModule/httpErrorWindow/view.html', 'router',
        'mediator'],
function(modalView, httpErrorView, router, mediator) {

    function init() {
        $('<div></div>', { 'id': 'notifications' }).appendTo('body');
        $('<div></div>', { 'id': 'preloader' }).appendTo('body');
        $(modalView).appendTo('body');
        $(httpErrorView).appendTo('body');

        $(document).ajaxStart(function() {
            window.setTimeout(
                function() {
                    if ($.active != 0) {
                       preloader.showPreloader('Loading...');
                       preloader.element.delay(preloader.minPreloaderDuration);
                    }
                }, preloader.minRequestDuration
            );
        });

        $(document).ajaxStop(function() {
            if ($.active === 0) {
               preloader.hidePreloader();
           }
        });

        // Hook into jQuery XHR response failure callback. Send errors to raven
        // and display error overlay.
        $(document).ajaxError(function(event, jqXHR, settings) {
            // We are not showing http error for validation errors.
            if (jqXHR.status <= 400) {
                return;
            }

            var debug_info = _.extend(
                    _.pick(jqXHR, 'status', 'statusText'),
                    _.pick(settings, 'type', 'url', 'data', 'contentType')
                ),
                msg;

            msg = 'XHR failed on ' + debug_info.url + ' with code: ' +
                debug_info.status;
            Raven.captureMessage(msg, {'xhr': debug_info});

            HttpError.load(jqXHR);
            $('#http-error').show();
        });

        // Hide http error view on hash change
        mediator.listen('URL_CHANGE', function() {
            var httpErrorView = $('#http-error');

            if (httpErrorView.is(':visible')) {
                httpErrorView.hide();
            }
        });

        ko.applyBindings({modalVM: modalVM}, $('#modal')[0]);
        ko.applyBindings({HttpError: HttpError}, $('#http-error')[0]);
    };

    var toastElement = $('<div></div>', { 'class': 'toast-message'});

    function Notification() {
        var self = this;

        // container to which notification element is appended
        var container = '#notifications';

        // notifications queue
        self.queue = ko.observableArray();
        // ready=True means that no notification is displayed
        self.ready = ko.observable(true);

        self.animateQueue = ko.computed(function() {
            // show notification when there is new element in queue
            // and no other notification is displayed
            if (!self.ready() || self.queue().length === 0) {
                return;
            }
            var text = self.queue()[0].text,
                timer = self.queue()[0].timer,
                element = toastElement.html('<p>' + text + '</p>');

            self.ready(false);
            animate(element, container, timer, function() {
                self.queue.remove(self.queue()[0]);
                self.ready(true);
            });

        }, self);
    }

    function Preloader() {
        var self = this;

        // preloader element which is actually shown
        self.element = $();
        // container to which preloader element is appended
        self.container = '#preloader';

        // time settings in miliseconds
        self.minPreloaderDuration = 500;
        self.minRequestDuration = 500;

        self.showPreloader = function(text) {
            var insideHTML = '<p><i class="loader"></i> ' + text + '</p>',
                element = toastElement.html(insideHTML);

            self.element = element;
            showToast(element, self.container, text);
        };

        self.hidePreloader = function() {
            hideToast(self.element);
        };
    }

    function HttpError() {
        var self = this;

        self.status = ko.observable();
        self.statusText = ko.observable();

        self.load = function(jqXHR) {
            self.status(jqXHR.status);
            self.statusText(jqXHR.statusText);
        };
    }

    function modalVM() {
        var self = this,
            modalType = {
                alert: 'alert',
                confirm: 'confirm',
                custom: 'custom'
            };

        self.title = ko.observable('');
        self.content = ko.observable('');
        self.isOpened = ko.observable(false);
        self.type = ko.observable('');

        // Action function connected with confirm dialog
        self.confirmFunction = function() {};
        self.rejectFunction = function() { return false };

        self.showModal = function(title, content) {
            self.title(title);
            self.content(content);
            self.type(modalType.alert);
            self.isOpened(true);
        };

        /**
         * Usage of confirm dialog:
         *
         * Calling this function opens the confirm box, with options based
         * on parameters passed to function:
         *
         * title, content - strings that represent text displayed in modal
         * confirm - function that is fired when user click 'ok'
         * reject - action that is performed when user click 'cancel'
         *          (this function is not required, default behavior
         *          is to close modal widow without any action)
         *
         * Don't close modal manually inside callback functions!
         * (confirm/reject) It's already done inside implementation.
         *
         */
        self.confirmDialog = function(title, content, confirm, reject) {
            self.confirmFunction = confirm;
            if (reject) {
                self.rejectFunction = reject;
            }

            self.showModal(title, content);
            self.type(modalType.confirm);
        };

        self.confirm = function() {
            self.confirmFunction();
            self.closeModal();
        };

        self.reject = function() {
            self.rejectFunction();
            self.closeModal();
        };

        self.customDialog = function(title, viewModel, template) {
            self.showModal(title);
            self.template = template;
            self.customVM = viewModel;
            self.type(modalType.custom);
        };

        self.closeModal = function() {
            self.isOpened(false);
        };
    }

    var notifications = new Notification();
    var preloader = new Preloader();
    var modalVM = new modalVM();
    var HttpError = new HttpError();

    // HELPER FUNCTIONS

    function showToast(element, container, callback) {
        element.appendTo(container).delay(10).queue(function(next) {
            element.addClass('in');
            _.isFunction(callback) && callback();
            next();
        });
    }

    function hideToast(element, callback) {
        element.queue(function(next) {
            element.removeClass('in');
            next();
        }).delay(100).queue(function(next) {
            element.remove();
            _.isFunction(callback) && callback();
        });
    }

    function animate(element, container, timer, callback) {
        // jQuery animation of single notification

        showToast(element, container);
        element.delay(timer * 1000);
        hideToast(element, callback);
    }

    function show(text, timer) {
        // Adding notification to notifications queue
        // text (text): text or HTML
        // timer (integer): visibility time (in seconds), default: 5

        var self = this;

        // default timer
        var timer = typeof timer !== 'undefined' ? timer : 5;

        notifications.queue.push({
            text: text,
            timer: timer
        });

    };

    return {
        init: init,
        show: show,
        showModal: modalVM.showModal,
        confirmDialog: modalVM.confirmDialog,
        customDialog: modalVM.customDialog,
        closeModal: modalVM.closeModal
    };
});
