
define(['notifications'],
function(notifications) {
    function create(setId, inventory) {
        /**
            @param {observable} setId : Publisher set ID
            @param {observable} inventory : Inventory type ('app' or 'site')
            @return {Deferred} Deferred object which is resolved with
                PublisherSet when module is ready
        */
        if (_.isUndefined(setId)) {
            throw 'Publisher set ID is required';
        }
        if (_.isUndefined(inventory)) {
            throw 'Inventory type is required';
        }
        var publisherSet = new PublisherSet(setId, inventory);

        function getSavedSet() {
            return publisherSet.selectedPublishers.get(setId());
        }

        function getSearchResults() {
            publisherSet.searchResults.get();
            deferred.resolve(publisherSet);
        }

        var deferred = $.Deferred();
        if (setId()) {
            /*
                Load saved set before search results to avoid
                re-loading search results if set has 'network' type
            */
            getSavedSet().done(getSearchResults);
        } else {
            getSearchResults();
        }
        return deferred.promise();
    }

    function PublisherSet(setId, inventory) {
        /**
            @param {observable} setId : Publisher set ID
            @param {observable} inventory : Inventory type ('app' or 'site')
        */
        var self = this;
        self.publisherFactory = new PublisherFactory();
        self.type = new PublisherType(inventory);
        self.blacklist = ko.observable(false);
        self.setId = setId;
        self.inventory = inventory;
        self.selectedPublishers = new SelectedPublishers(
            self.type,
            self.publisherFactory,
            self.setId,
            self.blacklist
        );
        self.searchResults = new SearchResults(self.type,
            self.publisherFactory);
    }

    function PublisherFactory() {
        /* Single place to create PublisherRow objects
           Eliminates the problem having separate instances
           of publisher in different tabs, because
           publishers in both tabs are the same objects
        */
        var self = this;
        self.cache = {};
        self.pubsub = PubSub();
        pubsub = self.pubsub;
        function Publisher(attributes) {
            var self = this;
            self.init = function() {
                for (key in attributes) {
                    self[key] = ko.observable(attributes[key]);
                }
                if (attributes.selected == undefined) {
                    self.selected = ko.observable(false);
                }
                self.expanded = ko.observable(false);
            };
            self.init(attributes);
            self.update = function(attributes) {
                for (key in attributes) {
                    if (_.isFunction(self[key])) {
                       self[key](attributes[key]);
                    }
                }
            };
            self.toggleSelected = function() {
                var newValue = ! self.selected();
                self.selected(newValue);
                var channel = (newValue) ? 'selected' : 'deselected';
                pubsub.publish(channel, self);
            };
            self.toggleExpanded = function() {
                var newValue = ! self.expanded();
                self.expanded(newValue);
            };
        };
        self.getOrCreate = function(attributes) {
            var id = attributes.id;
            if (! (id in self.cache)) {
                self.cache[id] = new Publisher(attributes);
            } else {
                self.cache[id].update(attributes);
            }
            return self.cache[id];
        };
    };

    var PublisherType = function(inventory) {
        var self = this;
        self.inventory = inventory;
        self.is_network = ko.observable(false);

        self.model = ko.computed(function() {
            var model;
            if (this.is_network()) {
                model = 'network';
            } else {
                model = this.inventory();
            }
            return model;
        }, self);

        /*  Different types of publishers (site, app, network)
            have a different representation in the UI,
            thus there are separate templates for each
            publisher type
        */
        self.templates = {
            app: {
                header: 'mobileHeader',
                row: 'publisherRow',
                name: 'App',
                filters: ['publisher_id', 'network_id', 'name', 'network']
            },
            site: {
                header: 'webHeader',
                row: 'publisherRow',
                name: 'Domain',
                filters: ['publisher_id', 'network_id', 'name', 'network']
            },
            network: {
                header: 'networkHeader',
                row: 'networkRow',
                name: 'Name',
                filters: ['network_id', 'network']
            }
        };

        self.template = ko.computed(function() {
            return self.templates[self.model()] || self.templates.app;
        });

        self.init = function(attributes) {
            self.inventory(attributes.inventory);
            self.is_network(attributes.is_network);
        };
    };

    var PublisherList = function(type, publisherFactory) {
        /* Base class for SearchResult and SelectedPublishers */
        var self = this;

        self.type = type;
        self.publisherFactory = publisherFactory;

        self.fields = {
            items: ko.observableArray()
        };

        self.isEmpty = function() {
            return (self.fields.items().length == 0);
        };

        self.fillItems = function(publishers, classDefaults) {
            var defaults = classDefaults || {};

            self.fields.items.removeAll();
            for (var i = 0; i < publishers.length; i++) {
                var fieldValues = _.extend(defaults, publishers[i]);
                self.fields.items.push(
                    self.publisherFactory.getOrCreate(fieldValues)
                );
            }
        };
    };

    var SearchResults = function(type, publisherFactory) {
        /* Representation of Search Results list */
        var self = this;
        PublisherList.apply(self, [type, publisherFactory]);

        self.MIN_TEXT_SEARCH_LENGTH = 3;

        self.availableFilters = [
            {
                label: 'Publisher ID',
                value: 'publisher_id',
                minLength: 0
            },
            {
                label: 'Network ID',
                value: 'network_id',
                minLength: 0
            },
            {
                label: 'Network name',
                value: 'network',
                minLength: self.MIN_TEXT_SEARCH_LENGTH
            }
        ];

        self.nameFilter = function() {
            return {
                label: self.type.template().name,
                value: 'name',
                minLength: self.MIN_TEXT_SEARCH_LENGTH
            };
        };

        self.acceptedFilters = function() {
            var acceptedNames = self.type.template().filters;
            function isAccepted(name) {
                return (_.indexOf(acceptedNames, name) != -1);
            }
            var accepted = [];

            if (isAccepted('name')) {
                accepted.push(self.nameFilter());
            }
            accepted = accepted.concat(
                _.filter(self.availableFilters, function(filter) {
                    return isAccepted(filter.value);
                })
            );

            return accepted;
        };

        self.filters = ko.computed(self.acceptedFilters, self);

        self.selectedFilter = ko.observable({minLength: 0});

        self.search = ko.observable();

        self.trimmedSearch = ko.computed(function() {
            /**
            *   Replaces with empty string if value is shorter min search length
            */
            var value = this.search() || '',
                threshold = this.selectedFilter().minLength || 0;
            return (value.length < threshold) ? '' : value;
        }, self);

        self.meta = ko.observable({
            page: 1,
            total_count: 0,
            limit: 20
        });

        self.page = ko.computed(function() {
            return this.meta().page;
        }, self);

        self.baseUrl = ko.computed(function() {
            var inventory = this.type.inventory();
            var is_network = this.type.is_network();
            var page = this.page();

            var url = (is_network) ?
                       Urls.api_dispatch_list('targeting/network') :
                       Urls.api_dispatch_list('targeting/publisher');
            url += '?inventory=' + inventory +
                       '&page=' + page +
                       '&limit=' + self.meta().limit;
            return url;
        }, self);

        self.searchUrl = ko.computed(function() {
            var filter = this.selectedFilter();
            var search = this.trimmedSearch();
            return (filter && search) ?
                    filter.value + '=' + encodeURI(search) :
                    '';
        }, self).extend({throttle: 500});

        self.get = function() {
            var url = self.baseUrl();
            if (self.searchUrl() != '') {
                url += '&' + self.searchUrl();
            }
            return $.ajax({
                url: url,
                method: 'GET',
                success: function(response) {
                    self.meta(response.meta);
                    self.fillItems(response.objects);
                }
            });
        };

        self.refresh = function() {
            self.resetPagination();
            self.get();
        };

        self.addListeners = function() {
            function handler() {
                self.refresh();
            };
            self.type.is_network.subscribe(handler);
            self.type.inventory.subscribe(handler);
            self.searchUrl.subscribe(handler);
        };

        self.addListeners();

        self.unselectAll = function() {
            var items = self.fields.items();

            for (var i = 0; i < items.length; i++) {
                if (items[i].selected()) {
                    items[i].toggleSelected();
                }
            }
        };

        self.selectAll = function() {
            var items = self.fields.items();

            for (var i = 0; i < items.length; i++) {
                if (! items[i].selected()) {
                    items[i].toggleSelected();
                }
            }
        };

        self.clear = function() {
            self.fields.items.removeAll();
        };

        self.resetPagination = function() {
            var newMeta = _.extend(self.meta(), {page: 1, total_count: 0});
            self.meta(newMeta);
        };

        self.maxPagerLenght = ko.observable(9);

        self.pageCount = ko.computed(function() {
            var meta = this.meta();
            return Math.floor(meta.total_count / meta.limit);
        }, self);

        self.pagerStart = ko.computed(function() {
            var maxLength = this.maxPagerLenght();
            var pageCount = this.pageCount();
            var page = this.page();
            var closestPageCount = (maxLength - 1) / 2;
            if ((pageCount <= maxLength) || (page <= closestPageCount)) {
                return 1;
            }

            var pagesLeft = pageCount - page;
            if (pagesLeft < closestPageCount) {
                return Math.max(1, pageCount - (maxLength - 1));
            } else {
                return page - closestPageCount;
            }
        } , self);

        self.pagerCount = ko.computed(function() {
            return Math.min(
                    this.maxPagerLenght(),
                    this.pageCount(),
                    this.pageCount() - (this.pagerStart() - 1)
                );
        }, self);

        self.changePage = function(page) {
            page = Math.max(1, page);
            var newMeta = self.meta();
            newMeta.page = page;
            self.meta(newMeta);
            self.get();
        };
        self.prevPage = function() {
            self.changePage(
               self.page() - 1
            );
        };
        self.nextPage = function() {
            self.changePage(
                self.page() + 1
            );
        };

        self.type.inventory.subscribe(function() {
            self.refresh();
        });
        self.type.is_network.subscribe(function() {
            self.refresh();
        });
    };

    var SelectedPublishers = function(type, publisherFactory, setId, blacklist) {

        /* Representation of Selecter Publishers list */

        var self = this;

        PublisherList.apply(self, [type, publisherFactory]);

        _.extend(self.fields, {
            id: setId,
            name: ko.observable(''),
            previousType: ko.observable(''),
            blacklist: blacklist
        });

        self.init = function(attributes) {
            self.initAttributes = attributes;
            self.fields.name(attributes.name);
            self.fields.blacklist(attributes.blacklist);
            self.fields.id(attributes.id);
            self.fillItems(attributes.targetvalues, {selected: true});
        };

        self.toJSON = function() {
            var fields = self.fields,
                type = self.type,
                object = {};
            _.extend(object, {
                name: fields.name(),
                blacklist: fields.blacklist(),
                inventory: type.inventory(),
                is_network: type.is_network(),
                targetvalues_ids: _.map(fields.items(), function(element) {
                    return element.id();
                })
            });

            if (fields.id()) {
                _.extend(object, {
                    id: fields.id()
                });
            }

            return object;
        };

        /* Changing type */

        self.togglerunOnNetwork = function() {
            self.unselectAll();
            var isRunningOnNetwork = ! self.type.is_network();
            self.type.is_network(isRunningOnNetwork);
        };

        /* Filling with data*/

        self.receiveFromTray = function(set) {
            self.get(set.id);
            self.focus();
        };

        self.oldFillItems = self.fillItems;
        self.fillItems = function(attributes, subClassDefaults) {
            self.unselectAll();
            self.oldFillItems(attributes, subClassDefaults);
        };


        /* Subscribing to publisher selection */

        self.add = function(item) {
            self.fields.items.push(item);
        };

        self.remove = function(deselectedItem) {
            self.fields.items.remove(
                    function(item) {
                        return deselectedItem.id() == item.id();
                }
            );
        };

        self.publisherFactory.pubsub.subscribe('selected', self.add);
        self.publisherFactory.pubsub.subscribe('deselected', self.remove);


        /* Clearing */

        self.unselectAll = function() {
            var items = self.fields.items();

            while (items.length > 0) {
                var first = items[0];
                if (first.selected()) {
                    first.toggleSelected();
                }
            }
        };

        self.reset = function(inventory) {
            self.unselectAll();
            self.init({
                id: null,
                name: '',
                targetvalues: []
            });
        };

        /* Handling type change */
        self.type.inventory.subscribe(self.reset);
        self.type.is_network.subscribe(self.reset);

        /* Dirty state */

        self.isSaved = function() {
            return (self.fields.id());
        };
        self.isChanged = function(field) {
            var empty = {
                name: self.fields.name(),
                id: self.fields.id(),
                targetvalues: self.fields.items(),
                inventory: self.type.inventory()
            };
            var initAttributes = self.initAttributes || empty;
            var fields = self.fields;
            var type = self.type;
            var functions = {
                'items': function() {
                    var oldPublishers = _.pluck(
                        initAttributes.targetvalues, 'id');
                    var newPublishers = _.map(
                        fields.items(), function(element) {
                            return element.id();
                    });

                    var removed = _.difference(oldPublishers, newPublishers);
                    var added = _.difference(newPublishers, oldPublishers);

                    added = added.length;
                    removed = removed.length;

                    return (removed > 0 || added > 0);
                },
                'inventory': function() {
                    return initAttributes.inventory != type.inventory();
                }
            };

            if (! field in functions) {
                throw 'Invalid field name: ' + field;
            }
            return functions[field]();
        };

        self.hasUnsavedChanges = ko.computed(function() {
            var a = self.fields.items();
            var b = self.type.inventory();
            if (self.isChanged('items') || self.isChanged('inventory')) {
                return true;
            }

            return false;
        }, self);

        self.saveBtnEnabled = ko.computed(function() {
            return self.hasUnsavedChanges() && !self.isEmpty();
        });

        self.saveAsBtnEnabled = ko.computed(function() {
            return self.hasUnsavedChanges() && !self.isSaved();
        });

        /* Saving */

        self.saveVm = {
            defaults: {
                name: '',
                name_validation: '',
                isEditingDisabled: null
            },
            fields: {
                name: ko.observable(),
                name_validation: ko.observable(),
                isEditingDisabled: ko.observable()
            },
            save: function() {
                var thisVm = self.saveVm;
                if (thisVm.isValid()) {
                    var newName = thisVm.fields.name();
                    var dfd = self.save(newName);
                    dfd.done(thisVm.done);
                }
            },
            done: function(text) {
                notifications.closeModal();
                notifications.show(text);
            },
            isValid: function() {
                return true;
            }
        };

        self.saveVm.reset = function(attributes) {
            var thisVm = self.saveVm;
            attributes = _.extend(thisVm.defaults, attributes);
            for (field in thisVm.fields) {
                thisVm.fields[field](attributes[field]);
            }
        };

        self.saveDialog = function(title, isEditingDisabled) {
            if (self.isEmpty()) {
                notifications.showModal(
                    'Error!',
                    'You cannot save empty Publisher set.'
                );
                return;
            }
            self.saveVm.reset({
                name: self.fields.name(),
                isEditingDisabled: isEditingDisabled || null
            });
            notifications.customDialog(
                title, self.saveVm, 'publisherSetNotification');
        };

        self.get = function(publisher_set_id) {
            return $.get(
                Urls.api_dispatch_list('publishers/sets/' + publisher_set_id)
            ).done(function(response) {
                self.type.is_network(response.is_network);
                self.init(response);
            });
        };

        self.save = function(newName) {
            var deferred = $.Deferred();
            var url, text, method;
            var data = self.toJSON();
            data.name = newName;
            if (self.isSaved()) {
                var set_id = self.fields.id();
                method = 'PUT',
                text = 'Set updated';
                url = Urls.api_dispatch_detail_id('publishers/sets', set_id);
            } else {
                method = 'POST',
                url = Urls.api_dispatch_list('publishers/sets'),
                text = 'Set created succesfully';
            }

            var deferred = $.Deferred();
            $.ajax({
                    url: url,
                    type: method,
                    data: JSON.stringify(data),
                    contentType: 'application/json'
            }).done(function(publisherSet) {
                self.init(publisherSet);
                deferred.resolve(text);
            }).fail(function(jqXHR) {
                // Getting backend errors
                var error = JSON.parse(jqXHR.responseText);
                if (error.sets.name) {
                    self.saveVm.fields.name_validation(error.sets.name);
                }
                deferred.resolve('An error occured while saving set.');
            });
            return deferred.promise();
        };

        /* Ui helper */

        self.focus = function() {
            $('.-t-selected-publishers').click();
        };

    };

    return {
        create: create
    };

});
