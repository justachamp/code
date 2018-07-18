# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
sys.path += ['/vagrant']

from addnow.apps.tracker.models.base import pydb


def create_index():
    print 'Creating index for outside_shares ...'
    pydb['outside_shares'].create_index([('source', 1)], background=True)


def drop_index():
    print 'Dropping index for outside_shares ...'
    pydb['outside_shares'].drop_index([('source', 1)])


def remove_twitter_counters():
    result = pydb['outside_shares'].delete_many({'source': 'twitter'})
    print 'Deleted %d documents' % result.deleted_count


if __name__ == '__main__':
    create_index()
    remove_twitter_counters()
    drop_index()
