define(['mediator', 'router', 'events'],
    function(mediator, router, events) {

        var leftMenuHilight = ko.observable();

        function init() {
            mediator.listen('URL_CHANGE', function(params) {
                leftMenuHilight(params.menu);
            });
        }

        return {
            init: init,
            router: router,
            events: events,
            leftMenuHilight: leftMenuHilight
        };

});
