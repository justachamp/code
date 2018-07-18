from pymongo import MongoClient
from schematics.models import Model

from django.conf import settings


mongodb_client = MongoClient(settings.MONGODB_URI)
pydb = mongodb_client[settings.MONGODB_NAME]

try:
    pydb.authenticate(settings.MONGODB_USERNAME, settings.MONGODB_PASSWORD)
except AttributeError:
    pass


class BaseModel(Model):
    collection_name = None
    indexes = []
    use_indexes = True

    def _replace_id(self, docs):
        for item in docs:
            _id = item['_id']
            if _id is None:
                continue
            item.update(_id)
            del item['_id']
        return docs

    @property
    def collection(self):
        return pydb[self.collection_name]

    def find(self, query=None, *args, **kwargs):
        return self.collection.find(filter=query, *args, **kwargs)

    def find_one(self, query=None, *args, **kwargs):
        return self.collection.find_one(filter=query, *args, **kwargs)

    def save(self, validate=True, **kwargs):
        if validate:
            self.import_data(kwargs)
            self.validate()
        return self.collection.save(self.to_native())

    def inc(self, query, fields, validate=True, upsert=False, many=False):
        if validate:
            self.import_data(query)
            self.validate()
        if many:
            return self.collection.update_many(query, {'$inc': fields}, upsert=upsert)
        return self.collection.update_one(query, {'$inc': fields}, upsert=upsert)

    def set(self, query, fields, validate=True, upsert=False, many=False):
        if validate:
            self.import_data(query)
            self.validate()
        if many:
            return self.collection.update_many(query, {'$set': fields}, upsert=upsert)
        return self.collection.update_one(query, {'$set': fields}, upsert=upsert)

    def create_indexes(self):
        if self.use_indexes:
            for index in self.indexes:
                args = index.get('args', {})
                self.collection.create_index(index['index'], **args)

    def drop_indexes(self):
        self.collection.drop_indexes()
