define(
    ['text!./view.html'],
    function(template) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = null;

            this.activate = function(params) {
                var d = $.Deferred();

                // Hmm, for what is it?
                if (params) {
                    sidebarHighlight = params.sidebarHighlight || false;

                    if (sidebarHighlight) {
                        this.panel.getJQueryElement()
                            .find('.current').removeClass('current');
                        this.panel.getJQueryElement()
                            .find('#' + sidebarHighlight)
                            .addClass('current');
                    }
                }

                d.resolve();
                return d.promise();
            };

        };

        return Component;
});
