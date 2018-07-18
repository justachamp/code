define(
    ['text!../contentNewADXRTBReporting/view.html', 'logger', 'campaign'],
    function(template, logger, campaign) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = campaign.newCampaignVM;

    };

    return Component;

});
