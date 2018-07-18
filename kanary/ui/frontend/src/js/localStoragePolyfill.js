define([''], function() {

    /*
     * Mock localStorage if not supported by browser.
     */
    if (!window.localStorage) {
        window.localStorage = {
            getItem: $.noop,
            setItem: $.noop
        };
    }
    return {};
});
