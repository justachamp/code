import urllib

from addnow.apps.accounts import constants


class Service(object):
    should_short_url = True

    def __str__(self):
        return self.__class__.__name__

    def get_redirect_url(self, *args, **kwargs):
        raise NotImplementedError('Should be implemented in child class')


class GmailService(Service):
    url = 'https://mail.google.com/mail/u/0/'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'view': 'cm',
            'fs': 1,
            'su': kwargs.get('title'),  # Email Subject
            'body': kwargs.get('url'),  # Email Body
            'tf': 1
        })
        return '%s?%s' % (self.url, params)


class GooglePlusService(Service):
    url = 'https://plus.google.com/share'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'hl': 'en-US',
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class FacebookService(Service):
    url = 'http://www.facebook.com/sharer/sharer.php'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            't': kwargs.get('title'),
            'u': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class TwitterService(Service):
    url = 'https://twitter.com/intent/tweet'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'text': kwargs.get('title'),
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class DiggService(Service):
    url = 'http://digg.com/submit'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class DeliciousService(Service):
    url = 'http://www.delicious.com/save'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'v': 5,
            'noui': '',
            'jump': 'close',
            'url': kwargs.get('url'),
            'title': kwargs.get('title')
        })
        return '%s?%s' % (self.url, params)


class StumbleuponService(Service):
    url = 'http://www.stumbleupon.com/badge/'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class LinkedinService(Service):
    url = 'https://www.linkedin.com/cws/share'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'token': '',
            'isFramed': 'true',
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class PinterestService(Service):
    url = 'http://pinterest.com/pin/create/button/'
    should_short_url = False

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'media': kwargs.get('media_url'),
            'description': kwargs.get('title'),
            'url': kwargs.get('url')
        })
        return '%s?%s' % (self.url, params)


class WhatsappService(Service):
    url = 'whatsapp://send'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'text': kwargs.get('title', '') + ': ' + kwargs.get('url', '')
        })
        return '%s?%s' % (self.url, params)


class LineService(Service):
    url = 'https://line.me/R/msg/text/'

    def get_redirect_url(self, *args, **kwargs):
        return "%s?%s" % (self.url, kwargs.get('title', ''))


class TumblrService(Service):
    url = 'http://www.tumblr.com/share/link'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'url': kwargs.get('url'),
            'name': kwargs.get('title'),
            'description': kwargs.get('title')
        })
        return '%s?%s' % (self.url, params)


class RedditService(Service):
    url = 'http://www.reddit.com/submit'
    should_short_url = False

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'resubmit': 'true',
            'url': kwargs.get('url'),
            'title': kwargs.get('title')
        })
        return '%s?%s' % (self.url, params)


class WeiboService(Service):
    url = 'http://service.t.sina.com.cn/share/share.php'

    def get_redirect_url(self, *args, **kwargs):
        params = urllib.urlencode({
            'url': kwargs.get('url'),
            'title': kwargs.get('title')
        })
        return "%s?%s" % (self.url, params)


class ServiceFactory():
    service_objects = {
        constants.SOCIAL_SERVICE_GMAIL: GmailService,
        constants.SOCIAL_SERVICE_GOOGLE_PLUS: GooglePlusService,
        constants.SOCIAL_SERVICE_FACEBOOK: FacebookService,
        constants.SOCIAL_SERVICE_TWITTER: TwitterService,
        constants.SOCIAL_SERVICE_DIGG: DiggService,
        constants.SOCIAL_SERVICE_DELICIOUS: DeliciousService,
        constants.SOCIAL_SERVICE_STUMBLEUPON: StumbleuponService,
        constants.SOCIAL_SERVICE_LINKEDIN: LinkedinService,
        constants.SOCIAL_SERVICE_PINTEREST: PinterestService,
        constants.SOCIAL_SERVICE_WHATSAPP: WhatsappService,
        constants.SOCIAL_SERVICE_TUMBLR: TumblrService,
        constants.SOCIAL_SERVICE_REDDIT: RedditService,
        constants.SOCIAL_SERVICE_WEIBO: WeiboService,
        constants.SOCIAL_SERVICE_LINE: LineService,
        constants.SOCIAL_SERVICE_INSTAGRAM: Service
    }

    def get_service(self, service):
        return self.service_objects[service]()
