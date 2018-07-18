define([], function() {

    function trace(deferred) {

        // deffered - Knockout RESET object
        // https://github.com/frapontillo/knockout-rest

        isModified = ko.computed(function() {
            if (deferred.isUpdating()) {
                // start preloader
                $('.preloader').show();
            } else {
                if (deferred.isError()) {
                    // error while ajax call
                    alert('ERROR');
                } else {
                    // stop preloader
                    $('.preloader').hide();
                }
            }
        });

    }

    return {
        trace: trace
    };
});
