define([], function() {

    // Model containing logic for object state changes
    function CampaignState(state) {
        var self = this;

        self.finished = ko.observable(state.finished);
        self.scheduled = ko.observable(state.scheduled);
        self.inProgress = ko.observable(state.in_progress);
        self.hasBudget = ko.observable(state.has_budget);
        self.creativesAudited = ko.observable(state.creatives_audited);
        self.creativesRejected = ko.observable(state.creatives_rejected);
        self.creativesPending = ko.observable(state.creatives_pending);
        self.creativesExpired = ko.observable(state.creatives_expired);
        self.creativesBrandRejected = ko.observable(state.creatives_brand_page_rejected);

        self.strategiesWithBudget = ko.observable(
            state.strategies_with_budget
        );
        self.strategiesWithoutBudget = ko.observable(
            state.strategies_without_budget
        );

        // State tooltips
        self.budgetText = ko.observable('');
        self.scheduledText = 'Campaign scheduled';
        self.finishedText = 'Campaign finished';
        self.rejectedText = 'At least one creative rejected';
        self.pendingText = 'At least one creative is in review';
        self.expiredText = 'At least one creative has expired';
        self.brandText = ko.observable('At least one creative has rejected facebook page');

        // Budget status logic
        self.outOfBudget = ko.computed(function() {
            var campaignHasBudget = self.hasBudget(),
                strategiesHaveBudget = (self.strategiesWithoutBudget() === 0);

            if (campaignHasBudget && strategiesHaveBudget) {
                return false;
            }
            var messages = [];
            if (!campaignHasBudget) {
                messages.push('Campaign out of budget');
            }
            if (!strategiesHaveBudget) {
                messages.push('At least one strategy out of budget');
            }
            self.budgetText(messages.join(' '));
            return true;
        });
    }


    return CampaignState;

});
