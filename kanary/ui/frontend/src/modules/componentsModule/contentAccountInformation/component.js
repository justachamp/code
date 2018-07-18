define(
    ['text!./view.html', 'logger', 'account'],
    function(template, logger, account) {

    var Component = function(moduleContext) {
        var self = this;

        self.template = template;
        self.panel = null;
        self.vm = account.user;

        self.activate = function() {
            return account.getLoggedUser().done(function() {
                self.vm.load();
            });
        };
    };

    return Component;

});
