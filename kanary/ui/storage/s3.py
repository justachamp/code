from boto import connect_s3
from django.conf import settings

from etc.constants import CDN_RESOURCE_KEY_MASK


def _get_bucket():
    '''
    Shortcut function for connecting with amazon and returning default bucket
    '''
    cloud = connect_s3(settings.AMAZON_ACCESS_KEY, settings.AMAZON_SECRET_KEY)
    return cloud.get_bucket(settings.AMAZON_BUCKET)


def upload_file_to_cdn(content, content_type, public_id):
    """
    :param string content: content to upload
    :param string content_type: content type
    :param int public_id: public id of creative instance
    """
    bucket = _get_bucket()
    key_path = CDN_RESOURCE_KEY_MASK % dict(cid=public_id)
    key = bucket.new_key(key_path)
    key.content_type = content_type
    key.set_contents_from_string(content)
    key.set_acl('public-read')
    return public_id
