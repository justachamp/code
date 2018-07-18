define(
    ['text!./view.html', 'logger', 'storage', 'strategy'],
    function(template, logger, storage, strategy) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = {strategy: strategy.strategyVM};

        this.activate = function(params) {
            var d = $.Deferred();

            strategy.strategyVM.getStep();

            d.resolve();
            return d.promise();
        };

    };

    return Component;

});
