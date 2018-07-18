from urllib import urlencode
from urlparse import parse_qs, urlparse, urlunparse

from tqdm import tqdm

from addnow.apps.tracker.models.base import pydb
from addnow.apps.tracker.models.dimensions import DomainUrl, Url, UrlSource, UrlCountry
from addnow.apps.tracker.utils import get_checksum


dimensions = [DomainUrl, Url, UrlSource, UrlCountry]

total_replaced_docs = 0
replaced_docs = {}
sites = set()


for d in dimensions:
    replaced_docs[d.name] = {}
    for model in d.models:
        replaced_docs[d.name][model.collection_name] = 0


def to_remove(param):
    tracking_params = ['spmailingid', 'spuserid', 'spjobid', 'spreportid', 'subid']
    return param.startswith('utm') or param.lower() in tracking_params


def remove_special_params(url):
    parsed = urlparse(url.encode('utf-8'))
    query_dict = parse_qs(parsed.query, keep_blank_values=True)
    filtered_query_dict = dict((k, v) for k, v in query_dict.iteritems() if not to_remove(k))
    if filtered_query_dict == query_dict:
        return url.split('#')[0]
    new_url = urlunparse([
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        urlencode(filtered_query_dict, doseq=True),
        ''
    ])
    return new_url.decode('utf-8')


def create_indexes():
    print ''
    print '================================================================'
    print 'Creating indexes...'
    print '================================================================'
    print 'stats.all'
    pydb['stats.all'].create_index([('type', 1)], background=True)
    pydb['stats.all'].create_index([('replaced', 1)], background=True)
    pydb['stats.all'].create_index([('to_remove', 1)], background=True)
    print 'stats.daily'
    pydb['stats.daily'].create_index([('type', 1)], background=True)
    pydb['stats.daily'].create_index([('replaced', 1)], background=True)
    pydb['stats.daily'].create_index([('to_remove', 1)], background=True)
    print 'stats.monthly'
    pydb['stats.monthly'].create_index([('type', 1)], background=True)
    pydb['stats.monthly'].create_index([('replaced', 1)], background=True)
    pydb['stats.monthly'].create_index([('to_remove', 1)], background=True)
    print 'stats.yearly'
    pydb['stats.yearly'].create_index([('type', 1)], background=True)
    pydb['stats.yearly'].create_index([('replaced', 1)], background=True)
    pydb['stats.yearly'].create_index([('to_remove', 1)], background=True)


def replace_urls():
    print ''
    print '================================================================'
    print 'Replacing urls...'
    print '================================================================'

    global sites
    for i in range(4):
        for dimension in dimensions:
            model_instance = dimension.models[i]()
            process_collection(model_instance, dimension)
            print ''

    sites = sorted(sites)
    sites = {str(site) for site in sites}


def process_collection(model_instance, dimension):
    global total_replaced_docs

    cursor = model_instance.find(no_cursor_timeout=True)
    description = 'replacing urls: %s, %s' % (model_instance.collection_name, dimension.name)

    for doc in tqdm(cursor, desc=description, total=cursor.count(), leave=True):
        replaced, site = replace_doc(doc, model_instance.collection_name)
        if replaced:
            replaced_docs[dimension.name][model_instance.collection_name] += 1
            total_replaced_docs += 1
            sites.add(site)


def replace_doc(doc, collection_name):
    replaced = False
    site = None

    url = doc['url']
    new_url = remove_special_params(url)
    if new_url != url:
        replaced = True
        site = doc['site']
        new_checksum = get_checksum(new_url)
        doc['url'] = new_url
        doc['checksum'] = new_checksum
        doc['replaced'] = True
        pydb[collection_name].save(doc)
    return replaced, site


def merge_counters():
    print ''
    print '================================================================'
    print 'Merging counters...'
    print '================================================================'

    for i in range(4):
        for dimension in dimensions:
            model_instance = dimension.models[i]()
            merge_counters_in_collection(model_instance, dimension)
            print ''


def merge_counters_in_collection(model_instance, dimension):
    cursor = model_instance.find({'replaced': True}, no_cursor_timeout=True)
    description = 'merging counters: %s, %s' % (model_instance.collection_name, dimension.name)

    for doc in tqdm(cursor, desc=description, total=cursor.count(), leave=True):
        query = doc.copy()
        del query['_id']
        del query['replaced']
        del query['totals']
        if 'values' in query:
            del query['values']

        docs_to_merge = list(model_instance.find(query))
        new_doc = docs_to_merge[0]
        # skip already processed docs
        if any('to_remove' in doc for doc in docs_to_merge):
            continue
        if 'replaced' in new_doc:
            del new_doc['replaced']
        del new_doc['_id']

        for doc in docs_to_merge[1:]:
            for event, value in doc['totals'].items():
                new_doc['totals'][event] += value
            if 'values' in doc:
                for i, values in enumerate(doc['values']):
                    for event, value in values.items():
                        if event != model_instance.granularity_name:
                            new_doc['values'][i][event] += value

        model_instance.collection.update_many(query, {'$set': {'to_remove': True}, '$unset': {'replaced': ''}})
        model_instance.collection.save(new_doc)


def remove_docs():
    print ''
    print '================================================================'
    print 'Removing old counters...'
    print '================================================================'
    print 'stats.all'
    pydb['stats.all'].delete_many({'to_remove': True})
    pydb['stats.all'].drop_index([('to_remove', 1)])
    pydb['stats.all'].drop_index([('replaced', 1)])
    print 'stats.daily'
    pydb['stats.daily'].delete_many({'to_remove': True})
    pydb['stats.daily'].drop_index([('to_remove', 1)])
    pydb['stats.daily'].drop_index([('replaced', 1)])
    print 'stats.monthly'
    pydb['stats.monthly'].delete_many({'to_remove': True})
    pydb['stats.monthly'].drop_index([('to_remove', 1)])
    pydb['stats.monthly'].drop_index([('replaced', 1)])
    print 'stats.yearly'
    pydb['stats.yearly'].delete_many({'to_remove': True})
    pydb['stats.yearly'].drop_index([('to_remove', 1)])
    pydb['stats.yearly'].drop_index([('replaced', 1)])


if __name__ == '__main__':
    create_indexes()
    replace_urls()
    print ''
    print 'Replaced %d documents for sites: %s' % (total_replaced_docs, ', '.join(sites))
    print replaced_docs
    merge_counters()
    remove_docs()
