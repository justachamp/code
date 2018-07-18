define(
    ['text!../contentNewStrategyBidding/view.html', 'logger',
    'strategy'],
    function(template, logger, strategy) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = strategy.strategyVM;

        this.activate = function(params) {
            var d = $.Deferred();

            strategy.strategyVM.getStep();

            // time picker
            $('.timepicker-input input').timepicker({showMeridian: false});

            d.resolve();
            return d.promise();
        };

    };

    return Component;

});
