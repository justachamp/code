define(
    ['text!../contentNewStrategy/view.html', 'logger', 'strategy', 'router'],
    function(template, logger, strategy, router) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = {strategy: strategy.strategyVM};

        this.activate = function(params) {
            var d = $.Deferred(),
                url = Urls.api_dispatch_detail('strategy', params.strategyName);

            strategy.strategyVM.getStep();

            // Get campaign slug
            strategy.strategyVM.campaign_slug(params.campaignName);
            strategy.strategyVM.getCampaignBudget().done(function() {
                d.resolve();
            });

            return d.promise();
        };
    };

    return Component;

});
