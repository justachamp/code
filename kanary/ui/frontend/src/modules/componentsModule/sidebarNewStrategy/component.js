define(
    ['text!./view.html', 'strategy'],
    function(template, strategy) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = {strategy: strategy.strategyVM};

            this.activate = function(params) {
                var dfd = $.Deferred();
                var strategyVM = strategy.strategyVM;
                strategyVM.reset();
                strategyVM.clearStepsErrors();
                strategyVM.clearInputsErrors();

                strategyVM.status('adding');
                strategyVM.site_validation_ready(true);

                strategyVM.campaign_slug(params.campaignName);

                var budget_updated = strategyVM.getCampaignBudget();
                $.when(budget_updated).done(function() {
                    strategyVM.loadDataFromTargeting(dfd);
                    strategyVM.partials.reset();
                });

                return dfd.promise();
            };

        };

        return Component;
});