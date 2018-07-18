define(
    ['text!../contentStorageAudience/view.html', 'storage', 'audience'],
    function(template, storage, audience) {

        var Component = function(moduleContext) {

            var self = this;

            self.template = template;
            self.panel = null;
            self.vm = new audience.Audience();

        };

        return Component;

    });
