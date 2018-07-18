define(
    ['logger', 'componentLoader', 'mediator', 'Boiler'],
    function(logger, componentLoader, mediator, Boiler) {

    var transition = {
        sidebar: {
            ease: '',
            width: 400,
            slideIn: 300
        },
        content: {
            fadeIn: 200,
            fadeOut: 300
        }
    };

    function init() {
        logger.info('presenter initialized');
    }

    function sidebarShow(sidebar) {
        sidebar.show();
        var scrollViewport = $(sidebar).find('.sidebar-viewport'),
            contentSelector = '.sidebar-content',
            scrollContent = $(scrollViewport).find(contentSelector);
        if ((scrollViewport.length == 0) || (scrollContent.length == 0)) {
            throw 'Sidebar view does\` have correct structure.' +
                ' Scrolling is disabled.';
        } else {
            $(scrollViewport).niceScroll([contentSelector, {}]);
        }
        return sidebar;
    };

    function sidebarHide(sidebar) {
        return sidebar.hide();
    };

    function addScroll(element) {
        $(element).bootstrapScroll();
    };

    function slideSidebar(oldElement, element, from, into) {
        var t = transition.sidebar;

        element.css({ marginLeft: from, 'z-index': 5 });
        return element
            .animate({ marginLeft: into }, t.slideIn, t.ease, function() {
                $('section.sidebar').css('z-index', 1);
                element.css('z-index', 2);
                sidebarShow(element);
                if (oldElement) {
                    oldElement.remove();
                }
            }).promise();
    }

    function slideIn(oldComponent, newComponent) {

        var newElement = newComponent.panel.getJQueryElement(),
            width = '-' + transition.sidebar.width + 'px';

        if (oldComponent) {
            var oldElement = oldComponent.panel.getJQueryElement();
        }

        return slideSidebar(oldElement, newElement, width, 0);
    }

    function slideComponent(oldComponent, newComponent, left) {

        var newElement = newComponent.panel.getJQueryElement();

        if (oldComponent) {
            var oldElement = oldComponent.panel.getJQueryElement();
        }

        var t = transition.sidebar;

        if (left) {
            var width = {
                minus: '+=' + t.width + 'px',
                plus: '-' + t.width + 'px'
            };
        } else {
            var width = {
                minus: '-=' + t.width + 'px',
                plus: '+' + t.width + 'px'
            };
        }

        if (oldElement) {
            oldElement.animate({ marginLeft: width.minus },
                t.slideIn, t.ease, function(el) {
                    sidebarShow(newElement);
            });
        }
        return slideSidebar(oldElement, newElement, width.plus, width.minus);
    }

    function slideFromRight(oldComponent, newComponent) {
        return slideComponent(oldComponent, newComponent, true);
    }

    function slideFromLeft(oldComponent, newComponent) {
        return slideComponent(oldComponent, newComponent, false);
    }

    function fadeInContent(oldComponent, newComponent, panelName) {

        var newElement = newComponent.panel.getJQueryElement().hide(),
            panelName = panelName || 'content';
        var contentBox = $('section#' + panelName);

        function fadeIn(fadeTime) {
            if (newComponent.panel) {
                newComponent.panel.appendTo(contentBox);
            }
            return newElement.fadeIn(fadeTime, addScroll(contentBox)).promise();
        }

        if (! oldComponent) {
            return fadeIn(transition.content.fadeIn * 2);
        }
        var oldElement = oldComponent.panel.getJQueryElement();

        var faded = oldElement.fadeOut(transition.content.fadeOut)
            .promise().done(
            function() {
                oldComponent.panel = null;
                oldElement.remove();
                return fadeIn(transition.content.fadeIn);
            });

        if (_.isFunction(oldComponent.deactivate)) {
            oldComponent.deactivate();
        }
        return faded;
    }

    function PanelPresenter(panel_name) {
        var self = this,
            transitions = {
                slideIn: slideIn,
                slideFromLeft: slideFromLeft,
                slideFromRight: slideFromRight,
                _default: fadeInContent
            };
        self.panel_name = panel_name;
        self.currentComponent = null;
        self.currentComponentName = null;

        self.on_url_change = function(params) {
            var transitionName = params[self.panel_name + 'Transition'],
                transitionFunc = transitions[transitionName || '_default'];
                window[self.panel_name + '_is_loading'] = true;

            componentLoader.getComponent(
                params[self.panel_name]
            ).done(function(component) {

                // We use two deferreds because we want to wait for all
                // requests/actions.
                // component.active / component.onUrlChange have to return
                // $.Deferred().promise()
                var activate_deferred = $.Deferred(),
                    url_change_deferred = $.Deferred();

                // this piece is called once, per component change
                if (component.panel) {
                    // so, resolve it immediately
                    activate_deferred.resolve();
                } else {
                    // call activate - called once, and retrieve elements
                    // to bind
                    if (_.isFunction(component.activate)) {
                        activate_deferred = component.activate(params);
                    } else {
                        // so, resolve it immediately
                        activate_deferred.resolve();
                    }
                }

                // if component defines it, called after *each* url change
                activate_deferred.done(function() {
                    if (_.isFunction(component.onUrlChange)) {
                        url_change_deferred = component.onUrlChange(params);
                    } else {
                        url_change_deferred.resolve();
                    }

                    // These deferreds return nothing, viewmodel is in
                    // Component.vm
                    $.when(url_change_deferred).done(function() {
                        self.component_loaded(
                            component, transitionFunc, params[self.panel_name]
                        );
                    });
                });
            });
        };
        self.component_loaded = function(
            component, transitionFunc, componentName) {

            if (!component.panel) {
                // set panel on component
                var parent = $('section#' + self.panel_name);
                component.panel = new Boiler.ViewTemplate(parent,
                                                          component.template);

                // binds elements to panel
                // ONLY ONCE PER COMPONENT (important)
                if (component.vm) {
                    ko.applyBindings(
                        component.vm, component.panel.getDomElement()
                    );
                }
            }
            // animate
            var animated = $.Deferred();
            if (component == self.currentComponent) {
                animated.resolve();
            } else {
                var animated = transitionFunc(
                    self.currentComponent,
                    component,
                    self.panel_name
                );
            }
            var active_class = self.panel_name + '-active';
            if (self.currentComponent && self.currentComponent.panel) {
                self.currentComponent.panel.getJQueryElement()
                                    .removeClass(active_class);
            }

            var oldComponent = self.currentComponent,
                oldComponentName = self.currnetComponentName;
            self.currentComponent = component;
            self.currnetComponentName = componentName;
            self.currentComponent.panel.getJQueryElement()
                                .addClass(active_class);

            animated.done(function() {
                if (_.isFunction(component.animated)) {
                    component.animated();
                }
                window[self.panel_name + '_is_loading'] = false;
            });

            // remove old component if the current component name is different
            if (oldComponentName && componentName != oldComponentName) {
                componentLoader.removeComponent(oldComponentName);
                delete oldComponent;
            }


        };
        /*
         * Registers function - module is loaded after url change
         */
        self.register = function() {
            // registers object as url_change_listener
            mediator.listen('URL_CHANGE', self.on_url_change);
        };
    }
    return {
        init: init,
        slideIn: slideIn,
        slideFromLeft: slideFromLeft,
        slideFromRight: slideFromRight,
        fadeInContent: fadeInContent,
        PanelPresenter: PanelPresenter
    };
});
