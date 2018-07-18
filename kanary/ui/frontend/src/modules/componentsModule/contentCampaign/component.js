define(
    ['text!../contentReport/view.html', 'campaign', 'report'],
    function(template, campaign, report) {
    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = report.report;

        self.activate = function(params) {
            var campaignName = params.campaignName,
                url = Urls.api_dispatch_detail('campaign', campaignName) +
                    '?' + $.param({format: 'json', with_strategies: true});

            self.vm = new report.Report();
            self.vm.level = 'Campaign';

            return campaign.editedCampaignVM.fields.Get(url).done(
                function() {
                    var now = moment();
                    campaign.editedCampaignVM.loadStrategies();
                    self.vm.name =
                        campaign.editedCampaignVM.fields().name();
                    self.vm.slug =
                        campaign.editedCampaignVM.fields().slug();

                    self.vm.end_date(now);
                    self.vm.load({
                        'end_date': now.format(CONFIG.JS_DATE_FORMAT_URL)
                    });
                }
            );
        };

        self.animated = function() {
            self.vm.show_chart(true);
        };
    };

    return Component;
});
