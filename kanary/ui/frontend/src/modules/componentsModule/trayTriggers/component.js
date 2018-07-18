define(
    ['Boiler', 'text!./view.html', './viewmodel', 'storage'],
    function(Boiler, template, vm, storage) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;
            this.vm = vm;

            this.activate = function(parent) {
                if (!this.panel) {
                    this.panel = new Boiler.ViewTemplate(parent, template);
                }
                ko.applyBindings(this.vm, this.panel.getDomElement());
            };
        };

        return Component;
});
