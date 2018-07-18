define(
    ['text!./view.html', './viewmodel'],
    function(template, reportsVM) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = reportsVM;

            this.activate = function(params) {
                return reportsVM.load();
            };

        };

        return Component;
});
