from ajaxuploader.views import AjaxFileUploader

from django.conf import settings
from ui.storage.upload_backend import CustomUploadBackend


# uploading temporary images for Creative
upload_creative_image = AjaxFileUploader(
    backend=CustomUploadBackend,
    UPLOAD_DIR=settings.CREATIVES_UPLOAD_DIR,
)
