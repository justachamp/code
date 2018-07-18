from testfixtures.logcapture import log_capture

from django.core import mail
from django.test import TestCase

from addnow.apps.reports import tasks


class TasksTestCase(TestCase):
    @log_capture()
    def test__task_site_stats(self, log_data):
        result = tasks.site_stats.delay(['mail@mail.com', 'mail2@mail.com'])
        self.assertEqual(len(mail.outbox), 1)
        result.get()
        log_data.check(('addnow.apps.reports.tasks', 'INFO', 'Created site stats report'),)
