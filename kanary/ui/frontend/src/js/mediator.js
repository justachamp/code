define(
    ['logger'],
    function(logger) {

        var pubsub = null;

        function init() {
            if (!pubsub) pubsub = new PubSub();
            logger.info('mediator started');
        }

        function notify(event, params) {
            pubsub.publish(event, params);
        }

        function listen(event, fn) {
            pubsub.subscribe(event, fn);
        }

        return {
            init: init,
            notify: notify,
            listen: listen
        };
});
