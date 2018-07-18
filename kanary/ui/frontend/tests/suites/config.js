var baseConfig = {
    paths: {
        'models': 'src/js',
        'tests': 'tests/suites'
    },
    shim: {
    },
    baseUrl: '../'
};

console.log('loading config');
mocha.setup('tdd');
var publisherSetTest = new TestSuite({
    modules: [
        'models/publisher_set', 'tests/publisher_set'
    ],
    stubs: {
        notifications: {},
        strategy: {}
    },
    globals: {
        Urls: {
            'api_dispatch_list': function() { return '';}
        }
    },
    config: baseConfig
});

publisherSetTest.run();
