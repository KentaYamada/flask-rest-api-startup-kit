import unittest
from app.tests import test_client


class BaseApiTestCase(unittest.TestCase):
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.endpoint = ''
        self.client = test_client

    def tearDown(self):
        self.client = None
