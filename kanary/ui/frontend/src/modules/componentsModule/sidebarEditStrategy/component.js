define(
    ['text!../sidebarNewStrategy/view.html', 'strategy', 'router'],
    function(template, strategy, router) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = {strategy: strategy.strategyVM};

            this.activate = function(params) {
                var strategy_name = params.strategyName,
                    campaign_name = params.campaignName,
                    url = Urls.api_dispatch_detail('strategy', strategy_name),
                    deferred = $.Deferred(),
                    strategyVM = strategy.strategyVM;

                strategyVM.status('editing');
                // turn off validation
                strategyVM.site_validation_ready(false);
                strategyVM.clearStepsErrors();
                strategyVM.clearInputsErrors();

                strategyVM.strategy_slug(strategy_name);
                strategyVM.campaign_slug(campaign_name);

                strategyVM.fields.Get(url, function() {
                }).done(function() {
                    strategyVM.applyCustomMapping();
                    strategyVM.loadDataFromTargeting(deferred);
                    strategyVM.partials.reset();
                    deferred.resolve();
                });

                return deferred.promise();
            };

        };

        return Component;
});
