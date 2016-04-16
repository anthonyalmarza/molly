from django.test import TestCase
from django.core.wsgi import WSGIHandler
from molly.test import TestCase as MollyTestCase

import mock


class ApplicationStartedTests(TestCase):

    def test_application_started_send(self):
        with mock.patch('molly.signals.application_started.send') as send:
            application = WSGIHandler()
            self.assertTrue(send.called)

            send.assert_called_once_with(
                sender=WSGIHandler, application=application
            )

    def test_name(self):
        self.assertEqual(WSGIHandler.__init__.__name__, '__init__')


class TestMollyTestCase(MollyTestCase):

    def test_appliction_instatiated(self):
        self.assertTrue(self.application is not None)
        self.assertIsInstance(self.application, WSGIHandler)
