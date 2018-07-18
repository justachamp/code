import os
import base64

from uuid import uuid4
from PIL import Image

import magic
import hexagonit.swfheader

from django.conf import settings

from ajaxuploader.backends.local import LocalUploadBackend


def random_filename():
    return base64.urlsafe_b64encode(uuid4().bytes).replace('=', '')


class CustomUploadBackend(LocalUploadBackend):

    def update_filename(self, request, filename):
        self.ext = os.path.splitext(filename)[1]
        return random_filename() + self.ext

    def upload_complete(self, request, filename, *args, **kwargs):
        '''
        Reads appropriate type creative would have for uploaded file.
        Adds found type to response dictionary
        '''
        response_dict = LocalUploadBackend.upload_complete(
            self, request, filename, *args, **kwargs)

        filepath = os.path.join(settings.CREATIVES_DIR, filename)

        if magic.from_file(filepath, mime=True).startswith('video'):
            response_dict['type'] = 'Video'
        else:
            try:
                response_dict['width'], response_dict['height'] =\
                    Image.open(filepath).size
                response_dict['type'] = 'Image'
            except IOError:
                try:
                    metadata = hexagonit.swfheader.parse(filepath)
                    response_dict['type'] = 'Flash'
                    response_dict['width'] = metadata['width']
                    response_dict['height'] = metadata['height']
                except ValueError:
                    response_dict['errors'] = 'Unknown file!'
                    response_dict['success'] = False

        return response_dict
