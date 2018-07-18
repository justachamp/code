define(['router', 'notifications'],
function(router, notifications) {

    var audiences = ko.observableArray();

    function get() {
        var audiences_url = Urls.api_dispatch_list('storage/audience');
        var filter = '?is_deleted=False';
        return $.getJSON(audiences_url + filter)
            .then(function(audiences_response) {
                var audiences_list = audiences_response.objects;
                var newAudiences = _.map(audiences_list,
                function(element) {
                    return new Audience(element);
                }
            );
            audiences(newAudiences);
            return ko.unwrap(audiences);
        });
    };

    var Audience = function(audience_fields) {

        var self = this;

        self.fields = {
            id: ko.observable(0),
            id_random: ko.observable(''),
            name: ko.observable(''),
            tracking_code: ko.observable(''),
            piggyback_url: ko.observable('')
        };

        self.set = function(audience_fields) {
            for (var field in audience_fields) {
                if (self.fields.hasOwnProperty(field)) {
                    self.fields[field](ko.unwrap(audience_fields[field]));
                }
            }
        };

        if (audience_fields) {
            self.set(audience_fields);
        }

        /*
         * Loads audience from db based on its id
         */
        self.load = function(id) {
            var url = Urls.api_dispatch_detail_id('storage/audience', id);

            return $.getJSON(url).done(function(audience_data) {
                self.set(audience_data);
            });
        };

        self.showApiErrors = function(response) {
            var messages;
            if (response.error) {
                messages = response.error;
            } else if (response.audience) {
                messages = _.map(response.audience,
                    function(message, field) {
                        return message;
                    });
            } else {
                messages = 'There has been an error!';
            }

            notifications.showModal('Error!', messages);
        };

        self.create = function() {
            var audience;
            var url = Urls.api_dispatch_list('storage/audience'),
                method = 'POST',
                success = function(data) {
                    audience = new Audience(data);
                    audiences.unshift(audience);

                };
            var deferred = $.Deferred();
            $.ajax({
                url: url,
                type: method,
                dataType: 'json',
                contentType: 'application/json',
                data: ko.mapping.toJSON(self.fields),
                success: function(response) {
                    success(response);
                    deferred.resolve(audience);
                },
                error: function(jqXHR, status, error) {
                    var response = JSON.parse(jqXHR.responseText);
                    self.showApiErrors(response);
                    deferred.reject();
                }
            });
            return deferred.promise();
        };

        self.createAndShowDetails = function() {
            self.create().done(function(audience) {
                audience.goToDetailsView();
            });
        };

        self.save = function() {
            var url = Urls.api_dispatch_detail_id('storage/audience',
                            self.fields.id());
                method = 'PUT';
                success = function(data) {
                    var audience = _.find(audiences(),
                        function(audience) {
                            return audience.fields.id() === data.id;
                    });
                    audience.set(data);
                };
            $.ajax({
                url: url,
                type: method,
                dataType: 'json',
                contentType: 'application/json',
                data: ko.mapping.toJSON(self.fields),
                success: function(response) {
                    success(response);
                },
                error: function(jqXHR, status, error) {
                    var response = JSON.parse(jqXHR.responseText);
                    self.showApiErrors(response);
                }
            });
        };

        self.remove = function() {
            var url = Urls.api_dispatch_detail_id('storage/audience',
                                            self.fields.id());
            var deferred = $.Deferred();
            $.ajax({
                url: url,
                type: 'DELETE',
                dataType: 'json',
                contentType: 'application/json',
                statusCode: {
                    204: function() {
                        audiences.remove(function(audience) {
                            return audience.fields.id() === self.fields.id();
                        });
                        deferred.resolve();
                        notifications.show('Audience was removed.', 2);
                    }
                }
            });
            return deferred.promise();
        };

        self.removeAndShowList = function() {
            self.remove().done(function() {
                self.goToListView();
            });
        };

        self.goToDetailsView = function() {
            router.routeTo(router.path.storage_audience({
                id: self.fields.id().toString()
            }));
        };

        self.goToListView = function() {
            router.routeTo(router.path.storage());
        };

    };
    return {
        Audience: Audience,
        audiences: audiences,
        get: get
    };
});
