define(
    ['text!./view.html', 'storage', 'audience'],
    function(template, storage, audience) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = new audience.Audience();

            this.activate = function(params) {

                if (audience.audiences().length === 0) {
                    return storage.init();
                }

                return $.Deferred().resolve();
            };

            this.onUrlChange = function(params) {
                var currentAudience = this.vm;

                // Refresh audiences list and fetch audience based on its id
                return audience.get().done(function() {
                    currentAudience.load(params.id);
                });
            };
        };

        return Component;
    });
