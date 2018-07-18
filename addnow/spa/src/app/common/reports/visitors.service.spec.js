'use strict';

describe('Service: VisitorsService', function() {
  beforeEach(module('angulardash.common'));

  var $rootScope;
  var $httpBackend;
  var VisitorsService;
  var AppSettings;
  var backendApi;

  beforeEach(inject(function(_$rootScope_, _$httpBackend_, _VisitorsService_, _AppSettings_) {
    $rootScope = _$rootScope_;
    $httpBackend = _$httpBackend_;
    VisitorsService = _VisitorsService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;
  }));

  function setHistoryMock(longitude, latitude, ts) {
    $httpBackend.expectGET(backendApi + 'reports/sites/1/visitors?history=' + VisitorsService.maxVisitorTime)
      .respond(200, [
        {
          geo: {
            longitude: longitude,
            latitude: latitude,
            city: 'London',
            country: 'UK'
          },
          browser: 'Firefox',
          ts: ts
        }
      ]);
  }

  function setRealMock(longitude, latitude, sourceValue) {
    $httpBackend.expectGET(backendApi + 'reports/sites/1/visitors')
      .respond(200, [
        {
          geo: {
            longitude: longitude,
            latitude: latitude,
            city: 'London',
            country: 'UK'
          },
          browser: 'Firefox',
          source: sourceValue
        }
      ]);
  }

  describe('getVisitors', function() {
    it('uses longitude and latitude for key', function() {
      var now = moment().utc();
      var ts = now.toISOString();
      var places;
      var length;
      var v;

      setHistoryMock(10, 20, ts);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
        length = result.activeCount;
      });

      $httpBackend.flush();
      v = places['10,20'];
      expect(length).toBeUndefined();
      expect(v).toBeDefined();
      expect(v.geo).toBeDefined();
      expect(v.geo.longitude).toBe(10);
      expect(v.geo.latitude).toBe(20);
      expect(v.geo.city).toBe('London');
      expect(v.geo.country).toBe('UK');
      expect(v.browser).toBe('Firefox');
    });

    it('calculates visitor time', function() {
      var now = moment().utc();
      var ts = now.toISOString();
      var places;
      var v;

      setHistoryMock(10, 20, ts);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();
      v = places['10,20'];
      expect(v.time).toBeDefined();
    });

    it('collects visitors from previous call', function() {
      var now = moment().utc();
      var ts = now.toISOString();
      var places;

      setHistoryMock(10, 20, ts);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();

      setHistoryMock(11, 22, ts);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();
      expect(places['10,20']).toBeDefined();
      expect(places['11,22']).toBeDefined();
    });

    it('return activeCount', function() {
      var places;
      var length;

      setRealMock(10, 20, 'google');
      VisitorsService.getVisitors(1, false).then(function(result) {
        places = result.places;
        length = result.activeCount;
      });

      $httpBackend.flush();

      expect(places['10,20']).toBeDefined();
      expect(length).toBe(1);
    });

    it('return source', function() {
      var places;

      setRealMock(10, 20, 'google');
      VisitorsService.getVisitors(1, false).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();

      expect(places['10,20']).toBeDefined();
      expect(places['10,20'].source).toBe('google');
    });

    it('return direct source for empty value', function() {
      var places;

      setRealMock(10, 20, '(not set)');
      VisitorsService.getVisitors(1, false).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();

      expect(places['10,20']).toBeDefined();
      expect(places['10,20'].source).toBe('direct');

      setRealMock(10, 20, '(not set)');
      VisitorsService.getVisitors(1, false).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();

      expect(places['10,20']).toBeDefined();
      expect(places['10,20'].source).toBe('direct');
    });

    it('makes old visitors expired', function() {
      var now = moment().utc();
      var oldTs = now.clone().subtract(2, 'h').toISOString();
      var newTs = now.toISOString();
      var places;

      setHistoryMock(10, 20, oldTs);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();

      setHistoryMock(11, 22, newTs);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();
      expect(places['11,22']).toBeDefined();
    });
  });

  describe('updates time', function() {
    var now = moment().utc();
    var ts = now.toISOString();
    var places;
    var firstVal;

    beforeEach(function(done) {
      setHistoryMock(10, 20, ts);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();
      firstVal = places['10,20'].time;
      setTimeout(function() {
        done();
      }, 1000);
    });

    it('every api requests', function() {
      $httpBackend.expectGET(
        backendApi + 'reports/sites/1/visitors?history=' + VisitorsService.maxVisitorTime
      ).respond(200, []);
      VisitorsService.getVisitors(1, true).then(function(result) {
        places = result.places;
      });

      $httpBackend.flush();
      expect(places['10,20'].time).toBeGreaterThan(firstVal);
    });
  });
});
