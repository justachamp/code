define(
    ['text!./view.html', 'logger', 'account'],
    function(template, logger, account) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = account.BillingInfo;

        self.activate = function(params) {
            return self.vm.load();
        };
    };

    return Component;

});
