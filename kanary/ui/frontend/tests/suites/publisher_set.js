define(['models/publisher_set'], function(publisher_set) {
    suite('Publisher Manater', function() {
        suite('Tray', function() {
            var mockPublisherSets = [
                {
                    id: 1,
                    name: 'Mobile set',
                    type: 'mobile',
                    publishers: [
                        {
                            id: 19,
                            name: 'mobile 19',
                            type: 'mobile',
                            network: 'Appnexus'
                        }
                    ]
                },
                {
                    id: 2,
                    name: 'Web set',
                    type: 'web',
                    publishers: [
                        {
                            id: 22,
                            name: 'web 22',
                            type: 'web',
                            network: 'Facebook'
                        }
                    ]
                },
                {
                    id: 3,
                    name: 'Network set',
                    type: 'network',
                    publishers: [
                        {
                            id: 33,
                            name: 'network 33',
                            type: 'network'
                        }
                    ]
                }
            ];
            test('sets should be an array', function() {
                chai.assert.isArray(publisher_set.sets());
            });
            suiteSetup(function() {
                $.mockjax({
                    url: Urls.api_dispatch_list('storage/publisher_set'),
                    dataType: 'json',
                    responseText: JSON.stringify(mockPublisherSets)
                });
            });
            suiteTeardown(function() {
                $.mockjaxClear();
            });
            test('getSets() should fill sets array', function(done) {
                publisher_set.getSets().done(function() {
                    chai.assert.lengthOf(
                        publisher_set.sets(),
                        mockPublisherSets.length,
                        'sets array has lenght equal to mock data'
                    );
                    done();
                }).fail(function() {
                    chai.assert.fail('response', 'error', 'AJAX error');
                    done();
                });
            });
        });
    });
});
