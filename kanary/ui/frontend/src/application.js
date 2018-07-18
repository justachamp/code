var requirements = [
    'Boiler', './modules/modules', 'router', 'mediator', 'sidebar', 'content',
    'componentLoader', 'logger', 'js/customControls', 'presenter', 'preloader',
    'notifications', 'custom-bindings', 'account', 'events', 'frontendReloader',
    'csrf'
];
define(requirements, function(
    Boiler, moduleContexts, router, mediator, sidebar, content,
    componentLoader, logger, customControls, presenter, preloader,
    notifications, customBindings, account, events, frontendReloader,
    csrf) {

    function init() {

        logger.info('Initializing application ...');

        mediator.init();
        router.init();
        componentLoader.init();
        sidebar.init();
        content.init();
        presenter.init();
        notifications.init();
        csrf.init();
        customControls.init();

        account.init();
        events.init();
        frontendReloader.init();

        //Create our root context instance
        var appContext = new Boiler.Context();

        // commenting this line breaks up application
        appContext.loadChildContexts(moduleContexts);

        hasher.changed.dispatch(hasher.getHash());
    }

    return {
        init: init
    };

});
