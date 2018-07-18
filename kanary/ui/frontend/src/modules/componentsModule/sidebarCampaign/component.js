define(['text!./view.html', 'campaign', 'router'],
function(template, campaign, router) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = {campaign: campaign.editedCampaignVM};

        self.activate = function(params) {

            var url = Urls.api_dispatch_detail(
                    'campaign', params.campaignName
                ),
                campaignVM = campaign.editedCampaignVM;

            url += '?with_strategies=true';

            return campaignVM.fields.Get(url).done(url, function() {
                campaignVM.loadStrategies();
            });
        };

        self.deactivate = function() {};
    };

    return Component;
});
