# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from functools import partial
from multiprocessing import Pool

import nltk
from many_stop_words import get_stop_words
from tqdm import tqdm

from django.conf import settings

from addnow.apps.tracker.models.base import pydb
from addnow.apps.tracker.models.stats.keyword import KeywordAll, KeywordDaily, KeywordMonthly, KeywordYearly
from addnow.apps.tracker.utils import _is_domain_name, _replace_punct, URL_REGEX, SYMBOLS


stop_words = get_stop_words('en')
stop_words = {word.decode('utf-8') for word in stop_words}
stop_words |= {'read'}

ALLOWED_TAGS = ('NN', 'NNS', 'NNP', 'NNPS')

models = [KeywordAll, KeywordDaily, KeywordMonthly, KeywordYearly]


if settings.NLTK_DATA_PATH not in nltk.data.path:
    nltk.data.path.append(settings.NLTK_DATA_PATH)


def get_urls(s):
    matched = URL_REGEX.findall(s)
    return [groups[0] for groups in matched]


def strip_dots(keyword):
    old_keyword = keyword
    while 1:
        new_keyword = keyword.strip('.')
        if new_keyword == keyword:
            break
        keyword = new_keyword
    # dot in the center of word, return keyword + '.'
    if '.' in keyword and old_keyword != keyword:
        keyword += '.'
    return keyword


def create_indexes():
    print 'Creating indexes ...'
    print 'stats.all'
    pydb['stats.all'].create_index([('type', 1)], background=True)
    print 'stats.daily'
    pydb['stats.daily'].create_index([('type', 1)], background=True)
    print 'stats.monthly'
    pydb['stats.monthly'].create_index([('type', 1)], background=True)
    print 'stats.yearly'
    pydb['stats.yearly'].create_index([('type', 1)], background=True)


def remove_keyword(doc, collection_name):
    pydb[collection_name].delete_one({'_id': doc['_id']})


def replace_keyword(doc, collection_name, new_keyword):
    doc['keyword'] = new_keyword
    pydb[collection_name].replace_one({'_id': doc['_id']}, doc)


def process_doc(doc, collection_name):
    result = {'remove': False, 'replace': False, 'keyword': doc['keyword']}
    disallowed_strings = ['http', 'ftp', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] + SYMBOLS

    old_keyword = doc['keyword']
    old_amount = len(old_keyword.split(' '))
    keyword = _replace_punct(old_keyword)
    keywords = keyword.split(' ')
    keywords = [k.strip(',').strip("'") for k in keywords]
    keywords = [strip_dots(k) for k in keywords]
    keywords = [k for k in keywords if k != '']
    if len(keywords) != old_amount:
        remove_keyword(doc, collection_name)
        result['remove'] = True
        return result
    for i, keyword in enumerate(keywords):
        tokens = nltk.word_tokenize(keyword)
        if len(tokens) != 1 and tokens[1] != '.':
            tagged_tokens = nltk.pos_tag(tokens)
            filtered_words = [word for word, tag in tagged_tokens if tag in ALLOWED_TAGS]
            if len(filtered_words) != 1:
                remove_keyword(doc, collection_name)
                result['remove'] = True
                return result
            keywords[i] = filtered_words[0]
    tagged_tokens = nltk.pos_tag(keywords)
    for word, tag in tagged_tokens:
        if tag == 'CD' or len(word) <= 2 or word in stop_words or get_urls(word) or _is_domain_name(word) \
                or any(s in word for s in disallowed_strings):
            remove_keyword(doc, collection_name)
            result['remove'] = True
            return result
    new_keyword = ' '.join(keywords)
    if new_keyword != old_keyword:
        replace_keyword(doc, collection_name, new_keyword)
        result['replace'] = True
        result['replace_to'] = new_keyword
    return result


def remove_keywords():
    pool = Pool(processes=2)

    with open('removed_keywords.txt', 'w') as f_removed, open('replaced_keywords.txt', 'w') as f_replaced:
        for model in models:
            model_instance = model()
            total_docs = model_instance.find().count()
            total_removed = 0
            total_replaced = 0
            print "Removing keywords from collection '%s' (%d documents) ..." % (
                model_instance.collection_name, total_docs
            )
            cursor = model_instance.find(no_cursor_timeout=True)
            it = pool.imap_unordered(partial(process_doc, collection_name=model_instance.collection_name),
                                     cursor, chunksize=100)
            for result in tqdm(it, total=total_docs, leave=True):
                keyword = result['keyword']
                if result['remove']:
                    print >> f_removed, keyword.encode('utf-8')
                    total_removed += 1
                if result['replace']:
                    new_keyword = result['replace_to']
                    print >> f_replaced, 'Old:', keyword.encode('utf-8')
                    print >> f_replaced, 'New:', new_keyword.encode('utf-8')
                    total_replaced += 1
            print ''
            print 'Total removed %d keywords.' % total_removed
            print 'Total replaced %d keywords.' % total_replaced

    pool.close()
    pool.join()


if __name__ == '__main__':
    create_indexes()
    remove_keywords()
