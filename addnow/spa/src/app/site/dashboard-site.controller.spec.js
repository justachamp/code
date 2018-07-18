'use strict';

describe('Controller: DashboardSiteCtrl', function() {
  beforeEach(module('angulardash.site'));

  var $httpBackend;
  var $routeParams;
  var scope;
  var ctrl;
  var AppSettings;
  var backendApi;

  function getQuery(siteId) {
    return new RegExp(backendApi + 'digest\\?aggregation=day&(begin_date=([0-9])+&)?(end_date=([0-9])+&)?site=' + siteId);
  }

  beforeEach(inject(function($rootScope, $controller, _$httpBackend_, _$routeParams_, _AppSettings_) {
    $httpBackend = _$httpBackend_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;

    $httpBackend.expectGET(getQuery(1)).respond(
      200,
      {
        cached: false,
        data: {
          eventsSummary: [
            {views: 0, follows: 0, copies: 0, shares: 10, date: '2015-04-22 00:00:00', clicks: 0},
            {views: 0, follows: 0, copies: 0, shares: 4, date: '2015-04-24 00:00:00', clicks: 6},
            {views: 0, follows: 0, copies: 0, shares: 48, date: '2015-04-27 00:00:00', clicks: 15},
            {views: 0, follows: 0, copies: 0, shares: 18, date: '2015-04-28 00:00:00', clicks: 8},
            {views: 0, follows: 0, copies: 0, shares: 2, date: '2015-04-29 00:00:00', clicks: 1},
            {views: 0, follows: 0, copies: 0, shares: 5, date: '2015-04-30 00:00:00', clicks: 5},
            {views: 0, follows: 2, copies: 4, shares: 25, date: '2015-05-13 00:00:00', clicks: 19},
            {views: 0, follows: 0, copies: 0, shares: 0, date: '2015-05-14 00:00:00', clicks: 1}
          ],
          referringDomains: [
            {domain: 'gravity4.com', url: 'http://gravity4.com/blog/article/', count: 1}
          ],
          searchEngines: [],
          searchTerms: [],
          sharesAndClicksByTool: [
            {sharesPercent: 71.0, clicksPercent: 21.0, clicks: 12, shares: 80, tool: 'sharing-buttons'},
            {sharesPercent: 28.0, clicksPercent: 78.0, clicks: 43, shares: 32, tool: 'address-bar'}
          ],
          topContentByClicks: [
            {clicksPercent: 62.0, clicks: 5, url: 'http://testing.addnow.com/demo/', title: ''},
            {clicksPercent: 25.0, clicks: 2, url: 'http://addnow.com/press/', title: ''},
            {clicksPercent: 12.0, clicks: 1, url: 'http://gravity4.com/blog/article-2/', title: ''},
            {clicksPercent: 0.0, clicks: 0, url: 'http://en.wikipedia.org/', title: ''}
          ],
          topContentByShares: [
            {sharesPercent: 55.0, shares: 5, url: 'http://testing.addnow.com/demo/', title: ''},
            {sharesPercent: 33.0, shares: 3, url: 'http://addnow.com/press/', title: ''},
            {sharesPercent: 11.0, shares: 1, url: 'http://en.wikipedia.org/', title: ''},
            {sharesPercent: 0.0, shares: 0, url: 'http://gravity4.com/blog/article-2/', title: ''}
          ],
          topCountries: [
            {country: 'AR', id: 'AR', shares: 58, clicks: 24, viralLift: 0},
            {country: 'US', id: 'US', shares: 28, clicks: 23, viralLift: 0},
            {country: 'PT', id: 'PT', shares: 24, clicks: 6, viralLift: 0},
            {country: 'UA', id: 'UA', shares: 2, clicks: 2, viralLift: 1}
          ],
          topFrequentlyCopied: [
            {copies: 1, keyword: 'analytics'},
            {copies: 1, keyword: 'consulting'},
            {copies: 1, keyword: 'web development'}
          ],
          topSocialChannels: [
            {sharesPercent: 39.0, clicksPercent: 3.0, clicks: 2, shares: 44, source: 'sms'},
            {sharesPercent: 21.0, clicksPercent: 52.0, clicks: 29, shares: 24, source: 'instagram'},
            {sharesPercent: 13.0, clicksPercent: 16.0, clicks: 9, shares: 15, source: 'googlePlus'},
            {sharesPercent: 7.0, clicksPercent: 25.0, clicks: 14, shares: 8, source: 'darkSocial'},
            {sharesPercent: 6.0, clicksPercent: 0.0, clicks: 0, shares: 7, source: 'digg'},
            {sharesPercent: 5.0, clicksPercent: 0.0, clicks: 0, shares: 6, source: 'facebook'},
            {sharesPercent: 2.0, clicksPercent: 0.0, clicks: 0, shares: 3, source: 'twitter'},
            {sharesPercent: 1.0, clicksPercent: 0.0, clicks: 0, shares: 2, source: 'whatsapp'},
            {sharesPercent: 0.0, clicksPercent: 1.0, clicks: 1, shares: 1, source: 'linkedin'},
            {sharesPercent: 0.0, clicksPercent: 0.0, clicks: 0, shares: 1, source: 'pinterest'},
            {sharesPercent: 0.0, clicksPercent: 0.0, clicks: 0, shares: 1, source: 'delicious'}
          ],
          totalExternalShares: [
            {source: 'facebook', sharesPercent: 84, shares: 1772290},
            {source: 'googlePlus', sharesPercent: 13, shares: 277908},
            {source: 'pinterest', sharesPercent: 2, shares: 44412},
            {source: 'twitter', sharesPercent: 0, shares: 3871},
            {source: 'linkedin', sharesPercent: 0, shares: 2601}
          ]
        }
      }
    );
    $routeParams = _$routeParams_;
    $routeParams.siteId = 1;
    scope = $rootScope.$new();
    ctrl = $controller('DashboardSiteCtrl', {$scope: scope});
  }));

  it('should create eventsSummary fetched from xhr', function() {
    $httpBackend.flush();
    expect(scope.eventsSummary).toEqual([
      {views: 0, follows: 0, copies: 0, shares: 10, date: '2015-04-22 00:00:00', clicks: 0, day: new Date(2015, 3, 22)},
      {views: 0, follows: 0, copies: 0, shares: 4, date: '2015-04-24 00:00:00', clicks: 6, day: new Date(2015, 3, 24)},
      {views: 0, follows: 0, copies: 0, shares: 48, date: '2015-04-27 00:00:00', clicks: 15, day: new Date(2015, 3, 27)},
      {views: 0, follows: 0, copies: 0, shares: 18, date: '2015-04-28 00:00:00', clicks: 8, day: new Date(2015, 3, 28)},
      {views: 0, follows: 0, copies: 0, shares: 2, date: '2015-04-29 00:00:00', clicks: 1, day: new Date(2015, 3, 29)},
      {views: 0, follows: 0, copies: 0, shares: 5, date: '2015-04-30 00:00:00', clicks: 5, day: new Date(2015, 3, 30)},
      {views: 0, follows: 2, copies: 4, shares: 25, date: '2015-05-13 00:00:00', clicks: 19, day: new Date(2015, 4, 13)},
      {views: 0, follows: 0, copies: 0, shares: 0, date: '2015-05-14 00:00:00', clicks: 1, day: new Date(2015, 4, 14)}
    ]);
  });

  it('should create referringDomains fetched from xhr with percent added', function() {
    $httpBackend.flush();
    expect(scope.referringDomains).toEqual([
      {domain: 'gravity4.com', url: 'http://gravity4.com/blog/article/', count: 1}
    ]);
  });

  it('should create sharesAndClicksByTool fetched from xhr and with percents added', function() {
    $httpBackend.flush();
    expect(scope.sharesAndClicksByTool).toEqual([
      {sharesPercent: 71, clicksPercent: 21, clicks: 12, shares: 80, tool: 'sharing-buttons', color: '#42c049', prettyName: 'Sharing Buttons'},
      {sharesPercent: 28, clicksPercent: 78, clicks: 43, shares: 32, tool: 'address-bar', color: '#0075d6', prettyName: 'Address Bar'}
    ]);
  });

  it('should create topContentByClicks fetched from xhr', function() {
    $httpBackend.flush();
    expect(scope.topContentByClicks).toEqual([
      {clicksPercent: 62.0, clicks: 5, url: 'http://testing.addnow.com/demo/', title: ''},
      {clicksPercent: 25.0, clicks: 2, url: 'http://addnow.com/press/', title: ''},
      {clicksPercent: 12.0, clicks: 1, url: 'http://gravity4.com/blog/article-2/', title: ''},
      {clicksPercent: 0.0, clicks: 0, url: 'http://en.wikipedia.org/', title: ''}
    ]);
  });

  it('should create topContentByShares fetched from xhr', function() {
    $httpBackend.flush();
    expect(scope.topContentByShares).toEqual([
      {sharesPercent: 55.0, shares: 5, url: 'http://testing.addnow.com/demo/', title: ''},
      {sharesPercent: 33.0, shares: 3, url: 'http://addnow.com/press/', title: ''},
      {sharesPercent: 11.0, shares: 1, url: 'http://en.wikipedia.org/', title: ''},
      {sharesPercent: 0.0, shares: 0, url: 'http://gravity4.com/blog/article-2/', title: ''}
    ]);
  });

  it('should create topCountries fetched from xhr', function() {
    $httpBackend.flush();
    expect(scope.topCountries).toEqual([
      {country: 'AR', id: 'AR', shares: 58, clicks: 24, viralLift: 0},
      {country: 'US', id: 'US', shares: 28, clicks: 23, viralLift: 0},
      {country: 'PT', id: 'PT', shares: 24, clicks: 6, viralLift: 0},
      {country: 'UA', id: 'UA', shares: 2, clicks: 2, viralLift: 1}
    ]);
  });

  it('should create copiedKeywords fetched from xhr', function() {
    $httpBackend.flush();
    expect(scope.copiedKeywords).toEqual([
      {copies: 1, keyword: 'analytics'},
      {copies: 1, keyword: 'consulting'},
      {copies: 1, keyword: 'web development'}
    ]);
  });

  it('should create topSocialChannels fetched from xhr and with percents added', function() {
    $httpBackend.flush();
    expect(scope.topSocialChannels).toEqual([
      {sharesPercent: 39, clicksPercent: 3, clicks: 2, shares: 44, source: 'sms', color: '#0075D6', prettyName: 'SMS'},
      {sharesPercent: 21, clicksPercent: 52, clicks: 29, shares: 24, source: 'instagram', color: '#2e5c7f', prettyName: 'Instagram'},
      {sharesPercent: 13, clicksPercent: 16, clicks: 9, shares: 15, source: 'googlePlus', color: '#dc4a38', prettyName: 'Google+'},
      {sharesPercent: 7, clicksPercent: 25, clicks: 14, shares: 8, source: 'darkSocial', color: '#131313', prettyName: 'Dark Social'},
      {sharesPercent: 6, clicksPercent: 0, clicks: 0, shares: 7, source: 'digg', color: '#333333', prettyName: 'Digg'},
      {sharesPercent: 5, clicksPercent: 0, clicks: 0, shares: 6, source: 'facebook', color: '#3b5998', prettyName: 'Facebook'},
      {sharesPercent: 2, clicksPercent: 0, clicks: 0, shares: 3, source: 'twitter', color: '#55acee', prettyName: 'Twitter'},
      {sharesPercent: 1, clicksPercent: 0, clicks: 0, shares: 2, source: 'whatsapp', color: '#34af23', prettyName: 'WhatsApp'},
      {sharesPercent: 0, clicksPercent: 1, clicks: 1, shares: 1, source: 'linkedin', color: '#0077b5', prettyName: 'LinkedIn'},
      {sharesPercent: 0, clicksPercent: 0, clicks: 0, shares: 1, source: 'pinterest', color: '#bd081c', prettyName: 'Pinterest'},
      {sharesPercent: 0, clicksPercent: 0, clicks: 0, shares: 1, source: 'delicious', color: '#f7f7f7', prettyName: 'Delicious'}
    ]);
  });

  it('should create totalExternalShares fetched from xhr and with percents added', function() {
    $httpBackend.flush();
    expect(scope.totalExternalShares).toEqual([
      {source: 'facebook', sharesPercent: 84, shares: 1772290, color: '#3b5998', prettyName: 'Facebook'},
      {source: 'googlePlus', sharesPercent: 13, shares: 277908, color: '#dc4a38', prettyName: 'Google+'},
      {source: 'pinterest', sharesPercent: 2, shares: 44412, color: '#bd081c', prettyName: 'Pinterest'},
      {source: 'twitter', sharesPercent: 0, shares: 3871, color: '#55acee', prettyName: 'Twitter'},
      {source: 'linkedin', sharesPercent: 0, shares: 2601, color: '#0077b5', prettyName: 'LinkedIn'}
    ]);
  });
});
