'use strict';

var signin = require('./pages/signin');
var dashboard = require('./pages/dashboard');
var dateUtils = require('./helpers/date-utils');

describe('Dashboard View', function() {
  var siteId = 1;
  var login = 'test@test.pl';
  var password = '123qwe';

  describe('Not logged user in', function() {
    it('should kick user when not logged in', function() {
      dashboard.openDashboard(siteId);
      expect(browser.getLocationAbsUrl()).toBe('/signin/');
    });

    it('should not kick user when signed in', function() {
      signin.login(login, password);
      expect(browser.getLocationAbsUrl()).toBe(dashboard.getDashboardPage(siteId));
    });
  });

  describe('Logged user in', function() {
    beforeAll(function() {
      signin.login(login, password);
    });

    describe('Site dashboard view', function() {
      beforeEach(function() {
        dashboard.openDashboard(siteId);
      });

      var pickerTests = function(periods) {

        periods.forEach(function(period) {
          it('should contain `by ' + period + '` datepicker', function() {
            var button = dashboard.getDatePickerPeriodButton(period);

            //hack for bamboo running
            button.isDisplayed().then(function(isVisible) {
              if (!isVisible) {
                dashboard.openDatePicker();
              }

              button.click();

              expect(dashboard.getDatePickerValue()).toBe(dateUtils.buildDatePickerValue(period));
            });
          });
        });
      };

      pickerTests(['day', 'week', 'month', 'year']);

      describe('Events summary widget', function() {
        it('should have one chart', function() {
          expect(dashboard.hasOneMainChart()).toBeTruthy();
        });
      });

      describe('Shares and clicks by tool widget', function() {

        it('should have 3 rows', function() {
          expect(dashboard.getSharesAndClicksByToolRowsCount()).toBe(3);
        });

        it('should be ordered by shares', function() {
          var expected = [
              ['89%', '25'],
              ['7%', '2'],
              ['4%', '1']
          ];
          dashboard.getSharesAndClicksByToolItemSharesPercents().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][0]);
          });

          dashboard.getSharesAndClicksByToolItemShares().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][1]);
          });
        });

        it('should have two charts', function() {
          expect(dashboard.getSummaryMainChartsCount()).toBe(2);
        });
      });

      describe('Top social channels widget', function() {

        it('should have 4 rows', function() {
          expect(dashboard.getTopSocialChannelsRowsCount()).toBe(4);
        });

        it('should be ordered by shares', function() {
          var expected = [
                  ['61%', '17'],
                  ['36%', '10'],
                  ['4%', '1'],
                  ['0%', '0']
              ];
          dashboard.getTopSocialChannelsItemSharesPercent().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][0]);
          });

          dashboard.getTopSocialChannelsItemShares().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][1]);
          });
        });
      });

      describe('Top content widgets', function() {
        describe('Top shared content', function() {
          it('should be ordered by shares', function() {
            var expected = [
                ['93%', '26'],
                ['7%', '2']
            ];
            dashboard.getTopContentBySharesItemSharesPercent().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][0]);
            });

            dashboard.getTopContentBySharesItemShares().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][1]);
            });
          });

          it('should have 2 rows', function() {
            expect(dashboard.getTopContentBySharesRowsCount()).toBe(2);
          });
        });

        describe('Top clicked content', function() {
          it('should have 2 rows for top clicked content', function() {
            expect(dashboard.getTopContentByClicksRowsCount()).toBe(2);
          });

          it('should be ordered by clicks', function() {
            var expected = [
                ['88%', '38'],
                ['12%', '5']
            ];
            dashboard.getTopContentBySharesItemClicksPercent().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][0]);
            });

            dashboard.getTopContentBySharesItemClicks().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][1]);
            });
          });
        });
      });

      describe('Top copied keywords widget', function() {

        it('should have 3 rows', function() {
          expect(dashboard.getKeywordsCount()).toBe(4);
        });

        it('should be ordered by copies', function() {
          var expected = [
                  '3',
                  '2',
                  '2',
                  '1'
              ];
          dashboard.getKeywordsItemCopies().each(function(row, index) {
            expect(row.getText()).toBe(expected[index]);
          });
        });
      });

      //no reffering domains presented
      xdescribe('Referring domains widget', function() {
        var referringRows;

        beforeEach(function() {
          referringRows = element.all(by.repeater('referringDomainsItem in referringDomains'));
        });

        it('should have 1 rows', function() {
          expect(referringRows.count()).toBe(1);
        });

        it('should be ordered by count', function() {
          var expected = ['1'];
          var count = 0;
          element.all(by.binding('referringDomainsItem.count')).each(function(row) {
            expect(row.getText()).toBe(expected[count++]);
          });
        });
      });

      describe('Top countries widget', function() {

        describe('Top countries list', function() {
          it('should have 2 rows', function() {
            expect(dashboard.getTopCountriesCount()).toBe(2);
          });

          it('should be ordered by shares and clicks', function() {
            var expected = [
                    ['26', '5'],
                    ['2', '38']
                ];
            dashboard.getTopCountriesShares().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][0]);
            });

            dashboard.getTopCountriesClicks().each(function(row, index) {
              expect(row.getText()).toBe(expected[index][1]);
            });
          });
        });

        it('top countries map should have an amcharts map', function() {
          expect(dashboard.getGeoMapsCount()).toBe(1);
        });
      });

      describe('Total external shares', function() {

        it('should have 2 rows', function() {
          expect(dashboard.getTotalExternalSharesCount()).toBe(3);
        });

        it('should be ordered by shares', function() {
          var expected = [
                  ['55%', '2,314'],
                  ['29%', '1,240'],
                  ['16%', '679']
              ];
          dashboard.getTotalExternalSharesItemSharesPercent().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][0]);
          });

          dashboard.getTotalExternalSharesItemShares().each(function(row, index) {
            expect(row.getText()).toBe(expected[index][1]);
          });
        });
      });
    });
  });
});
