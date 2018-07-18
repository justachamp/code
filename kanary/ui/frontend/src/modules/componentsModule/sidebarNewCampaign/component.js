define(
    ['text!./view.html', 'campaign'],
    function(template, campaign) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = campaign.newCampaignVM;

        this.activate = function(params) {
            var d = $.Deferred();

            campaign.newCampaignVM.clearStepsErrors();
            campaign.newCampaignVM.clearInputsErrors();
            campaign.newCampaignVM.getStepFromHash();

            d.resolve();
            return d.promise();
        };

    };

    return Component;
});
