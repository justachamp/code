define(['logger', 'presenter'], function(logger, presenter) {

    function init() {
        var panel = new presenter.PanelPresenter('content');
        panel.register();
    }

    return {
        init: init
    };
});
