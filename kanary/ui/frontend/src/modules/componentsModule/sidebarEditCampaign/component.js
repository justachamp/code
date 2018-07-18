define(
    ['text!../sidebarNewCampaign/view.html', 'campaign'],
    function(template, campaign) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = campaign.editedCampaignVM;

        self.activate = function(params) {
            var d = $.Deferred();

            var slug = params.campaignName;

            campaign.editedCampaignVM.mode('edit');
            campaign.editedCampaignVM.clearStepsErrors();
            campaign.editedCampaignVM.clearInputsErrors();
            campaign.editedCampaignVM.getStepFromHash();

            campaign.editedCampaignVM.fields.Get(
                Urls.api_dispatch_detail('campaign', slug) +
                '?with_strategies=true', function() {
                    d.resolve();
                }
            );

            return d.promise();
        };

        self.deactivate = function() {};

    };

    return Component;
});
