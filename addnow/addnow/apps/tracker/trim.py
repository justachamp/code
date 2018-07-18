import logging
from json import dumps

import requests
from requests.packages import urllib3

from django.conf import settings

from addnow.apps.tracker.exceptions import TrimAPIException, BadTrimKeyException, ValidationFailedException


urllib3.disable_warnings()
logger = logging.getLogger(__name__)


class TrimService(object):
    def __init__(self, trim_key=None):
        self.trim_key = trim_key or settings.TRIM_KEY

    def http_request(self, request_type, endpoint, data=None):
        """
        :param request_type: request method
        :param endpoint: path
        :param data: dict
        :return: response dict
        """
        data = dumps(data)
        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.trim_key
        }
        if (request_type != 'post') and (request_type != 'get'):
            message = 'Unsupported Trim request type %s' % request_type
            logger.exception(message)
            raise TrimAPIException(message)
        try:
            if request_type == 'post':
                response = requests.post(settings.TRIM_API + endpoint, data=data, headers=headers, verify=False).json()
            else:
                response = requests.get(settings.TRIM_API + endpoint, headers=headers, verify=False).json()
        except Exception as e:
            logger.exception('Trim API error, endpoint %s, data %s', endpoint, data)
            raise TrimAPIException('(%s) %s' % (e.__class__.__name__, e.message))

        if 'Forbidden' in response:
            raise BadTrimKeyException('Invalid TRIM API key.')
        return response

    def create_shortcut(self, long_url, site_id, tool, service=None, vanity_domain=None):
        """
        Request: trim.api/links
            Content-Type: application/json
            {"long_url": "http://google.com", "seed": "addnow_fb"}

        Response:
            {"keyword": "Az34w", "url": "http://tr.im/Az34w"}

        :return: tuple(keyword, url)
        """
        data = {'long_url': long_url}
        if service:
            data['seed'] = 'an_%s_%s_%s' % (site_id, tool, service)
        else:
            data['seed'] = 'an_%s_%s' % (site_id, tool)
        if vanity_domain:
            data['vanity_domain'] = vanity_domain

        response = self.http_request('post', 'links', data=data)
        try:
            return response['keyword'], response['url']
        except KeyError:
            message = "Couldn't return data from response %s" % repr(response)
            logger.exception(message)
            if 'Validation Failed' in repr(response):
                raise ValidationFailedException(repr(response))
            else:
                raise TrimAPIException(message)

    def create_hook(self, short_url, hook):
        """
        Request: trim.api/links/{short_url}/hooks
        Content-Type: application/json
        hook    string  URL which should be called

        Response:
            {"id": "3"}

        :return: id
        """
        response = self.http_request('post', 'links/%s/hooks' % short_url, data={'hook': hook})
        hook_id = response.get('id')
        if hook_id:
            logger.debug('Hook(%s) for short_url(%s) was created. Id is: %s', hook, short_url, hook_id)
        else:
            logger.warning('Hook(%s) for short_url(%s) was not created. Response was: %s', hook, short_url, response)
        return hook_id

    def get_hooks_count(self, short_url):
        """
        Request: trim.api/links/{short_url}/hooks
            Content-Type: application/json
            hook	string	URL which should be called

        Response:
            {"hooks": [{...}, {...}]}

        :return: hooks count
        """
        response = self.http_request('get', 'links/%s/hooks' % short_url)
        if 'Forbidden' in response:
            raise BadTrimKeyException('Invalid TRIM API key.')
        try:
            return len(response['hooks'])
        except KeyError:
            message = "Couldn't return data from response %s" % repr(response)
            logger.exception(message)
            raise TrimAPIException(message)

    def get_vanity_domains(self):
        """
        Request: trim.api/vanity_domains/list
            Content-Type: application/json


        Response:
            {"vanity_domains_count": 3, "vanity_domains": ["...", "...", "..."]}

        :return: domains list
        """
        response = self.http_request('post', 'vanity-domains/list', data={})
        if 'Forbidden' in response:
            raise BadTrimKeyException('Invalid TRIM API key.')
        try:
            return response['vanity_domains']
        except KeyError:
            message = "Couldn't return data from response %s" % repr(response)
            logger.exception(message)
            raise TrimAPIException(message)
