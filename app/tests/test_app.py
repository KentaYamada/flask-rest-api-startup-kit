import json
import unittest
from app import app


class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        self.client = None

    def test_handle_api_exception_when_notfound_error(self):
        response = self.client.get('/hoge/fuga')
        data = response.get_json()
        self.assertEqual(404, data['code'])
