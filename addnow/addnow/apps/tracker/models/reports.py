# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from addnow.apps.tracker.models.dimensions import (
    Browser, Click, Copy, Country, Domain,
    DomainUrl, Follow, Keyword, Search, Share,
    Source, Tool, Url, UrlCountry, UrlSource, View,
)


ALL_REPORTS = []
REPORT_TYPES = {}
ALL_DIMENSIONS = {}


class ReportMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        _class = super(ReportMetaClass, mcs).__new__(mcs, name, bases, attrs)
        if _class.dimensions:
            ALL_REPORTS.append(_class)
            for dimension in _class.dimensions:
                ALL_DIMENSIONS[dimension.name] = dimension
        if _class.event:
            REPORT_TYPES[_class.event] = _class
        if _class.event_singular:
            REPORT_TYPES[_class.event_singular] = _class
        return _class


class Report(object):
    __metaclass__ = ReportMetaClass

    dimensions = ()
    event = None
    event_singular = None

    @classmethod
    def inc(cls, value=1, **kwargs):
        """
        :param kwargs: site, url, title, country, source, browser, date
        :return: number of queries
        :rtype: int
        """
        return sum(d().inc(cls.event, value, **kwargs) for d in cls.dimensions)


class Shares(Report):
    event = 'shares'
    # TODO: fix
    event_singular = 'share'
    dimensions = (
        Share,
        Browser,
        Country,
        Source,
        Tool,
        Url,
        UrlCountry,
        UrlSource,
    )


class Clicks(Report):
    event = 'clicks'
    event_singular = 'click'
    dimensions = (
        Click,
        Browser,
        Country,
        Domain,
        DomainUrl,
        Search,
        Source,
        Tool,
        Url,
        UrlSource,
        UrlCountry,
    )


class Views(Report):
    event = 'views'
    event_singular = 'view'
    dimensions = (
        View,
        Browser,
        Country,
        Domain,
        DomainUrl,
        Url,
        UrlCountry,
    )


class Follows(Report):
    event = 'follows'
    event_singular = 'follow'
    dimensions = (
        Follow,
        Source,
    )


class Copies(Report):
    event = 'copies'
    event_singular = 'copy'
    dimensions = (
        Copy,
        Keyword,
    )
