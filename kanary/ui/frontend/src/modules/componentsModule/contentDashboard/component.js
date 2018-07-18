define(
    ['text!./view.html', 'events', 'liveview'],
    function(template, events, liveview) {

        var Component = function(moduleContext) {


            this.template = template;
            this.panel = null;
            this.vm = {
                events: events,
                liveview: liveview.vm
            }

            this.activate = function(params) {
                liveview.vm.startPolling();
                return events.update();
            };

            this.deactivate = function(params) {
                liveview.vm.stopPolling();
            };

        };

        return Component;

    }
);
