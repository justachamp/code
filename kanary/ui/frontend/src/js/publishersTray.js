define([], function() {
    var Tray = function() {
        /* Tray for choosing publisher sets from storage */
        var self = this;

        self.sets = ko.observableArray();
        self.getSets = function(inventory) {
            var deferred = $.Deferred();
            var url = Urls.api_dispatch_list('publishers/sets');

            if (inventory != undefined) {
                url += '?inventory=' + inventory;
            }
            return $.get(url).done(function(response) {
                var sets = response.objects;
                self.sets(sets);
            });
        };
    };

    var tray = new Tray();
    return {
        getSets: tray.getSets,
        sets: tray.sets
    };

});
