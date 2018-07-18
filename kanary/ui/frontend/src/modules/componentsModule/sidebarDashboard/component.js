define(['text!./view.html', 'events'],
function(template, events) {

    var Component = function(moduleContext) {

        this.template = template;
        this.panel = null;
        this.vm = events;

        this.activate = function(params) {
            return events.categories_update();
        };

    };

    return Component;
});
