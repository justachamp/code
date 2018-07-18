import simplejson

from django.test.client import Client


class KanaryClient(Client):

    '''Extends django base client for our utility/shortcut methods'''

    def get_json(self, url):
        '''Tries to retrieve given url by given client and cast all data into
        json
        :param url: (string) url from which we'll retrieve data
        :return: retrieved json object'''

        response = self.get(url)
        assert response.status_code == 200
        return simplejson.loads(response.content)

    def post_json(self, url, data):
        '''Tries to post json data
        :param url: (string) url, to which data will be posted
        :param data: (dict) which must be json serializable
        :return: retrieved json object'''
        response = self.post(url, simplejson.dumps(data),
                             content_type='application/json')
        assert response.status_code == 201
        return simplejson.loads(response.content)
