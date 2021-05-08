import unittest
from app import app


class BaseApiTestCase(unittest.TestCase):
    CONTENT_TYPE = 'application/json'

    def setUp(self):
        self.endpoint = ''
        self.client = app.test_client()

    def tearDown(self):
        self.client = None
