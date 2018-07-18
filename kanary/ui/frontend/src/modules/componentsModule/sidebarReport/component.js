define(
    ['text!./view.html', 'report'],
    function(template, report) {

        var Component = function(moduleContext) {
            var self = this;

            self.template = template;
            self.panel = null;
            self.vm = report.presentation;

        };

        return Component;
    }
);
