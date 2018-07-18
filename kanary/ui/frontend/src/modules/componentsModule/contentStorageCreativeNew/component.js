define(
    ['text!../contentStorageCreative/view.html', 'storage', 'creative'],
    function(template, storage, creative) {

        var Component = function(moduleContext) {

            var self = this;

            self.template = template;
            self.panel = null;
            self.vm = new creative.Creative();

        };

        return Component;

    });
