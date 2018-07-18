define([
'text!../contentReport/view.html', 'strategy', 'report'
], function(template, strategy, report) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;

        self.activate = function(params) {

            var campaignName = params.campaignName,
                strategyName = params.strategyName,
                url = Urls.api_dispatch_detail('strategy', strategyName);

            self.vm = new report.Report();
            self.vm.level = 'Strategy';

            return strategy.strategyVM.fields.Get(url).then(function() {
                var now = moment();
                self.vm.slug = strategyName;
                self.vm.name = strategy.strategyVM.fields().name();

                self.vm.end_date(now);
                return self.vm.load(
                    {'end_date': now.format(CONFIG.JS_DATE_FORMAT_URL)});
            });
        };

        self.animated = function() {
            self.vm.show_chart(true);
        };
    };

    return Component;
});
