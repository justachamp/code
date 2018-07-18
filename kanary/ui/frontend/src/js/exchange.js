define([], function() {

    function Exchange(id, name, selected) {
        this.id = ko.observable(id);
        this.name = ko.observable(name);
        this.selected = ko.observable(selected || false);
    }

    function ExchangeVM() {
        var self = this;

        self.getExchanges = function(handler) {
            var json_handler = function(response) {
                handler(response.objects);
            };
            $.getJSON(Urls.api_dispatch_url('exchange'), json_handler);
        };
    }
    return {
        ExchangeVM: new ExchangeVM(),
        Exchange: Exchange
    };
});
