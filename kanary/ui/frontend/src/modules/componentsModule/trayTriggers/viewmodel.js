define(['mediator'], function(mediator) {

    var leftMenuHilight = ko.observable();

    function init() {
        mediator.listen('URL_CHANGE', function(params) {
            leftMenuHilight(params.menu);
        });
    }

    return {
        init: init,
        leftMenuHilight: leftMenuHilight
    };

});
