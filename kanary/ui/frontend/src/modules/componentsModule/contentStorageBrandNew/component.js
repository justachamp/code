define(
    ['text!../contentStorageBrand/view.html', 'storage', 'brand'],
    function(template, storage, brand) {

        var Component = function(moduleContext) {

            var self = this;

            self.template = template;
            self.panel = null;
            self.vm = new brand.Brand();

        };

        return Component;

    });
