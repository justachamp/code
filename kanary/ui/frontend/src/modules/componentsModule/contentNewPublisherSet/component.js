define(
    ['text!./view.html', 'logger', 'storage', 'strategy', 'publisher_set'],
    function(template, logger, storage, strategy, publisher_set) {
    var Component = function(moduleContext) {

        var self = this;

        this.template = template;
        this.panel = null;
        this.vm = {
            strategy: strategy.strategyVM,
            showPublishersTray: storage.showPublishersTrayFor
        };

        this.activate = function(params) {
            var deferred = $.Deferred();
            strategy.strategyVM.getStep();
            var partials = strategy.strategyVM.partials;
            partials.loaded.done(function() {
                var publishers = partials.publishers;
                self.vm.selectedPublishers = publishers.selectedPublishers;
                self.vm.searchResults = publishers.searchResults;
                self.vm.type = publishers.type;
                self.vm.blacklist = publishers.blacklist;
                deferred.resolve();
            });
            return deferred.promise();
        };
    };
    return Component;
});
