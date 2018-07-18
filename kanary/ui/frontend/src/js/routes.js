/**
List of routes defined in following format:
[route_name, route_pattern, additional_params, [callback_name]]

additional_params is object.
callback_name is a function defined in route_callbacks object in router.js
file. This callbacks are called with additional_params as first argument,
and vals returned from crossroads as second.

 */

define([], function() {

    var routes = [
        ['root', '/', {
            menu: 'dashboard',
            sidebar: 'sidebarDashboard',
            content: 'contentDashboard'
        }],
        ['dashboard', 'dashboard', {
            menu: 'dashboard',
            sidebar: 'sidebarDashboard',
            content: 'contentDashboard'
        }],

        // Storage
        ['storage', 'storage', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorage'
        }],
        ['new_creative', 'storage/creative-create', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageCreativeNew'
        }],
        ['storage_creative', 'storage/creative/{id}', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageCreative'
        }],
        ['creative_id', 'creative_id/{id}', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageCreative'
        }],
        ['new_audience', 'storage/new_audience', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageAudienceNew'
        }],
        ['storage_audience', 'storage/audience/{id}', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageAudience'
        }],
        ['new_trigger', 'storage/new_trigger', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageNewTrigger'
        }],
        ['new_brand', 'storage/brand-create', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageBrandNew'
        }],
        ['storage_brand', 'storage/brand/{id}', {
            menu: 'storage',
            sidebar: 'sidebarStorage',
            content: 'contentStorageBrand'
        }],

        // Campaigns
        ['campaigns', 'campaigns', {
            menu: 'campaigns',
            sidebar: 'sidebarCampaigns',
            content: 'contentCampaigns'
        }],
        ['new_campaign', 'campaigns-create/overall', {
            menu: 'campaigns',
            sidebar: 'sidebarNewCampaign',
            content: 'contentNewCampaign'
        }],
        ['new_campaign_budget', 'campaigns-create/budget', {
            menu: 'campaigns',
            sidebar: 'sidebarNewCampaign',
            content: 'contentNewCampaignBudget'
        }],
        ['new_campaign_conversion', 'campaigns-create/conversion', {
            menu: 'campaigns',
            sidebar: 'sidebarNewCampaign',
            content: 'contentNewCampaignConversion'
        }],
        ['new_campaign_capping', 'campaigns-create/capping', {
            menu: 'campaigns',
            sidebar: 'sidebarNewCampaign',
            content: 'contentNewCampaignCapping'
        }],
        ['new_campaign_adx_setup_campaign', 'campaigns-create/campaigns', {
            menu: 'campaigns',
            sidebar: 'sidebarNewCampaign',
            content: 'contentNewADXSetupCampaign'
        }],
        ['new_campaign_adx_pretargeting', 'campaigns-create/adx_pretargeting', {
            menu: 'campaigns',
            sidebar: 'sidebarNewTargeting',
            content: 'contentNewADXPretargeting'
        }],
        ['new_campaign_adx_ad_serving_setup', 'campaigns-create/adx_ad_serving_setup', {
            menu: 'campaigns',
            sidebar: 'sidebarNewTargeting',
            content: 'contentNewADXAdServingSetup'
        }],
        ['new_campaign_adx_ddm_reporting', 'campaigns-create/adx_ddm_reporting', {
            menu: 'campaigns',
            sidebar: 'sidebarNewTargeting',
            content: 'contentNewADXDDMReporting'
        }],
        ['new_campaign_adx_rtb_reporting', 'campaigns-create/adx_rtb_reporting', {
            menu: 'campaigns',
            sidebar: 'sidebarNewTargeting',
            content: 'contentNewADXRTBReporting'
        }],
        ['campaign', 'campaigns/{campaignName}', {
            menu: 'campaigns',
            sidebar: 'sidebarCampaign',
            content: 'contentCampaign'
        }],
        ['campaign_overview',
        'campaigns/{campaignName}/overview/:overviewParams*:', {
            menu: 'campaigns',
            sidebar: 'sidebarCampaign',
            content: 'contentCampaign'
        }],
        ['campaign_id', 'campaign_id/{id}', 'campaign', 'routeToObject'],
        ['campaign_api', 'campaigns/{slug}', {
            menu: 'campaigns',
            sidebar: 'sidebarCampaign',
            content: 'contentCampaign'
        }],
        ['edit_campaign', 'campaigns/{campaignName}/edit/overall', {
            menu: 'campaigns',
            sidebar: 'sidebarEditCampaign',
            content: 'contentEditCampaign'
        }],
        ['edit_campaign_budget', 'campaigns/{campaignName}/edit/budget', {
            menu: 'campaigns',
            sidebar: 'sidebarEditCampaign',
            content: 'contentEditCampaignBudget'
        }],
        ['edit_campaign_conversion',
        'campaigns/{campaignName}/edit/conversion', {
            menu: 'campaigns',
            sidebar: 'sidebarEditCampaign',
            content: 'contentEditCampaignConversion'
        }],
        ['edit_campaign_capping', 'campaigns/{campaignName}/edit/capping', {
            menu: 'campaigns',
            sidebar: 'sidebarEditCampaign',
            content: 'contentEditCampaignCapping'
        }],
        ['new_strategy', 'campaigns/{campaignName}/newStrategy', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategy'
        }],
        ['new_strategy_targeting',
        'campaigns/{campaignName}/newStrategy/targeting', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategyTargeting'
        }],
        ['new_strategy_publishers',
        'campaigns/{campaignName}/newStrategy/publishers', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewPublisherSet'
        }],
        ['new_strategy_landing_pages',
        'campaigns/{campaignName}/newStrategy/landing_pages', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategyLandingPages'
        }],
        ['new_strategy_creatives',
        'campaigns/{campaignName}/newStrategy/creatives', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategyCreatives'
        }],
        ['new_strategy_bidding',
        'campaigns/{campaignName}/newStrategy/bidding', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategyBidding'
        }],
        ['new_startegy_retargeting',
        'campaigns/{campaignName}/newStrategy/retargeting', {
            menu: 'campaigns',
            sidebar: 'sidebarNewStrategy',
            content: 'contentNewStrategyRetargeting'
        }],
        ['strategy', 'campaigns/{campaignName}/{strategyName}', {
            menu: 'campaigns',
            sidebar: 'sidebarStrategy',
            content: 'contentStrategy'
        }],
        ['strategy_creative', 'campaigns/{campaignName}/{strategyName}/' +
         'creative/{id}', {
            menu: 'campaigns',
            sidebar: 'sidebarStrategy',
            content: 'contentStorageCreative'
        }],
        ['strategy_overview',
        'campaigns/{campaignName}/{strategyName}/overview/:overviewParams*:', {
            menu: 'campaigns',
            sidebar: 'sidebarStrategy',
            content: 'contentStrategy'
        }],
        ['strategy_id', 'strategy_id/{id}', 'strategy', 'routeToObject'],
        ['strategy_api', 'campaigns/{campaign_slug}/{slug}', {
            menu: 'campaigns',
            sidebar: 'sidebarStrategy',
            content: 'contentStrategy'
        }],
        ['edit_strategy', 'campaigns/{campaignName}/{strategyName}/edit', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditStrategy'
        }],
        ['edit_strategy_targeting',
        'campaigns/{campaignName}/{strategyName}/edit/targeting', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditStrategyTargeting'
        }],
        ['edit_strategy_landing_pages',
        'campaigns/{campaignName}/{strategyName}/edit/landing_pages', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditStrategyLandingPages'
        }],
        ['edit_strategy_publishers',
        'campaigns/{campaignName}/{strategyName}/edit/publishers', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditPublisherSet'
        }],
        ['edit_strategy_creatives',
        'campaigns/{campaignName}/{strategyName}/edit/creatives', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditStrategyCreatives'
        }],
        ['edit_strategy_bidding',
        'campaigns/{campaignName}/{strategyName}/edit/bidding', {
            menu: 'campaigns',
            sidebar: 'sidebarEditStrategy',
            content: 'contentEditStrategyBidding'
        }],

        // Reports
        ['reports', 'reports', {
            menu: 'reports',
            sidebar: 'sidebarReports',
            content: 'contentReports'
        }],
        ['new_report', 'reports-create/', {
            menu: 'reports',
            sidebar: 'sidebarNewReport',
            content: 'contentNewReport'
        }],
        ['new_report_filters', 'reports-create/filters', {
            menu: 'reports',
            sidebar: 'sidebarNewReport',
            content: 'contentNewReportFilters'
        }],
        ['new_report_data_src', 'reports-create/data_sources', {
            menu: 'reports',
            sidebar: 'sidebarNewReport',
            content: 'contentNewReportDatasources'
        }],
        ['report_edit', 'reports/{slug}/edit', {
            menu: 'reports',
            sidebar: 'sidebarEditReport',
            content: 'contentEditReport'
        }],
        ['report', 'reports/{slug}/:params*:', {
            menu: 'reports',
            sidebar: 'sidebarReport',
            content: 'contentReport'
        }],
        ['report_id', 'report_id/{id}/', 'report', 'routeToObject'],
        ['report_api', 'reports/{slug}/', {
            menu: 'reports',
            sidebar: 'sidebarReport',
            content: 'contentReport'
        }],
        ['report_new_data_source_set',
        'reports/{slug}/advanced/new_data_source_set', {
            menu: 'reports',
            sidebar: 'sidebarNewDataSourceSet',
            content: 'contentUnderConstruction'
        }],
        ['report_advanced', 'reports/{slug}/advanced', {
            menu: 'reports',
            sidebar: 'sidebarAdvancedReport',
            content: 'contentReport'
        }],

        // Accounts
        ['account', 'account', {
            menu: 'appsettings',
            sidebar: 'sidebarAccount',
            content: 'contentAccountInformation'
        }],
        ['billing', 'account/billing', {
            menu: 'appsettings',
            sidebar: 'sidebarAccount',
            content: 'contentAccountBilling'
        }],
        ['payment', 'account/payment', {
            menu: 'appsettings',
            sidebar: 'sidebarAccount',
            content: 'contentAccountPayment'
        }],

        // Other
        ['livedata', 'livedata', {
            menu: 'livedata',
            sidebar: 'sidebarLiveData',
            content: 'contentUnderConstruction'
        }],
        ['appsettings', 'appsettings', {
            menu: 'appsettings',
            sidebar: 'sidebarAppSettings',
            content: 'contentUnderConstruction'
        }],
        ['appstore', 'appstore', {
            menu: 'appstore',
            sidebar: 'sidebarAppStore',
            content: 'contentAppstore'
        }],
        ['appstore_trim', 'appstore/trim', {
            menu: 'appstore',
            sidebar: 'sidebarAppStore',
            content: 'contentAppstoreTrim'
        }]
    ];

    return routes;
});
