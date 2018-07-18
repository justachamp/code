# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory

from addnow.apps.tracker.tasks import ALLOWED_KEYWORD_TAGS
from addnow.apps.tracker.utils import get_keywords
from addnow.apps.tracker.views import get_hook


class TestUtils(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUtils, cls).setUpClass()
        cls.factory = RequestFactory()
        cls.create_shortlink_url = reverse('tracker_create_shortlink')

    def test__get_hook(self):
        request = self.factory.get(self.create_shortlink_url)
        hook = get_hook(request, 1234, 'test_tool', 'test_service', 'test_uuid', 'test_title')
        self.assertEqual(hook, 'http://testserver/click/1234/test_tool?uuid=test_uuid&service=test_service&'
                               'title=test_title')

    def test__get_hook_with_special_chars_in_title(self):
        request = self.factory.get(self.create_shortlink_url)
        hook = get_hook(request, 1234, 'test_tool', 'test_service', 'test_uuid', 'áãé’')
        self.assertEqual(hook, 'http://testserver/click/1234/test_tool?uuid=test_uuid&service=test_service&'
                               'title=%25C3%25A1%25C3%25A3%25C3%25A9%25E2%2580%2599')

    def test__get_keywords_returns_only_nouns(self):
        sentence = "I'm going to use addnow product. It provides great widgets to track social (and 'dark social') " \
                   "sharing of content. Thanks to all addnow team! You can contact me via email " \
                   "myemail@gmail.com and site http://mysite.com"
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [
            'addnow', 'product', 'widgets', 'content', 'addnow', 'team', 'email',
            'addnow product', 'product widgets', 'widgets content', 'content addnow', 'addnow team', 'team email',
            'addnow product widgets', 'product widgets content', 'widgets content addnow', 'content addnow team',
            'addnow team email'
        ])

    def test__get_keywords_with_unicode_punct(self):
        sentence = 'Schindler’s list is an American “epic” historical period drama film‚ directed and co—produced ' \
                   'by Steven Spielberg and scripted by Steven Zaillian． It is based on the novel Schindlerʼs ' \
                   'Ark by Thomas Keneally‚ an Australian novelist…'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [
            'schindler', 'list', 'period', 'drama', 'film', 'steven', 'spielberg', 'steven', 'zaillian', 'schindler',
            'ark', 'thomas', 'keneally', 'novelist', 'schindler list', 'list period', 'period drama', 'drama film',
            'film steven', 'steven spielberg', 'spielberg steven', 'steven zaillian', 'zaillian schindler',
            'schindler ark', 'ark thomas', 'thomas keneally', 'keneally novelist', 'schindler list period',
            'list period drama', 'period drama film', 'drama film steven', 'film steven spielberg',
            'steven spielberg steven', 'spielberg steven zaillian', 'steven zaillian schindler',
            'zaillian schindler ark', 'schindler ark thomas', 'ark thomas keneally', 'thomas keneally novelist'
        ])

    def test__get_keywords_with_small_length_of_words(self):
        sentence = '$, %, (, ), ^, >, <, *, #, @, go, to, am, so, no, ok'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_stop_words(self):
        sentence = "so i'm sorry that i tried to go this way"
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_urls(self):
        sentence = 'www.google.com www.google.com/search?client=ubuntu https://www.google.com/search?client=ubuntu ' \
                   'mailto:test@test.com'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_domain_names(self):
        sentence = 'freepokertourneys.com buyairplanetickets.com thumbtack.net'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_digits_and_dates(self):
        sentence = '658 250,000 1.9m 8pm 2015/10/12 13:35:34 2015-10-12 13:35:34'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_disallowed_strings(self):
        sentence = 'ixzz3kxlsye8l google_api_doesnt_work notfoundhttpexception ______'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])

    def test__get_keywords_with_non_alphanumeric_characters(self):
        sentence = 'radius/ulna news|pictures|filmography|community vista\win b***ches'
        keywords = get_keywords(sentence, ALLOWED_KEYWORD_TAGS)
        self.assertEqual(keywords, [])
