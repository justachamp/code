define(
    ['text!./view.html', 'logger'],
    function(template, logger) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = null;

    };

    return Component;

});
