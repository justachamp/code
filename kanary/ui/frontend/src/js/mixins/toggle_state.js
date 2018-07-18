define(['notifications'], function(notifications) {

    /*
     * This mixin handles common behavior of changing active state between
     * strategy models (in campaign overview and in startegy overview)
     */
    function ToggleStateMixin() {
        var self = this;

        self.toggleText = ko.computed(function() {
            var get_state = self.paused || self.fields().paused;
            return !get_state() ? 'Deactivate Strategy' : 'Activate Strategy';
        });

        self.activeToggle = function(strategy, event) {
            event.stopPropagation();

            var get_id = self.id || self.fields().id,
                url = Urls.strategy_toggle_active(get_id());

            return $.post(url).done(function(response) {
                strategy.paused(response.is_paused);
                if (response.is_paused) {
                    notifications.show('Strategy deactivated', 2);
                } else {
                    notifications.show('Strategy activated', 2);
                }
            });
        };
    };

    return ToggleStateMixin;
});
