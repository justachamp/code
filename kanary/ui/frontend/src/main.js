'use strict';  // avoid accidental global variable declarations

require.config({
    paths: {
        // requirejs plugins in use
        text: '../libs/require/text',
        order: '../libs/require/order',
        i18n: '../libs/require/i18n',
        domReady: '../libs/require/domReady',
        path: '../libs/require/path',
        underscore: '../libs/underscore/underscore',
        components: 'modules/componentsModule',

        // namespace that aggregate core classes that are in frequent use
        Boiler: './core/_boiler_',
        router: 'js/router',
        'ui.components': 'js/ui.components',
        events: 'js/events',
        account: 'js/account',
        appcenter: 'js/appcenter',
        audience: 'js/audience',
        componentLoader: 'js/componentLoader',
        creative: 'js/creative',
        brand: 'js/brand',
        liveview: 'js/liveview',
        presenter: 'js/presenter',
        preloader: 'js/preloader',
        mixins: 'js/mixins',
        publisher_set: 'js/publisher_set',
        publishersTray: 'js/publishersTray',
        notifications: 'js/notifications',
        validation: 'js/validation',
        sidebar: 'js/sidebar',
        content: 'js/content',
        mediator: 'js/mediator',
        logger: 'js/logger',
        storage: 'js/storage',
        campaign: 'js/campaign',
        CampaignState: 'js/campaign_state',
        exchange: 'js/exchange',
        strategy: 'js/strategy',
        StrategyState: 'js/strategy_state',
        report: 'js/report',
        mockReports: 'js/mockReports',
        'reports.ui': 'js/reports.ui',
        utils: 'js/utils',
        csrf: 'js/csrf',
        'custom-bindings': 'js/custom-bindings',
        frontendReloader: 'js/frontendReloader',
        localStoragePolyfill: 'js/localStoragePolyfill'
    },
    shim: {
        underscore: {
            exports: '_'
        }
    },
    waitSeconds: CONFIG.REQUIRE_TIMEOUT,
    urlArgs: "v=" +  CONFIG.VERSION
});

/*
 * This is the main entry to the application.
 * This script is called from the main HTML file.
 *
 * Here we use the requirejs domReady plugin to run our code, once the
 * DOM is ready to be used.
 */
require(['./application', 'domReady'], function(Application, domReady) {
    domReady(function() {
        /*
         * The "./appcontext" script contains a requirejs AMD module. It
         * returns a function (not an object instance) that encapsulates the
         * logic for creating a GlobalContext. In JavaScript, functions can be
         * used as classes for OO programming. So below, we create an instance
         * by calling the 'new' operator on that function.
         */
        // new Application();
        //
        Application.init();
    });
});
