define(['notifications', 'CampaignState'],
    function(notifications, CampaignState) {

        var category = {
            running: 'running',
            onHold: 'onHold',
            finished: 'finished'
        };

        function Campaign(campaign) {

            var self = this;

            self.id = ko.observable(campaign.id);
            self.name = ko.observable(campaign.name);
            self.slug = ko.observable(campaign.slug);
            self.status = ko.observable(campaign.status);

            self.state = new CampaignState(campaign.state);
            self.paused = ko.observable(campaign.paused);

            self.category = ko.computed(function() {
                var isFinished = self.status() === 'finished';

                if (!(self.paused() || isFinished)) {
                    return category.running;
                } else if (isFinished) {
                    return category.finished;
                } else {
                    return category.onHold;
                }
            });

            self.toggleText = ko.computed(function() {
                return self.paused() ? 'Activate campaign' :
                                       'Deactivate campaign';
            });

            self.activeToggle = function(campaign, event) {
                event.stopPropagation();

                console.log(campaign.status());

                // toggle paused state
                campaign.paused(!campaign.paused());

                var newState = campaign.paused(),
                    url = Urls.api_dispatch_detail('campaign', self.slug());

                return $.patchObject(url, { paused: newState })
                    .done(function() {
                        if (newState) {
                            notifications.show('Campaign deactivated', 2);
                        } else {
                            notifications.show('Campaign activated', 2);
                        }
                    });
            };
        };

        function CampaignList() {

            var self = this;

            // all campaigns
            self.campaigns = ko.observableArray();

            // campaigns filtered by category
            self.campaignsRunning = ko.computed(function() {
                return ko.utils.arrayFilter(self.campaigns(), function(item) {
                    return item.category() === category.running;
                });
            });

            self.campaignsOnHold = ko.computed(function() {
                return ko.utils.arrayFilter(self.campaigns(), function(item) {
                    return item.category() === category.onHold;
                });
            });

            self.campaignsFinished = ko.computed(function() {
                return ko.utils.arrayFilter(self.campaigns(), function(item) {
                    return item.category() === category.finished;
                });
            });

            self.loadCampaigns = function() {
                var url = Urls.api_dispatch_list('campaign');

                self.campaigns([]);

                return $.getJSON(url).done(function(response) {
                    self.campaigns(_.map(response.objects, function(c) {
                        return new Campaign(c);
                    }));
                });
            };

            self.removeCampaign = function(campaign, event) {
                event.stopPropagation();

                notifications.confirmDialog(
                    'Warning!',
                    'Are you sure to remove this campaign?',
                    function() {
                        var slug = campaign.slug(),
                            url = Urls.api_dispatch_detail('campaign', slug),
                            msg = 'Campaign was removed';

                        $.ajax({
                            url: url,
                            type: 'DELETE',
                            dataType: 'json',
                            contentType: 'application/json',
                            statusCode: {
                                204: function() {
                                    self.campaigns.remove(campaign);
                                    notifications.show(msg, 2);
                                }
                            }
                        });
                    }
                );
            };
        };

        return {
            CampaignList: new CampaignList()
        };
    }
);
