define(['notifications', 'localStoragePolyfill'], function(notifications) {

    AVAILABLE_APPS = ['trim', 'addnow', 'delieverme', 'reachme',
                      'unifyanalytics', 'unifyenterprise'];

    var appStates = {};

    _.each(AVAILABLE_APPS, function(application){
        appStates[application] = ko.observable(false);
    });

    function toggleEnabled(application){
        var isEnabledObservable = appStates[application];
        var newState = !isEnabledObservable();
        isEnabledObservable(newState);
        localStorage.setItem(application, newState);
        // console.log('Switched 2' + newState);
    }

    function connect(application){
        appStates[application](true);
        localStorage.setItem(application, true);
        // console.log('Switched ' + true);
    }

    function refresh(){
        /** Read integration states from local storage */
         _.each(AVAILABLE_APPS, function(application){
            var isEnabled = localStorage.getItem(application) === "true";
            appStates[application] = ko.observable(isEnabled);

        });
    }

    function modal() {
        notifications.customDialog('Connect Tr.im', this, 'trimModal');
    }

    refresh();

    return {
        appStates: appStates,
        toggleEnabled: toggleEnabled,
        refresh: refresh,
        modal: modal,
        connect: connect
    };
});
