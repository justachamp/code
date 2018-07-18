define(['models/reports.ui'], function(reports_ui) {
    suite('Components', function() {
        test('checks if ui controls are available', function() {
            assert.isObject(reports_ui.Table);
        });
    });

});
