import unittest
from app.libs.json_response import OK, Created, NoContent


class TestJsonResponse(unittest.TestCase):
    def test_http_status_ok_response(self):
        response = OK({'message': 'status OK'})
        payload = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertEqual('status OK', payload['message'])

    def test_http_status_created(self):
        response = Created({'message': 'Created'})
        payload = response.get_json()
        self.assertEqual(201, response.status_code)
        self.assertEqual('Created', payload['message'])

    def test_http_status_no_content(self):
        response = NoContent()
        self.assertEqual(204, response.status_code)
