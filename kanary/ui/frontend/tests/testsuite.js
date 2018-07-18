var TestSuite = (function() {
    var uniqueId = 0;
    function createContext(stubs, baseConfig) {
        /* Making sure mock component names are not duplicated */
        uniqueId++;
        var map = {};

        _.each(stubs, function(value, key) {
            var stubName = 'stub' + key + uniqueId;
            map[key] = stubName;

            define(stubName, function() {
                return value;
            });
        });

        return require.config(
            _.extend(baseConfig, {
                context: 'context_' + uniqueId,
                map: {
                    '*': map
                }
            })
        );
    }

    var TestSuite = function(options) {
        var self = this;
        var defaults = {
            modules: [],
            stubs: {},
            globals: {},
            config: {}
        };
        _.extend(self, defaults, options);
        self.componentContext = createContext(self.stubs, self.config);
        self.defineGlobals = function() {
            _.extend(window, self.globals);
        };
        self.run = function() {
            self.defineGlobals();
            self.componentContext(self.modules, function() {
                if (navigator.userAgent.indexOf('PhantomJS') < 0) {
                    mocha.run();
                } else {
                    mochaPhantomJS.run();
                }
            });
        };
    };

    return TestSuite;
})();
