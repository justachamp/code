define(['notifications', 'account'], function(notifications, account) {

    function init() {
        var version;
        $(document).ajaxComplete(function(event, xhr, settings) {
            var header = xhr.getResponseHeader(CONFIG.AJAX_HEADER_X_VERSION);
            if (header) {
                if (version) {
                    if (header != version) {
                        // backend change is detected -> show nofification
                        notifications.showModal(
                            'Please reload this page',
                            'Kanary version update detected.'
                        );
                    }
                } else {
                    version = header;
                }
            }

            // We need update information about user. So, each ajax have this
            // information.
            var user_info_header = xhr.
                getResponseHeader(CONFIG.AJAX_HEADER_USER_INFO);

            if (user_info_header) {
                // If we have info about user, parse it into json and update
                // User object (account.loggedUser).
                var user_info = JSON.parse(user_info_header);
                account.loggedUser.setFields(user_info);
            }
        });
    }

    return {
        init: init
    };

});
