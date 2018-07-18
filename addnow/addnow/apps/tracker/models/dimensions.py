from addnow.apps.tracker.models.stats import (
    browser, click, copy, country, domain,
    domain_url, follow, keyword, search, share,
    source, tool, url, url_country, url_source, view
)


class BaseDimension(object):
    name = None
    models = ()

    def inc(self, event, value=1, **kwargs):
        for m in self.models:
            m().inc_counter(event, value, **kwargs)
        return len(self.models)

    @classmethod
    def get_events(cls):
        if not cls.models:
            return []
        return cls.models[0].get_events()

    @classmethod
    def get_data_fields(cls):
        if not cls.models:
            return []
        return cls.models[0].data_fields


class Browser(BaseDimension):
    name = 'browser'
    models = (
        browser.BrowserAll,
        browser.BrowserDaily,
        browser.BrowserMonthly,
        browser.BrowserYearly
    )


class Copy(BaseDimension):
    name = 'copy'
    models = (
        copy.CopyAll,
        copy.CopyDaily,
        copy.CopyMonthly,
        copy.CopyYearly
    )


class Click(BaseDimension):
    name = 'click'
    models = (
        click.ClickAll,
        click.ClickDaily,
        click.ClickMonthly,
        click.ClickYearly
    )


class Country(BaseDimension):
    name = 'country'
    models = (
        country.CountryAll,
        country.CountryDaily,
        country.CountryMonthly,
        country.CountryYearly
    )


class Domain(BaseDimension):
    name = 'domain'
    models = (
        domain.DomainAll,
        domain.DomainDaily,
        domain.DomainMonthly,
        domain.DomainYearly
    )


class DomainUrl(BaseDimension):
    name = 'domain_url'
    models = (
        domain_url.DomainUrlAll,
        domain_url.DomainUrlDaily,
        domain_url.DomainUrlMonthly,
        domain_url.DomainUrlYearly
    )


class Follow(BaseDimension):
    name = 'follow'
    models = (
        follow.FollowAll,
        follow.FollowDaily,
        follow.FollowMonthly,
        follow.FollowYearly
    )


class Keyword(BaseDimension):
    name = 'keyword'
    models = (
        keyword.KeywordAll,
        keyword.KeywordDaily,
        keyword.KeywordMonthly,
        keyword.KeywordYearly
    )

    def inc(self, event, value=1, **kwargs):
        copied_keywords = kwargs['copied_keywords']
        ret = 0
        for copied_keyword in copied_keywords:
            kwargs['keyword'] = copied_keyword
            ret += super(Keyword, self).inc(event, value, **kwargs)
        return ret


class Search(BaseDimension):
    name = 'search'
    models = (
        search.SearchAll,
        search.SearchDaily,
        search.SearchMonthly,
        search.SearchYearly
    )


class Share(BaseDimension):
    name = 'share'
    models = (
        share.ShareAll,
        share.ShareDaily,
        share.ShareMonthly,
        share.ShareYearly
    )


class Source(BaseDimension):
    name = 'source'
    models = (
        source.SourceAll,
        source.SourceDaily,
        source.SourceMonthly,
        source.SourceYearly
    )


class Tool(BaseDimension):
    name = 'tool'
    models = (
        tool.ToolAll,
        tool.ToolDaily,
        tool.ToolMonthly,
        tool.ToolYearly
    )


class Url(BaseDimension):
    name = 'url'
    models = (
        url.UrlAll,
        url.UrlDaily,
        url.UrlMonthly,
        url.UrlYearly
    )


class UrlCountry(BaseDimension):
    name = 'url_country'
    models = (
        url_country.UrlCountryAll,
        url_country.UrlCountryDaily,
        url_country.UrlCountryMonthly,
        url_country.UrlCountryYearly
    )


class UrlSource(BaseDimension):
    name = 'url_source'
    models = (
        url_source.UrlSourceAll,
        url_source.UrlSourceDaily,
        url_source.UrlSourceMonthly,
        url_source.UrlSourceYearly
    )


class View(BaseDimension):
    name = 'view'
    models = (
        view.ViewAll,
        view.ViewDaily,
        view.ViewMonthly,
        view.ViewYearly
    )
