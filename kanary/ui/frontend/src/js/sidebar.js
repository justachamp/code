define(['logger', 'presenter', 'account'],
    function(logger, presenter, account) {

        function init() {
            var panel = new presenter.PanelPresenter('sidebar');
            panel.register();
        }

        return {
            init: init
        };
});
