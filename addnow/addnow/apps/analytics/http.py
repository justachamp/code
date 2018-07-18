import uuid
import urlparse

from googleapiclient.http import HttpRequest


USER_PARAM = 'quotaUser'


class AddnowHttpRequest(HttpRequest):

    @property
    def uri(self):
        return self.__uri

    @uri.setter
    def uri(self, val):
        parsed = urlparse.urlparse(val)
        uid = str(uuid.uuid1())
        if parsed.query:
            if USER_PARAM in urlparse.parse_qs(parsed.query):
                self.__uri = val
            else:
                self.__uri = val + '&' + '%s=%s' % (USER_PARAM, uid)
        else:
            self.__uri = val + '?' + '%s=%s' % (USER_PARAM, uid)
