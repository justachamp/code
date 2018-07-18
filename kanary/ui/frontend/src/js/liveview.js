define([],
    function() {

    INTERVAL_SECONDS = CONFIG.LIVE_VIEW_POLLING_INTERVAL;

    function Poll(results_observable, interval_seconds) {
        /**
        * Class that makes AJAX calls with given interval,
        * writing results to provided observable.
        */
        var self = this;

        self.interval_milliseconds = interval_seconds * 1000;

        /* Observable containing refreshed data */
        self.results_observable = results_observable;

        /* Active drill or null if polling is disabled*/
        self.activeDrill = null;

        /* If it is the first request after changing drill, skip timeout */
        self.skipTimeout = true;

        /* Field for storing set interval in case it needs to be cleared */
        self.timeout = null;

        self.start = function(drill) {
            self.activeDrill = drill;
            self.skipTimeout = true;
            (function poll() {
                if (drill == self.activeDrill) {
                    self.timeout = setTimeout(function() {
                        self.skipTimeout = false;
                       $.ajax({
                            url: "/liveview/" + drill + "/",
                            success: function(data) {
                                // Only update if drill hasn't changed
                                // during AJAX call
                                if (drill == self.activeDrill) {
                                    self.results_observable(data);
                                }
                            },
                            error: function(){
                                self.results_observable(null);
                            },
                            dataType: "json",
                            complete: poll
                        });
                    }, self.skipTimeout ? 0 : self.interval_milliseconds);
                }
            })();
        }

        self.stop = function() {
            self.activeDrill = null;
            if (! _.isNull(self.timeout)) {
                clearTimeout(self.timeout);
                self.timeout = null;
            }
        }
    }

    function LiveView() {
        /**
        * Viewmodel for polling AJAX resource and displaying live reports
        * for Campaign, Stragegy and Advert.
        */
        var self = this;

        self.drill = ko.observable('Campaign');
        self.drillChoices = ko.observableArray(['Campaign', 'Strategy', 'Advert']);
        self.rows = ko.observableArray();
        self.rows(null);
        self.isEnabled = ko.observable(CONFIG.LIVE_VIEW_IS_ENABLED);
        self.poll = new Poll(self.rows, INTERVAL_SECONDS);

        self.startPolling = function() {
            self.isEnabled() && self.poll.start(self.drill());
        };

        self.stopPolling = function() {
            self.poll.stop();
        }

        self.drillChanged = ko.computed(function() {
            self.stopPolling();
            self.startPolling();
        });
    }


    return {
        vm: new LiveView()
    };

});
