define(
    ['text!../contentNewCampaignCapping/view.html', 'campaign'],
    function(template, campaign) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = campaign.editedCampaignVM;

    };

    return Component;
});
