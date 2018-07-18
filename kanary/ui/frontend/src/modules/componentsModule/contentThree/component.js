define(
    ['text!./view.html', 'logger'],
    function(template, logger) {

    var Component = function(moduleContext) {

        this.panel = null;
        this.template = template;
        this.vm = null;
    };

    return Component;

});
