Report models and corresponding managers; order by class hierarchy popularity and length
========================================================================================

In tables below 'Report query identity' columns list names of Report table columns that must be used to select only
records that belong to single report series on chart or one report row in table.
The first element in 'Report query identity' column is the table column name used to IN filtering in WHERE clause.
The second column is used for extra filtering to get only report records related to current view (current strategy
or campaign). You need to know chart queries are very inconsistent. Types of chart queries:

1. Queries with only related_id(s) - related ids used in IN filtering.
2. Queries with dimension_id and related_id - dimension_id used for IN filtering and used to select records that belong
   to given campaign/strategy.
3. Queries with dimension and related_id - same as above but dimension is a string (URL).

BaseReportManager._report_chart_where method recognises what is needed to query for given report based on values of its
single_series_identifier and report_base_identifier.


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Strategy Report views                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+
| Model                                                                                                         | Manager                                               | Report query identity    |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+
| BaseReportAdvert <- ReportAdvert                                                                              | ReportAdvertManager                                   | related_id               |
| BaseReportStrategy <- BaseReportPublisherStrategy <- BaseReportDimension <- ReportStrategyPublisher           | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- ReportStrategyPublisherNetwork                                   | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseReportSite <- ReportStrategySite                             | ReportSiteManager                                     | dimension,    related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyCategory                   | ReportCategoryManager (HAS OWN REPORT_CHART)          | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyPeer39Brand                | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyPeer39Contextual           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyPeer39Language             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyPeer39Quality              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicContext            | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicLanguage           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicMaturity           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicNotice             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicPlace              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicQuality            | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyProximicSafety             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyLotameDemographic          | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyLotameAdvancedDemographic  | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyLotameBehavioralInterest   | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyLotameInfluencers          | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportDimension <- BaseMultivalueReport <- ReportStrategyLotameOffline              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyAge               | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyCarrier           | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyCity              | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyCountry           | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyDomain            | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyGender            | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyMake              | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyModel             | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyOs                | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyPosition          | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportStrategy <- BaseReportTargetValueStrategy <- BaseReportDimension <- ReportStrategyRegion            | ReportTargetValueManager                              | dimension_id, related_id |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+


+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Campaign Report views                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+
| Model                                                                                                         | Manager                                               | Report query identity    |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+
| BaseReportStrategy <- ReportStrategy                                                                          | ReportCampaignManager <- ReportStrategyManager        | related_id               |
| BaseReportCampaign <- BaseReportDimension <- ReportCampaignPublisher                                          | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- ReportCampaignPublisherNetwork                                   | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseReportSite <- ReportCampaignSite                             | ReportSiteManager                                     | dimension,    related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignCategory                   | ReportCategoryManager  (HAS OWN REPORT_CHART)         | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignPeer39Brand                | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignPeer39Contextual           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignPeer39Language             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignPeer39Quality              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicContextual         | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicLanguage           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicMaturity           | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicNotice             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicPlace              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicQuality            | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignProximicSafety             | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignLotameDemographic          | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignLotameAdvancedDemographic  | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignLotameBehavioralInterest   | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignLotameInfluencers          | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportDimension <- BaseMultivalueReport <- ReportCampaignLotameOffline              | ReportTargetValueManager <- ReportDataProviderManager | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignAge               | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignCarrier           | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignCity              | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignCountry           | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignDomain            | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignGender            | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignMake              | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignModel             | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignOs                | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignPosition          | ReportTargetValueManager                              | dimension_id, related_id |
| BaseReportCampaign <- BaseReportTargetValueCampaign <- BaseReportDimension <- ReportCampaignRegion            | ReportTargetValueManager                              | dimension_id, related_id |
+---------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+--------------------------+
