define(
    ['text!../contentNewStrategyCreatives/view.html', 'logger',
    'storage', 'strategy'],
    function(template, logger, storage, strategy) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = {
            strategy: strategy.strategyVM,
            showCreativesTray: storage.showCreativesTrayFor
        };

        this.activate = function(params) {

            strategy.strategyVM.getStep();

            return $.Deferred().resolve();
        };
    };

    return Component;

});
