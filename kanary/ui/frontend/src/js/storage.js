define(['router', 'notifications', 'creative', 'audience', 'brand', 'publishersTray'],
function(router, notifications, creative, audience, brand, publishersTray) {

    var Storage = function() {

        var self = this,
            draggableRevertDuration = 200;

        self.trays = {
            audiences: null,
            creatives: null,
            brands: null,
            triggers: null,
            publishers: null,
            current: null
        };
      
        self.creativesDestination = ko.observable('default');

        self.trayOpenedBy = null;

        self.stats = {
            creatives: ko.computed(function() {
                return creative.creatives().length;
            }),
            audiences: ko.computed(function() {
                return audience.audiences().length;
            }),
            brands: ko.computed(function() {
                return brand.brands().length;
            }),
            triggers: ko.observable(0)
        };

        self.hideTray = function() {
            if (!self.trays['current'])
                return;
            self.trays['current'].hide();
            self.trays['current'] = null;
            self.trayOpenedBy = null;
        };

        /**
            Passes element, which was clicked in tray to element,
            which opened it
         */
        self.clickTrayElement = function(element) {
            if (self.trayOpenedBy &&
                _.isFunction(self.trayOpenedBy.receiveFromTray)) {
                    self.trayOpenedBy.receiveFromTray(element);
            }
            self.hideTray();
        };

        /**
            Opens tray for given element, so it can receive objects
            from tray.
         */
        self.showCreativesTrayFor = function(postfix, creative) /*this order for correct bind in template*/ {
            if (postfix=='d') {
                self.creativesDestination = 'default';
            } else {
                self.creativesDestination = 'facebook_sidebar';  
            }
            self.showCreativesTray(postfix);
            self.trayOpenedBy = creative;
        };

        self.showPublishersTrayFor = function(publisherSet, type) {
            self.showPublishersTray(type);
            self.trayOpenedBy = publisherSet;
        };

        self.showAudiencesTrayFor = function(openingVM) {
            self.showAudiencesTray();
            self.trayOpenedBy = openingVM;
        };

        self.slideInTray = function(component) {

            if (self.trays['current'] === component) {
                return;
            }

            self.trays['current'] = component;
            component.show();
        };

        self.toggleCreativesTray = function() {
            if (self.trays['current'] === self.trays['creatives']) {
                self.hideTray();
            } else {
                self.slideInTray(trays['creatives']);
            }
        };

        self.showCreativesTray = function(postfix) {
            return self.init(postfix).done(function() {
                self.slideInTray(self.trays['creatives']);
            });
        };

        self.showPublishersTray = function(type) {
            publishersTray.getSets(type).done(function(sets) {
                self.slideInTray(self.trays['publishers']);
            });
        };

        self.showTriggersTray = function() {
            self.slideInTray(self.trays['triggers']);
        };

        self.showAudiencesTray = function() {
            self.slideInTray(self.trays['audiences']);
        };

        /**
            Initializes storage object. Reads creatives from backend,
            and puts them into storage.creatives array
         */
        self.init = function(postfix) {
            return $.when(creative.get(postfix), audience.get(), brand.get());
        };
    };

    return new Storage();

});