define(['underscore'], function(_) {
    'use strict';
    /*******
    Identifies a collection of components inside interface.
    Tries to create consisitient interface between this kind of objects,
    with update/init methods
    *****/


    /*
     * Defines base object for rest of the component-like objects.
     * It saves information about parent object/component for easier
     * implementation  of cross component code.
     * e.g. Click on row table must call widget in different element.
     * However it's more like a concept than real design implementation.
     */
    var Component = function(parent) {
        var self = {};

        // Stores a reference to the parent object
        self.parent = parent;

        /*
         * Initiliazes state of component
         */
        self.init = $.noop;

        /*
         * Updates state of component
         */
        self.update = $.noop;

        return self;
    };

    /**
     * Stores a list of components and provides methods to massive updates
     * of their state.
     * Main purpose of this class is to simplify translation of objects
     * from given list.
     *
     * @param {string} property_id - name of property_id which identifies
     * object in the list. It's like gethash function of object.
     * @param {object} item_constructor - constructor of an item which will be
     * added/maintained in list. Called with single argument of self.parent.
     */
    var ComponentSet = function(parent, property_id, item_constuctor) {

        var self = new Component(parent);

        // stores a list of objects
        self.elements = ko.observableArray();

        // Defines name of property which identifies elements in the list
        self.property_id = property_id;

        // Reference of constructor used when we need add new object into list
        self.item_constuctor = item_constuctor;

        /*
         * Insert or update a list of objects
         *
         * @param {array} list of object with- fields which are used for update
         * or initialization of object from item_constructor
         */
        self.update = function(objects) {
            self.clear();
            _.each(objects, function(item) {
                if (self.hasItem(item)) {
                    self.updateItem(item);
                } else {
                    self.addItem(item);
                }
            });
        };

        /*
         * Checks if given element exists in the set of components
         * @param {object} item - a object with fields which will be updated
         */
        self.hasItem = function(item) {
            var current_ids = _.pluck(self.elements(), self.property_id);
            return _.contains(current_ids, item[self.property_id]);
        };

        /*
         * Adds new element into set and initializes ith with data given
         * in parameters
         * @param {object} data - object/structure with data to initializaze
         * ui control.
         */
        self.addItem = function(data) {
            // Pass ComponentSet's parent as element's as parent.
            var item = new self.item_constuctor(self.parent);
            item.init(data);
            self.elements.push(item);
        };

        /*
         * Updates state of existing element in the set.
         * @param {object} data - data which are passed to ui widget.
         */
        self.updateItem = function(data) {
            var items = _.where(self.elements(), {id: data[self.property_id]}),
                item;

            // elements not found, exit for better performance
            if (!items.length) {
                return;
            }
            // Extracts first elements as _.where returns an array
            item = items[0];
            item.update(data);
        };

        /*
         * Makes updates of a list of objects from a list of dastructures
         * @param {array} items - a array of items which are passed to ui
         * components.
         */
        self.updateItems = function(items) {
            _.map(items, function(item) {
                self.updateItem(item);
            });
        };

        /*
         * Removes all components from the set.
         */
        self.clear = function() {
            self.elements([]);
        };

        return self;
    };

    return {
        Component: Component,
        ComponentSet: ComponentSet
    };

});
