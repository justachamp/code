define(['notifications'],
    function(notifications) {
        var self = this;

        self.reports = ko.observableArray([]);

        self.reportsCount = ko.computed(function() {
            var len = self.reports().length,
                suffix = '';
            if (len !== 1) {
                suffix = 's';
            }
            return len + ' report' + suffix;
        }, self);


        self.load = function() {
            var apiUrl = Urls.api_dispatch_list('report');

            return $.getJSON(apiUrl).done(function(data) {
                self.reports(ko.mapping.fromJS(data.objects)());

                ko.utils.arrayForEach(self.reports(), function(report) {
                    report.remove = removeReport;
                });
            });
        };

        function removeReportBySlug(reportData) {
            var url = Urls.api_dispatch_detail('report', reportData.slug());

            $.ajax({
                type: 'DELETE',
                url: url,
                contentType: 'application/json',
                dataType: 'json'
            });

            self.reports.remove(reportData);
            notifications.show('Report was deleted.', 2);
        };

        function removeReport(reportData) {

            notifications.confirmDialog(
                'Warning!',
                'Are you sure to remove this report?',
                function() { removeReportBySlug(reportData); }
            );
        };

        return self;
    }
);
