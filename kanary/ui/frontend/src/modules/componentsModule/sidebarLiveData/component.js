define(
    ['text!./view.html'],
    function(template) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = null;

        };

        return Component;
});
