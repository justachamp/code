from django.conf import settings

from nltk.downloader import Downloader


def install_nltk(download_dir=None):
    """ Download specific collection identifiers """
    if not download_dir:
        download_dir = settings.NLTK_DATA_PATH
    downloader = Downloader(download_dir=download_dir)
    downloader.download('punkt')
    downloader.download('maxent_treebank_pos_tagger')
