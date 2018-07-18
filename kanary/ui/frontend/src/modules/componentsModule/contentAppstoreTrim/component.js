define(
    ['text!./view.html', 'appcenter'],
    function(template, appcenter) {

        var Component = function(moduleContext) {
            var self = this;

            self.template = template;
            self.panel = null;
            self.vm = appcenter;
        };

        return Component;
});
