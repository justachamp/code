define(
    ['text!./view.html', './viewmodel'],
    function(template, vm) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = vm.CampaignList;

        this.activate = function(params) {
            return vm.CampaignList.loadCampaigns();
        };

    };

    return Component;
});
