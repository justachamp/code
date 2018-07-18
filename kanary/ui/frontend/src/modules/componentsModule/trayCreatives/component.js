// not served by presenter
define(
    ['Boiler', 'text!./view.html', 'storage', 'creative'],
    function(Boiler, template, storage, creative) {

        var Component = function(moduleContext) {
            var self = this;

            self.template = template;
            self.panel = null;

            self.vm = {
                storage: storage,
                creatives: creative.creatives,
                creative: ko.observable(null),
                newCreativeVisibillity: ko.observable(false),
                save: function() {
                    $.when(self.vm.creative().save(false))
                    .done(function(){
                        self.vm.newCreativeVisibillity(false);
                    })
                    .fail(function(){
                        self.vm.newCreativeVisibillity(true);
                    });
                },
                addNewCreative: function() {  
                    self.vm.creative(new creative.Creative()); 
                    self.vm.newCreativeVisibillity(true); 
                }
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
