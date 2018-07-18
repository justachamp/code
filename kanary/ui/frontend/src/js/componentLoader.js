define(['logger'], function(logger) {

    var components = null;

    function init() {
        if (!components) {
            components = {};
        }
        logger.info('componentLoader started');
    }

    function getComponent(componentName) {
        console.log('loading component', componentName);
        var deferred = $.Deferred();

        if (components.hasOwnProperty(componentName)) {
            deferred.resolve(components[componentName]);
        } else {

            var fullPath =
                'modules/componentsModule/' + componentName + '/component';

            require([fullPath], function(Component) {
                var component = new Component();
                components[componentName] = component;
                deferred.resolve(component);
            });
        }

        return deferred.promise();
    }

    function removeComponent(componentName) {
        console.log('removing component', componentName);
        delete components[componentName];
    }

    return {
        init: init,
        getComponent: getComponent,
        removeComponent: removeComponent
    };
});
