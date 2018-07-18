define(['router', 'notifications', 'utils', 'brand'],
function(router, notifications, utils, brand) {

    var creatives = ko.observableArray();

    function get(postfix) {
        var postfix = postfix || '',
            creatives_url = Urls.api_dispatch_list('storage/creative'),
            data = {};
        if (postfix != '')
            data = {
                destination__startswith: postfix
            };
      
        return $.getJSON(creatives_url, data)
            .then(function(creatives_response) {
                var creative_list = creatives_response.objects;
                var newCreatives = _.map(creative_list,
                    function(element) {
                        return new Creative(element);
                    }
                );
                creatives(newCreatives);
                return ko.unwrap(creatives);
            });
    };

    var Creative = function(creative_data) {

        var self = this;

        self.fields = {
            id: ko.observable(0),
            type: ko.observable('Image'),
            name: ko.observable(''),
            height: ko.observable(0),
            width: ko.observable(0),
            api_data: ko.observable(''),
            status: ko.observable('pending'),
            liverail_status: ko.observable('pending'),
            vast_url: ko.observable(''),
            to_audit: ko.observable(false),
            is_auditable: ko.observable(false),
            destination: ko.observable('default'),
            fb_title: ko.observable(null),
            fb_body: ko.observable(null),
            fb_message: ko.observable(null),
            fb_domain: ko.observable(null),
            fb_brand_page: ko.observable(null),
            fb_brand_page_access: ko.observable(''),
            strategy: ko.observable('')
        };
      
        /* For binding of facebook newsfeed and facebook brand page */
        self.available_brands = ko.computed(function() {
            return _.filter(brand.brands(), function(brand){
                return ((brand.fields.appnexus_access_status() == 'confirmed') ||
                        (brand.fields.id() == self.fields.fb_brand_page()));
            })
        });
        
        self.isCreativeTypeFB = function() {
            return (self.fields.destination()=='facebook_sidebar' ||
                    self.fields.destination()=='facebook_newsfeed');
        };

        /**
         * Checks if all conditions for displaying given
         * creative type preview are met for currently chosen one.
         */
        self.is_preview_visible = ko.computed(function() {
            var type = self.fields.type(),
                api_data = self.fields.api_data(),
                liverail_status = self.fields.liverail_status();

            // Video creatives preview is visible only after succesful transcoding
            return (
                (type === 'Video' && liverail_status === 'active' && api_data) ||
                (type !== 'Video' && api_data !== '')
            );
        });

        /**
            Sets data on this object based on object passed.
            Object can contain simple attributes or observables

            @param {object} creative_data - creative data to be set on
                this creative object.
         */
        self.set = function(creative_data) {
            for (var key in creative_data) {
                if (creative_data.hasOwnProperty(key) &&
                    self.fields.hasOwnProperty(key)) {
                    if (ko.isObservable(creative_data[key])) {
                        self.fields[key](creative_data[key]());
                    } else {
                        self.fields[key](creative_data[key]);
                    }
                }
            }
        };

        if (creative_data) {
            self.set(creative_data);
        }

        self.status_description = ko.computed(function() {
            var status = self.fields.status(),
                liverail_status = self.fields.liverail_status();

            if (status === 'blocked') {
                return 'on hold because of lack of funds';
            } else if (status === 'audited') {
                return 'positive';
            } else if (liverail_status === 'error') {
                return 'transcoding error occured'
            } else {
                return status;
            }
        });

        /**
         * Sends creative to review.
         */
        self.send_to_audit = function() {
            var url = Urls.creative_manual_audit(self.fields.id());
            return $.getJSON(url).done(function(creative_data) {
                self.set(creative_data);
            });
        };


        /**
         * Loads creative with data from backend, based on its id
         */
        self.load = function(id) {
            var url = Urls.api_dispatch_detail_id('storage/creative', id);

            return $.getJSON(url).done(function(creative_data) {
                self.set(creative_data);
            });
        };


        /**
            Saves/updates object in backend. POST for new creative,
            PUT for existing
         */
        self.save = function(view_after_success) {
            if (_.isUndefined(view_after_success)) {
                view_after_success = true;
            }
            var url = Urls.api_dispatch_list('storage/creative'),
                successMsg = 'New creative was saved!',
                method = 'POST',
                success = function(data) { 
                    creative = new Creative(data);
                    creatives.unshift(creative);
                    if (view_after_success) {
                        creative.goToView();
                    }
                    return creative;
                };
            if (self.fields.id()) {
                url = Urls.api_dispatch_detail_id('storage/creative',
                            self.fields.id());
                method = 'PUT';
                successMsg = 'Creative was updated!';
                success = function(data) {
                    var creative = _.find(creatives(),
                        function(creative) {
                            return creative.fields.id() === data.id;
                    });
                    return creative.set(data);
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
                    var creative = success(response);
                    notifications.show(successMsg, 2);
                    deferred.resolve(creative);
                },
                error: function(jqXHR, status, error) {
                    var response = JSON.parse(jqXHR.responseText);
                    var messages = 'There has been an error!';
                    if (response.error) {
                        messages = response.error;
                    } else if (response.creative) {
                        messages = _.map(response.creative,
                            function(message, key) {
                                return key + ': ' + message;
                            });
                    }

                    notifications.showModal('Error!', messages);
                    deferred.reject();
                }
            });
            return deferred.promise();
        };

        /**
            Sends delete request for current Creative object

            After that removes itself from creatives list
            and redirects to main storage page
         */
        self.remove = function() {
            var url = Urls.api_dispatch_detail_id('storage/creative',
                                            self.fields.id());

            $.ajax({
                url: url,
                type: 'DELETE',
                dataType: 'json',
                contentType: 'application/json',
                success: function(response) {
                    success(response);
                },
                statusCode: {
                    204: function() {
                        creatives.remove(function(creative) {
                            return creative.fields.id() === self.fields.id();
                        });
                        router.routeTo(router.path.storage());
                        notifications.show('Creative was removed.', 2);
                    }
                }
            });
        };


        /**
            Switches to current object's view page.
            Copies itself into storage.creative,
            and then goes to edit/view page
         */
        self.goToView = function() {
            // needs presenter refactor to get rid of
            router.routeTo(router.path.storage_creative({
                id: self.fields.id().toString()
            }));
        };

        self.setImageFromqqUploader = function(responseJSON, fileName) {
            if (!self.verifyImageSize(responseJSON.width, responseJSON.height)) {
                return;
            }
            
            self.fields.api_data(responseJSON.path);
            self.fields.width(responseJSON.width);
            self.fields.height(responseJSON.height);
            if (!self.fields.name()) {
                self.fields.name(fileName);
            }

            // only allow to be fluent, if the object is not created!
            if (responseJSON.type && !self.fields.id()) {
                self.fields.type(responseJSON.type);
            } else if (responseJSON.type &&
                       responseJSON.type !== self.fields.type()) {
                notifications.showModal(
                    'Error!', 'Incorrect file for this creative type!');
            }
        };
        
        /**
           Image for facebook sidebar creative must be larger than 254x133 with an aspect ratio of 1.91:1
           For facebook newsfeed image can be rectangular (minimum 560x292 with an aspect ratio of 1.91:1)
           or square (minimum 90x90)
        */
        self.verifyImageSize = function(width, height) {
            if (self.fields.destination()=='facebook_sidebar') {
                if ((width!=0 && height!=0)&&(width<254 || height<133 || 
                    (width/height).toFixed(2)<1.90 || (width/height).toFixed(2)>1.92)) {
                    notifications.showModal('Error!', 'Image for facebook sidebar creative must be larger than 254x133 with an aspect ratio of 1.91:1. The recommended size is 600x315');
                    return false;
                }
                return true;
            }
            if (self.fields.destination()=='facebook_newsfeed') {
                if ((width == height)&&(width>=90))
                    return true;
                if ((width!=0 && height!=0)&&(width<560 || height<292 || 
                    (width/height).toFixed(2)<1.90 || (width/height).toFixed(2)>1.92)) {
                    notifications.showModal('Error!', ' Rectangular image for facebook news feed must be larger than 560x292 with an aspect ratio of 1.91:1. The recommended size is 600x315. Square image must be larger than 90x90. The recommended size is 200x200');   
                    return false;
                }
                return true;
            }
            /* for default creatives */
            return true;
        };
        
        self.destinationChange = function(){
           if (!self.verifyImageSize(self.fields.width(), self.fields.height()) && self.isCreativeTypeFB()) {
                 self.fields.api_data('');
                 self.fields.width(0);
                 self.fields.height(0); 
           }
        };
    };

    return {
        Creative: Creative,
        creatives: creatives,
        get: get
    };
});
