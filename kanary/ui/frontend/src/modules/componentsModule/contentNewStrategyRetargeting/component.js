define(
    ['text!./view.html', 'logger'],
    function(template, logger) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = null;

        this.activate = function(params) {
            var d = $.Deferred();

            strategy.strategyVM.getStep();

            d.resolve();
            return d.promise();
        };

    };

    return Component;

});
