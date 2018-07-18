define([
    'Boiler',
    'storage',
    './leftMenu/component',
    './trayCreatives/component',
    './trayTriggers/component',
    './trayPublishers/component',
    './trayAudiences/component'],

    function(
        Boiler,
        storage,
        LeftMenuComponent,
        TrayCreativesComponent,
        TrayTriggersComponent,
        TrayPublishersComponent,
        TrayAudiencesComponent) {

        var Module = function(globalContext) {

            var context = new Boiler.Context(globalContext);

            domController = new Boiler.DomController($('body'));

            storage.trays['triggers'] = new TrayTriggersComponent(context);
            storage.trays['creatives'] = new TrayCreativesComponent(context);
            storage.trays['publishers'] = new TrayPublishersComponent(context);
            storage.trays['audiences'] = new TrayAudiencesComponent(context);
            storage.trays['brands'] = new TrayAudiencesComponent(context);

            domController.addRoutes({
                '#left-menu' : new LeftMenuComponent(context),
                '#trayCreatives': storage.trays['creatives'],
                '#trayTriggers': storage.trays['triggers'],
                '#trayPublishers': storage.trays['publishers'],
                '#trayAudiences': storage.trays['audiences'],
                '#trayBrands': storage.trays['brands']
            });

            domController.start();

        };

        return Module;
});
