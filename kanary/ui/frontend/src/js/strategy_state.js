define([], function() {

    function StrategyState(state) {
        var self = this;

        self.hasBudget = ko.observable(state.has_budget());
        self.creativesPending = ko.observable(state.creatives_pending());
        self.creativesRejected = ko.observable(state.creatives_rejected());
        self.creativesExpired = ko.observable(state.creatives_expired());
        self.creativesBrandRejected = ko.observable(state.creatives_brand_page_rejected());

        self.budgetText = ko.observable('Strategy out of budget');
        self.pendingText = ko.observable('At least one creative in review');
        self.rejectedText = ko.observable('At least one creative rejected');
        self.expiredText = ko.observable('At least one creative has expired');
        self.brandText = ko.observable('At least one creative has rejected facebook page');

        self.outOfBudget = ko.computed(function() {
            return ! self.hasBudget();
        });

    }

    return StrategyState;
});
