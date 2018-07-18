# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial
from multiprocessing import Pool, cpu_count
from optparse import make_option

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

from pymongo import MongoClient
from schematics.exceptions import ModelValidationError
from tqdm import tqdm

from addnow.apps.tracker.models.collections import OutsideShares
from addnow.apps.tracker.models.dimensions import Keyword
from addnow.apps.tracker.models.reports import ALL_DIMENSIONS


HOUR_EVENTS = ['share', 'click', 'view', 'follow', 'copy']

COLLECTIONS = [
    (['browser'], 'event_browser_day', 'day', ''),
    (['country'], 'event_country_day', 'day', ''),
    (['domain'], 'event_domain_day', 'day', ''),
    (['domain_url'], 'event_domain_url_day', 'day', ''),
    (['keyword'], 'event_keywords_day', 'day', ''),
    (['search'], 'event_search_day', 'day', ''),
    (['source'], 'event_source_day', 'day', ''),
    (['tool'], 'event_tool_day', 'day', ''),
    (['url'], 'event_url_day', 'day', ''),
    (['url_country'], 'event_url_country_day', 'day', ''),
    (['url_source'], 'event_url_source_day', 'day', ''),
    (HOUR_EVENTS, 'event_hour', 'hour', 'daily_'),
    (None, 'event_url_source_all', None, None),
]

OLD_COLLECTIONS = (
    'event_hour',
    'event_day', 'event_month', 'event_year', 'event_all',
    'event_browser_day', 'event_browser_month', 'event_browser_year', 'event_browser_all',
    'event_country_day', 'event_country_month', 'event_country_year', 'event_country_all',
    'event_domain_day', 'event_domain_month', 'event_domain_year', 'event_domain_all',
    'event_domain_url_day', 'event_domain_url_month', 'event_domain_url_year', 'event_domain_url_all',
    'event_keywords_day', 'event_keywords_month', 'event_keywords_year', 'event_keywords_all',
    'event_search_day', 'event_search_month', 'event_search_year', 'event_search_all',
    'event_source_day', 'event_source_month', 'event_source_year', 'event_source_all',
    'event_tool_day', 'event_tool_month', 'event_tool_year', 'event_tool_all',
    'event_url_day', 'event_url_month', 'event_url_year', 'event_url_all',
    'event_url_country_day', 'event_url_country_month', 'event_url_country_year', 'event_url_country_all',
    'event_url_source_day', 'event_url_source_month', 'event_url_source_year', 'event_url_source_all',
)

pydb = None


def do_job(doc, item):
    Command().process_doc(doc, item)


class Command(BaseCommand):
    help = 'Migrate MongoDB data'

    option_list = BaseCommand.option_list + (
        make_option(
            '-w', '--write-concern',
            help='Write concern. Write operations will block until they have been replicated to the specified number '
                 'or tagged set of servers. w=0 disables acknowledgement of write operations',
            type='int',
            default=None
        ),
        make_option(
            '-j', '--journal',
            help='If True, block until write operations have been committed to the journal',
            action='store_true',
            default=None
        ),
        make_option(
            '-p', '--processes',
            help='Processes number used for migration. Default equal to cpu count * 2',
            type='int',
            default=cpu_count() * 2
        ),
        make_option(
            '-c', '--chunk-size',
            help='Chunk size for every process used for migration. Default equal to 100',
            type='int',
            default=100
        ),
        make_option(
            '-d', '--drop',
            help='Drop old data',
            action='store_true',
            default=False
        ),
    )

    def print_error(self, doc, err):
        self.stderr.write('ERROR:')
        self.stderr.write('Message: %s' % err)
        self.stderr.write('MongoDB document: %s' % doc)
        self.stderr.write('-' * 50)

    def mark_as_migrated(self, old_doc, collection):
        old_doc['migrated'] = True
        collection.save(old_doc)

    def save_data(self, dimension_class, data, event_prefix=''):
        for event in dimension_class.get_events():
            value = data.get('%s%s' % (event_prefix, event))
            if value:
                self.save_event(dimension_class, event, data, value)

    def save_event(self, dimension_class, event, data, value):
        try:
            dimension_class().inc(event, value=value, **data)
        except ModelValidationError as err:
            self.print_error(data, err)

    def process_doc(self, doc, item):
        if doc.get('migrated'):
            return

        dimension_names, collection_name, time_section, event_prefix = item
        collection = pydb[collection_name]
        data = doc.copy()

        # recalculate checksum
        if 'checksum' in data:
            del data['checksum']

        # migrate outside_shares
        if collection_name == 'event_url_source_all':
            outside_shares = data.get('outside_shares')
            if outside_shares:
                try:
                    OutsideShares().set_counter(site=data['site'], url=data['url'], source=data['source'],
                                                value=outside_shares)
                except (KeyError, ModelValidationError) as err:
                    self.print_error(data, err)
                    return
        else:
            for dimension_name in dimension_names:
                dimension_class = ALL_DIMENSIONS[dimension_name]
                try:
                    data['date'] = doc[time_section]
                except KeyError as err:
                    self.print_error(data, err)
                    continue

                # Remove null sources
                if dimension_name in ('source', 'url_source') and data.get('source') is None:
                    continue

                # Remove outside shares from events
                if dimension_name in ('source', 'url', 'url_source'):
                    if 'outside_shares' in data:
                        del data['outside_shares']

                if dimension_class == Keyword:
                    copied_keywords = data.get('copied_keywords')
                    if copied_keywords:
                        for keyword, count in copied_keywords.items():
                            # replace mongodb reserved characters
                            keyword = keyword.replace('\uff0e', '.').replace('\uff04', '$')
                            data['copied_keywords'] = [keyword]
                            self.save_event(dimension_class, dimension_class.get_events()[0], data, value=count)
                else:
                    self.save_data(dimension_class, data, event_prefix=event_prefix)
        self.mark_as_migrated(doc, collection)

    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 1))
        write_concern = options['write_concern']
        journal = options['journal']
        drop_old_data = options['drop']

        write_concern_options = {}
        if write_concern is not None:
            write_concern_options['w'] = write_concern
        if journal is not None:
            write_concern_options['j'] = journal
        processes = options['processes']
        chunk_size = options['chunk_size']

        mongodb_client = MongoClient(settings.MONGODB_URI, **write_concern_options)
        global pydb
        pydb = mongodb_client[settings.MONGODB_NAME]

        try:
            pydb.authenticate(settings.MONGODB_USERNAME, settings.MONGODB_PASSWORD)
        except AttributeError:
            pass

        call_command('indexes', create=True, verbosity=verbosity)

        # sort collections by number of documents in collections
        collections = sorted(COLLECTIONS, key=lambda i: pydb[i[1]].count())

        pool = Pool(processes=processes)

        for item in collections:
            _, collection_name, _, _ = item
            collection = pydb[collection_name]
            total_docs = collection.count()

            if verbosity >= 1:
                self.stdout.write("Importing '%s' (%d documents) ..." % (
                    collection_name, total_docs
                ))

            if total_docs == 0:
                continue

            cursor = collection.find(no_cursor_timeout=True)
            it = pool.imap_unordered(partial(do_job, item=item), cursor, chunksize=chunk_size)
            for _ in tqdm(it, total=total_docs):
                pass

        pool.close()
        pool.join()

        if drop_old_data:
            if verbosity >= 1:
                self.stdout.write('Dropping old collections...')
            for collection_name in OLD_COLLECTIONS:
                if verbosity >= 1:
                    self.stdout.write(collection_name)
                collection = pydb[collection_name]
                collection.drop()

        if verbosity >= 1:
            self.stdout.write('Done.')
