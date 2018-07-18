# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import base64
import hashlib
import re
from urlparse import urlparse
from uuid import uuid1

from django.conf import settings
from django.contrib.gis.geoip import GeoIP
from django.core.exceptions import ValidationError

import nltk
from nltk.util import bigrams, trigrams
from many_stop_words import get_stop_words

from addnow.apps.accounts.validators import DomainNameValidator
from addnow.cache import GeoIpCache


URL_REGEX = re.compile(
    r'(?i)\b('
    r'(?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)'
    r'(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+'
    r'(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'
)

EMAIL_REGEX = re.compile(r'[\w\.-]+@[\w\.-]+')

SYMBOLS = ['~', '№', '^', '*', '=', '/', '\\', '|']

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if settings.NLTK_DATA_PATH not in nltk.data.path:
    nltk.data.path.append(settings.NLTK_DATA_PATH)


def create_uuid():
    return base64.b64encode(uuid1().bytes).rstrip('=')


def get_checksum(s):
    if isinstance(s, unicode):
        s = s.encode('utf-8')
    return hashlib.sha1(s).hexdigest()


def decode_uuid(uuid):
    uuid_length = len(uuid)
    uuid_padding = 4 - uuid_length % 4
    uuid = uuid.ljust(uuid_length + uuid_padding, '=')
    return base64.b64decode(uuid).decode('latin1')


def strip_scheme(url):
    """
    Strips scheme from url.
    """
    parsed = urlparse(url)
    scheme = '%s://' % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)


def get_geoip_data(ip):
    data = GeoIpCache.get(dict(ip=ip))
    if not data:
        data = GeoIP().city(ip)
        if data:
            keys = ('city', 'country_code', 'country_name', 'latitude', 'longitude')
            data = {k: data[k] for k in keys}
        GeoIpCache.set(dict(ip=ip), data, timeout=0)
    return data


def _remove_by_regex(s):
    s = URL_REGEX.sub('', s)
    s = EMAIL_REGEX.sub('', s)
    return s


def _is_domain_name(s):
    try:
        DomainNameValidator()(s)
    except ValidationError:
        return False
    return True


def _replace_punct(sentence):
    punct_to_remove = '"″“”¨<>‹›«»'
    symbols_to_strip = ''.join(SYMBOLS) + '-'
    quotes = ['′', '‘', '’', 'ʻ', 'ʼ', '´', '`', 'ˈ']
    replace_map = {
        ord('‚'): ',',
        ord('．'): '.',
        ord('։'): ':',
        ord('—'): '-',
        ord('–'): '-',
        ord('…'): ' '
    }
    for quote in quotes:
        replace_map[ord(quote)] = "'"
    if not isinstance(sentence, unicode):
        sentence = sentence.decode('utf-8')
    sentence = re.sub(r'[%s]' % punct_to_remove, '', sentence)
    sentence = re.sub(r'(^[%s]+)|([%s]+$)' % (symbols_to_strip, symbols_to_strip), '', sentence)
    sentence = sentence.translate(replace_map)
    return sentence


def is_proper_keyword(keyword, tag, allowed_tags, stop_words):
    disallowed_strings = ['http', 'ftp', '_'] + DIGITS + SYMBOLS

    return tag in allowed_tags and len(keyword) > 2 and not (
        keyword in stop_words or
        _is_domain_name(keyword) or
        any(s in keyword for s in disallowed_strings)
    )


def get_keywords(sentence, allowed_tags):
    sentence = _remove_by_regex(_replace_punct(sentence))
    tokens = nltk.word_tokenize(sentence)
    tokens = [token.strip("'") for token in tokens]
    tagged_tokens = nltk.pos_tag(tokens)
    stop_words = get_stop_words('en')
    stop_words = {word.decode('utf-8') for word in stop_words}
    stop_words |= {'read'}
    keywords = []
    for word, tag in tagged_tokens:
        word = word.lower()
        if is_proper_keyword(word, tag, allowed_tags, stop_words):
            keywords.append(word)
    bigrams_keywords = list(bigrams(keywords))
    trigrams_keywords = list(trigrams(keywords))

    for k in bigrams_keywords:
        keywords.append(' '.join(k))

    for k in trigrams_keywords:
        keywords.append(' '.join(k))
    return keywords
