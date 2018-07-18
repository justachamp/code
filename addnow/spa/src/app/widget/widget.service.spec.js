'use strict';

describe('Widget Service', function() {
  beforeEach(module('angulardash.widget'));

  var $httpBackend;
  var WidgetService;
  var AppSettings;
  var backendApi;

  beforeEach(inject(function(_$httpBackend_, _WidgetService_, _AppSettings_) {
    $httpBackend = _$httpBackend_;
    WidgetService = _WidgetService_;
    AppSettings = _AppSettings_;
    backendApi = AppSettings.backendApi;
  }));

  it('create', function() {
    $httpBackend.expectPOST(backendApi + 'sites/1/widgets').respond(200, {ok: true});
    WidgetService.addConfiguration(1, {key: 'value'});
    $httpBackend.flush();
  });

  it('getById', function() {
    $httpBackend.expectGET(backendApi + 'sites/1/widgets/1').respond(200, {id: 123});
    WidgetService.getConfigurationById(1, 1);
    $httpBackend.flush();
  });

  it('edit', function() {
    $httpBackend.expectPATCH(backendApi + 'sites/1/widgets/1').respond(200, {id: 123});
    WidgetService.editConfiguration(1, 1, {key: 'value'});
    $httpBackend.flush();
  });

  it('list', function() {
    $httpBackend.expectGET(backendApi + 'sites/1/widgets').respond(200, {id: 123});
    WidgetService.getConfigurations(1);
    $httpBackend.flush();
  });

  it('list with type', function() {
    $httpBackend.expectGET(backendApi + 'sites/1/widgets?type=test').respond(200, {id: 123});
    WidgetService.getConfigurations(1, 'test');
    $httpBackend.flush();
  });
});
