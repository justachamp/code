// this component is not served by presenter!
define(
    ['Boiler', 'text!./view.html', './viewmodel'],
    function(Boiler, template, vm) {

        var Component = function(moduleContext) {

            this.template = template;
            this.panel = null;

            this.activate = function(parent) {
                if (!this.panel) {
                    this.panel = new Boiler.ViewTemplate(parent, template);
                    vm.init();
                }
                ko.applyBindings(vm, this.panel.getDomElement());
            };

        };

        return Component;
});
