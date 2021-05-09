import json
import unittest
from app.tests import test_client


class TestFlaskApp(unittest.TestCase):
    def test_handle_api_exception_when_notfound_error(self):
        response = test_client.get('/hoge/fuga')
        data = response.get_json()
        self.assertEqual(404, data['code'])
