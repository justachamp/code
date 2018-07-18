from django.core.management import call_command
from django.test.testcases import TestCase

from addnow.apps.tracker.models.base import pydb


class MongoTestCase(TestCase):
    @classmethod
    def drop_collections(cls):
        for collection in pydb.collection_names(include_system_collections=False):
            pydb[collection].drop()

    @classmethod
    def create_indexes(cls):
        call_command('indexes', create=True, verbosity=0)

    @classmethod
    def setUpClass(cls):
        super(MongoTestCase, cls).setUpClass()
        cls.create_indexes()

    def tearDown(self):
        super(MongoTestCase, self).tearDown()
        self.drop_collections()
        self.create_indexes()
