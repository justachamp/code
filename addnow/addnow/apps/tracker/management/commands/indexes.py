# -*- coding: utf-8 -*-
"""
    Keep in mind:
    * max 1024 bytes index entry total size (including BSON structure),
    * max 64 indexes per collection,
    * max 31 compound indexes per collection.
"""

from __future__ import unicode_literals

from collections import OrderedDict
from optparse import make_option

from django.core.management.base import BaseCommand

from addnow.apps.tracker.models.reports import ALL_DIMENSIONS
from addnow.apps.tracker.models.collections import OutsideShares, UpdateCounters, GeoIPModel


class Command(BaseCommand):
    help = 'Create or drop MongoDB indexes for models'

    option_list = BaseCommand.option_list + (
        make_option(
            '-s', '--show',
            help='Shows indexes',
            action='store_true',
            default=True
        ),
        make_option(
            '-c', '--create',
            help='Creates indexes',
            action='store_true',
            default=False
        ),
        make_option(
            '-d', '--drop',
            help='Drops indexes',
            action='store_true',
            default=False
        ),
    )

    def print_indexes(self, model_instance):
        if model_instance.use_indexes and model_instance.indexes:
            for index in model_instance.indexes:
                self.stdout.write('%s %s' % (
                    index['index'],
                    index.get('args', {})
                ))

    def handle(self, *args, **options):
        verbosity = int(options.get('verbosity', 1))
        show_indexes = options['show']
        create_indexes = options['create']
        drop_indexes = options['drop']

        model_list = []
        collection_models = {}
        for dimension in ALL_DIMENSIONS.values():
            for model in dimension.models:
                model_list.append(model)
        model_list += [OutsideShares, UpdateCounters, GeoIPModel]
        for model in model_list:
            collection_models.setdefault(model.collection_name, []).append(model)
        collection_models = OrderedDict(sorted(collection_models.items()))

        if verbosity >= 1:
            if create_indexes:
                self.stdout.write('Creating indexes...')
            elif drop_indexes:
                self.stdout.write('Dropping indexes...')
        for collection_name, models in collection_models.items():
            if verbosity >= 1 and show_indexes:
                self.stdout.write('collection %s:' % collection_name)
            for model in models:
                model_instance = model()
                self.print_indexes(model_instance)
                if create_indexes:
                    model_instance.create_indexes()
                elif drop_indexes:
                    model_instance.drop_indexes()
        if verbosity >= 1 and (create_indexes or drop_indexes):
            self.stdout.write('Done.')
