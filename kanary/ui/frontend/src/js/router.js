define(
['logger', 'mediator', 'js/routes'],
function(logger, mediator, routes) {
    var router = crossroads.create();
    router.normalizeFn = crossroads.NORM_AS_OBJECT;
    var apiRouter = crossroads.create();

    var path = {};
    var routeToObject = {};

    var _replaceHash = false;

    router.routed.add(function(request, data) {
        Raven.updateUser({path: request});
    });

    var routeTo = function(path, callback, noHashSave) {

        if (path === 'back') {
            window.history.back();
            return false;
        }

        if (! _replaceHash) {
             _replaceHash = noHashSave;
            hasher.setHash(path);
        } else {
            _replaceHash = false;
            hasher.replaceHash(path);
        }

        if (_.isFunction(callback)) {
            callback();
        }
    };

    // Hash change without event handling
    var updateTo = function(path, noHashSave) {
        hasher.changed.active = false;
        if (noHashSave) {
            hasher.replaceHash(path);
        } else {
            hasher.setHash(path);
        }
        hasher.changed.active = true;
    };

    // history
    var history = [];

    var isGoingBack = function(request) {
        var prev = history[history.length - 2];
        return prev === request;
    };


    // sidebar transition
    var sidebarTransition = 'slideIn';

    var setSidebarTransition = function(new_request) {

        var old_request = history[history.length - 1];

        if (!old_request)
            return 'slideIn';

        // menu change
        if (old_request.split('/')[0] !== new_request.split('/')[0])
            return 'slideIn';

        // are we going back in history?
        if (isGoingBack(new_request))
            return 'slideFromLeft';

        return 'slideFromRight';
    };

    function processHashChange(request, data) {
    }

    function parseHash(newHash, oldHash) {
        router.parse(newHash);

        if (_replaceHash) {
            return;
        }

        sidebarTransition = setSidebarTransition(newHash);

        // save history
        var prev = history[history.length - 1];
        if (isGoingBack(newHash)) {
            history.pop();
        } else {
            history.push(newHash);
        }
    }


    function broadcastUrlChange(params) {

        var message = $.extend(params, {
            sidebarTransition: params
                .sidebarTransition || sidebarTransition || 'slideIn'
        });

        mediator.notify('URL_CHANGE', message);
    }


    var init = function() {

        var self = this;

        var routeToObject = function(name, id) {
            var url = Urls.api_dispatch_detail_id(name, id);

            $.getJSON(url).done(function(resp) {
                self.routeTo(self.path[name + '_api'](resp), true);
            });
        };

        hasher.initialized.add(parseHash);
        hasher.changed.add(parseHash);

        if (! hasher.isActive())
            hasher.init();

        // routes object
        this.routes = {};

        // automapping api urls
        this.path = {};

        // Route callbacks
        var route_callbacks = {
            broadcastUrlChange: function(params, vals) {
                _.extend(params, vals);
                broadcastUrlChange(params);
            },
            routeToObject: function(object_name, vals) {
                routeToObject(object_name, vals.id);
            }
        };

        /*
            Loop creates two objects from a route definition list
            (routes argument):
            1. adds route do router, and to routes object
            2. creates callback for each route, that generates it's api path
         */
        $.each(routes, function(i, route) {
            var route_name = route[0],
                route_pattern = route[1],
                additional_params = route[2];
            // default callback is broadcastUrlChange
            var callback = 'broadcastUrlChange';
            if (route.length == 4) {
                callback = route[3];
            }
            // creating route object
            self.routes[route_name] = router.addRoute(route_pattern,
                function(vals) {
                    route_callbacks[callback](additional_params, vals);
                });
            // creating method that will automap api url
            self.path[route_name] = function(dict) {
                _.each(dict, function(value, name) {
                    dict[name] = String(value);
                });
                return '#' + self.routes[route_name].interpolate(dict);
            };
        });

    }; // end init

    return {
        init: init,
        path: path,
        history: history,
        routeTo: routeTo,
        routeToObject: routeToObject,
        updateTo: updateTo
    };
});
