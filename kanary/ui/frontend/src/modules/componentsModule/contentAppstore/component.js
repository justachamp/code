define(
    ['text!./view.html', 'logger', 'appcenter'],
    function(template, logger, appcenter) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = appcenter;

    };

    return Component;

});
