define(
    ['text!./view.html', 'storage', 'creative', 'audience', 'brand'],
    function(template, storage, creative, audience, brand) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = {
                storage: storage,
                creatives: creative.creatives,
                audiences: audience.audiences,
                brands: brand.brands 
            };
            this.activate = function(params) {
                return this.vm.storage.init();
            };
        };

        return Component;
});
