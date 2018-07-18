define(['logger'], function(logger) {

    var currentComponent = null;

    function init() {

        $(document).delegate('[data-toggle=collapse-tree]', 'click',
            function() {
                $(this).parent()
                       .toggleClass('icon-folder-open icon-folder-close');

                return false;
            });

        logger.info('customControls started');
    }

    return {
        init: init
    };
});
