define(
    ['text!./view.html', 'router'],
    function(template, router) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = { step: ko.observable('') };

        self.onUrlChange = function(params) {
            // set highlight in account sidebar
            var currentHash = '#' + hasher.getHash(),
                steps = {};

                steps[router.path.account()] = 'account';
                steps[router.path.billing()] = 'billing';
                steps[router.path.payment()] = 'billing';

            self.vm.step(steps[currentHash]);
        };
    };

    return Component;

});
