define(['router', 'notifications', 'validation', 'mixins/validation'],
function(router, notifications, validation, ValidationMixin) {

    var brands = ko.observableArray();

    function get() {
        var brands_url = Urls.api_dispatch_list('storage/brand');
        
        return $.getJSON(brands_url)
            .then(function(brands_response) {
                var brands_list = brands_response.objects;
                var newBrands = _.map(brands_list,
                function(element) {
                    return new Brand(element);
                }
            );
            brands(newBrands);
            return ko.unwrap(brands);
        });
    };

    var Brand = function(brand_fields) {

        var self = this;

        self.fields = {
            id: ko.observable(0),
            brand_id: ko.observable(),
            facebook_page_id: ko.observable(''),
            page_name: ko.observable(''),
            appnexus_access_status: ko.observable('pending'),
            check_access_status: ko.observable(true)
        };

        self.set = function(brand_fields) {
            for (var field in brand_fields) {
                if (self.fields.hasOwnProperty(field)) {
                    self.fields[field](ko.unwrap(brand_fields[field]));
                }
            }
        };

        if (brand_fields) {
            self.set(brand_fields);
        }

        /*
         * Loads brand from db based on its id
         */
        self.load = function(id) {
            var url = Urls.api_dispatch_detail_id('storage/brand', id);

            return $.getJSON(url).done(function(brand_data) {
                self.set(brand_data);
            });
        };

        self.showApiErrors = function(response) {
            var messages;
            if (response.error) {
                messages = response.error;
            } else if (response.brand) {
                messages = _.map(response.brand,
                    function(message, field) {
                        return message;
                    });
            } else {
                messages = 'There has been an error!';
            }

            notifications.showModal('Error!', messages);
        };

        /*
         * POST for new elements and PUT for sending of access request
         */
        self.save = function() {
            var url = Urls.api_dispatch_list('storage/brand'),
                successMsg = 'New brand was saved!',
                method = 'POST',
                success = function(data) { 
                    brand = new Brand(data);
                    brands.unshift(brand);
                    brand.goToDetailsView();
                    return brand;
                };
            
            if (self.fields.id()) {
                url = Urls.api_dispatch_detail_id('storage/brand', self.fields.id());
                method = 'PUT';
                successMsg = 'Access request was sent';
                success = function(data) {
                    var brand = _.find(brands(),
                        function(brand) {
                            return brand.fields.id() === data.id;
                    });
                    self.fields.check_access_status(true);
                    self.fields.appnexus_access_status('pending');
                    return brand.set(data);
                };
            }
            
            var deferred = $.Deferred();
            $.ajax({
                url: url,
                type: method,
                dataType: 'json',
                contentType: 'application/json',
                data: ko.mapping.toJSON(self.fields),
                success: function(response) {
                    var brand = success(response);
                    notifications.show(successMsg, 2);
                    deferred.resolve(brand);
                },
                error: function(jqXHR, status, error) {
                    var response = JSON.parse(jqXHR.responseText);
                    self.showApiErrors(response);
                    deferred.reject();
                }
            });
            return deferred.promise();
        };

        self.remove = function() {
            var url = Urls.api_dispatch_detail_id('storage/brand',
                                            self.fields.id());
            var deferred = $.Deferred();
            $.ajax({
                url: url,
                type: 'DELETE',
                dataType: 'json',
                contentType: 'application/json',
                statusCode: {
                    204: function() {
                        brands.remove(function(brand) {
                            return brand.fields.id() === self.fields.id();
                        });
                        deferred.resolve();
                        notifications.show('Brand was removed.', 2);
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
            router.routeTo(router.path.storage_brand({
                id: self.fields.id().toString()
            }));
        };

        self.goToListView = function() {
            router.routeTo(router.path.storage());
        };
        
        self.instruction_visible = ko.observable(false);
        self.toggle_instruction = function() {
            self.instruction_visible( !self.instruction_visible() );
        }
    };
    return {
        Brand: Brand,
        brands: brands,
        get: get
    };
});
