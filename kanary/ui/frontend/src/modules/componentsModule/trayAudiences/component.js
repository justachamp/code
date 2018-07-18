// not served by presenter
define(
    ['Boiler', 'text!./view.html', 'storage', 'audience'],
    function(Boiler, template, storage, audience) {

        var Component = function(moduleContext) {
            var self = this;

            self.template = template;
            self.panel = null;

            self.vm = {
                storage: storage,
                audiences: audience.audiences
            };

            self.activate = function(parent) {
                // vm is in storage.js
                if (!self.panel) {
                    self.panel = new Boiler.ViewTemplate(parent, template);
                }
                ko.applyBindings(self.vm, self.panel.getDomElement());
            };

            self.hide = function() {
                self.panel.getJQueryElement().parent().animate({
                    right: '-417px'
                }, 400, function() {
                });
            };

            self.show = function() {
                var panel = self.panel.getJQueryElement().parent();
                panel.css({
                        'z-index': 7,
                        right: 0
                 }).animate({}, 400, function() {
                        $('section.tray').css('z-index', 0);
                        panel.css('z-index', 6);
                        panel.removeClass('hide');
                });
            };
        };

        return Component;
});
