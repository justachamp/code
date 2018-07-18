(function() {
  /* global moment*/
  'use strict';

  function DashboardSiteCtrl($scope, SiteService, $routeParams, pickerFormat, moment, usSpinnerService, $timeout) {
    var siteId = $routeParams.siteId;
    var Report = SiteService.getReportResource();
    var exportConfig;
    var serviceNames;
    var toolNames;
    $scope.colors = {
      facebook: '3b5998',
      twitter: '55acee',
      googlePlus: 'dc4a38',
      linkedin: '0077b5',
      pinterest: 'bd081c',
      instagram: '2e5c7f',
      digg: '333333',
      delicious: 'f7f7f7',
      stumbleupon: 'eb4823',
      gmail: 'e75a4d',
      whatsapp: '34af23',
      line: '00FF00',
      reddit: '000000',
      weibo: 'FF0000',
      tumblr: '35465c',
      sms: '0075D6',
      'address-bar': '0075d6',
      'copy-paste': 'ff9000',
      'sharing-buttons': '42c049',
      'newsletter-sharing-buttons': 'ff413e',
      copyLink: '00FF00',
      darkSocial: '131313'
    };
    serviceNames = {
      facebook: 'Facebook',
      twitter: 'Twitter',
      googlePlus: 'Google+',
      linkedin: 'LinkedIn',
      pinterest: 'Pinterest',
      instagram: 'Instagram',
      digg: 'Digg',
      delicious: 'Delicious',
      stumbleupon: 'StumbleUpon',
      gmail: 'Gmail',
      whatsapp: 'WhatsApp',
      line: 'Line',
      reddit: 'Reddit',
      tumblr: 'Tumblr',
      weibo: 'Weibo',
      sms: 'SMS',
      email: 'Email',
      others: 'Others',
      darkSocial: 'Dark Social',
      copyLink: 'Copy Link'
    };
    toolNames = {
      'address-bar': 'Address Bar',
      'copy-paste': 'Copy Paste',
      'sharing-buttons': 'Sharing Buttons',
      'newsletter-sharing-buttons': 'Newsletter Sharing Buttons'
    };
    $scope.dashboard = true;
    $scope.showSideBar = false;
    $scope.site = {};
    $scope.site.id = siteId;

    // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
    $scope.dateRange = {
      startDate: moment().utc().startOf('day').subtract(1, 'month'),
      endDate: moment().utc().endOf('day')
    };

    // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
    $scope.pickerOpts = {
      ranges: {
        'By day': [moment().utc().startOf('day'), moment().utc().endOf('day')],
        'By week': [moment().utc().startOf('day').subtract(1, 'week'), moment().utc().endOf('day')],
        'By month': [moment().utc().startOf('day').subtract(1, 'month'), moment().utc().endOf('day')],
        'By year': [moment().utc().startOf('day').subtract(1, 'year'), moment().utc().endOf('day')]
      },
      format: pickerFormat
    };

    $scope.toggleSideBar = function toggleSideBar() {
      $scope.showSideBar = !$scope.showSideBar;
    };

    $scope.startSpin = function startSpin() {
      //fix for issue https://github.com/urish/angular-spinner/issues/26
      $timeout(function() {
        usSpinnerService.spin('reportSpinner');
      }, 100);
    };

    $scope.stopSpin = function stopSpin() {
      $timeout(function() {
        usSpinnerService.stop('reportSpinner');
      }, 100);
    };

    //Watch for date changes
    $scope.$watch('dateRange', function(newDateRange) {
      queryReport(newDateRange);
    }, false);

    function queryReport(dateRange) {
      var query;
      var dtRange;
      query = {
        site: siteId
      };

      // jscs:disable requireCamelCaseOrUpperCaseIdentifiers
      if (!angular.isUndefined(dateRange.startDate)) {
        query.begin_date = moment(dateRange.startDate).unix();
      }

      if (!angular.isUndefined(dateRange.endDate)) {
        query.end_date = moment(dateRange.endDate).unix();
      }

      dtRange = query.end_date - query.begin_date;

      // jscs:enable requireCamelCaseOrUpperCaseIdentifiers
      query.aggregation = 'day';
      if (dtRange < 346000) {
        query.aggregation = 'hour';
      }

      $scope.startSpin();
      Report.get(query).$promise.then(function(response) {
        processResponse(response, query);
      }).finally(function() {
        $scope.stopSpin();
      });
    }

    function processResponse(response, query) {
      var data = response.data;

      if (query.aggregation === 'day') {
        $scope.charts.eventsSummary.categoryAxis.minPeriod = 'DD';
      } else if (query.aggregation === 'hour') {
        $scope.charts.eventsSummary.categoryAxis.minPeriod = 'hh';
      }

      $scope.eventsSummary = data.eventsSummary.map(function(v) {
        v.day = moment(v.date).toDate();
        return v;
      });

      $scope.sharesAndClicksByTool = data.sharesAndClicksByTool.map(function(v) {
        v.color = '#' + $scope.colors[v.tool];
        v.prettyName = toolNames[v.tool];
        return v;
      });

      $scope.topSocialChannels = data.topSocialChannels.map(function(v) {
        v.color = '#' + $scope.colors[v.source];
        v.prettyName = serviceNames[v.source];
        return v;
      });

      $scope.totalExternalShares = data.totalExternalShares.map(function(v) {
        v.color = '#' + $scope.colors[v.source];
        v.prettyName = serviceNames[v.source];
        return v;
      });

      $scope.topContentByShares = data.topContentByShares;
      $scope.topContentByClicks = data.topContentByClicks;
      $scope.referringDomains = data.referringDomains;
      $scope.searchTerms = data.searchTerms;
      $scope.searchEngines = data.searchEngines;
      $scope.copiedKeywords = data.topFrequentlyCopied;
      $scope.topCountries = data.topCountries;
      $scope.topCountriesMapData = data.topCountries.map(function(v) {
        var desc = v.shares + ' shares - ' + v.clicks + ' clicks';
        return {
          id: v.id,
          value: v.shares + v.clicks,
          description: desc
        };
      });
    }

    exportConfig = {
      enabled: true,
      libs: {autoLoad: false},
      position: 'bottom-left',
      menu: [{
        label: 'Export',
        class: 'export-main',
        menu: ['PNG', 'JPG', 'SVG', 'CVS']
      }]
    };

    $scope.showRange = true;
    $scope.charts = {
      sharesByTool: {
        dataProvider: [],
        allLabels: [{
          text: 'Shares',
          align: 'center',
          color: '#777A89',
          y: '45%'
        }],
        type: 'pie',
        theme: 'gravity4',
        titleField: 'prettyName',
        valueField: 'shares',
        responsive: {
          enabled: true
        }
      },
      clicksByTool: {
        dataProvider: [],
        allLabels: [{
          text: 'Clicks',
          align: 'center',
          color: '#777A89',
          y: '45%'
        }],
        type: 'pie',
        theme: 'gravity4',
        titleField: 'prettyName',
        valueField: 'clicks',
        responsive: {
          enabled: true
        }
      },
      eventsSummary: {
        dataProvider: [],

        //dataDateFormat: 'YYYY-MM-DD, JJ:NN:SS',
        valueField: 'day',
        height: 300,
        type: 'serial',
        theme: 'gravity4',
        graphs: [{
          id: 'g1',
          lineColor: '#0075D6',
          title: 'Shares',
          valueField: 'shares',
          balloonText: '[[category]]<br>Shares: [[value]]'
        },
          {
            id: 'g2',
            lineColor: '#FF9000',
            title: 'Clicks',
            valueField: 'clicks',
            balloonText: '[[category]]<br>Clicks: [[value]]'
          },
          {
            id: 'g3',
            lineColor: '#42C049',
            title: 'Follows',
            valueField: 'follows',
            balloonText: '[[category]]<br>Follows: [[value]]'
          },
          {
            id: 'g4',
            lineColor: '#FF413E',
            title: 'Copies',
            valueField: 'copies',
            balloonText: '[[category]]<br>Copies: [[value]]'
          },
          {
            id: 'g5',
            lineColor: '#1F3144',
            title: 'Views',
            valueField: 'views',
            balloonText: '[[category]]<br>Views: [[value]]'
          }],
        categoryField: 'day',
        categoryAxis: {
          minPeriod: 'DD',
          autoGridCount: false,
          minorGridEnabled: true,
          parseDates: true,
          dateFormats: [
            {
              period: 'fff',
              format: 'JJ:NN:SS'
            },
            {
              period: 'ss',
              format: 'JJ:NN:SS'
            },
            {
              period: 'mm',
              format: 'JJ:NN'
            },
            {
              period: 'hh',
              format: 'YYYY-MM-DD\nJJ:NN'
            },
            {
              period: 'DD',
              format: 'MMM DD'
            },
            {
              period: 'WW',
              format: 'MMM DD'
            },
            {
              period: 'MM',
              format: 'MMM'
            },
            {
              period: 'YYYY',
              format: 'YYYY'
            }
          ]
        }/*,
         responsive: {
         enabled: true,
         rules: [
         {
         maxWidth: 400,
         overrides: {
         autoMargins: false,
         legend: {
         enabled: false
         },
         categoryAxis: {
         labelsEnabled: false
         }
         }
         }
         ]
         }*/
      },
      topCountries: {
        type: 'map',
        theme: 'gravity4',
        dragMap: true,
        zoomOnDoubleClick: true,
        height: 400,
        dataProvider: {
          map: 'worldHigh',
          areas: []
        },
        zoomControl: {
          panControlEnabled: true,
          zoomControlEnabled: true
        },
        areasSettings: {
          autoZoom: false,
          balloonText: '[[title]]: [[description]]',
          descriptionWindowTop: -200
        },
        responsive: {
          enabled: true
        }
      },
      totalExternalShares: {
        dataProvider: [],
        allLabels: [{
          text: 'Shares',
          align: 'center',
          color: '#777A89',
          y: '45%'
        }],
        type: 'pie',
        theme: 'gravity4',
        titleField: 'prettyName',
        valueField: 'shares',
        responsive: {
          enabled: true
        }
      }
    };
  }

  angular.module('angulardash.site')
    .value('pickerFormat', 'YYYY-MM-DD')
    .constant('moment', moment)
    .controller('DashboardSiteCtrl', ['$scope', 'SiteService', '$routeParams', 'pickerFormat',
      'moment', 'usSpinnerService', '$timeout', DashboardSiteCtrl]);
})();
