define(
    ['text!./view.html', 'router', 'strategy'],
    function(template, router, strategy) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = {strategy: strategy.strategyVM};

            this.activate = function(params) {
                var strategySlug = params.strategyName,
                    campaignSlug = params.campaignName,
                    url = Urls.api_dispatch_detail('strategy',
                                                   params.strategyName),
                    d = $.Deferred();
                strategy.strategyVM.campaign_slug(campaignSlug);
                strategy.strategyVM.strategy_slug(strategySlug);

                strategy.strategyVM.fields.Get(url, function() {
                    d.resolve();
                });

                return d.promise();
            };

            this.deactivate = function(params) {
                this.vm = {};
            };

        };

        return Component;
});
