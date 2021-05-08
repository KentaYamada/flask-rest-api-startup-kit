import json
from urllib.parse import urljoin
from app.tests.api.base import BaseApiTestCase


class TestSampleApi(BaseApiTestCase):
    def setUp(self):
        super().setUp()
        self.endpoint = '/api/samples/'

    def test_get(self):
        response = self.client.get(
            self.endpoint,
            content_type=TestSampleApi.CONTENT_TYPE
        )
        body = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertTrue('message' in body)
        self.assertEqual('ham', body['message'])

    def test_get_by_language(self):
        url = urljoin(self.endpoint, '1')
        response = self.client.get(
            url,
            content_type=TestSampleApi.CONTENT_TYPE
        )
        body = response.get_json()
        self.assertEqual(200, response.status_code)
        self.assertTrue('language' in body)
        self.assertEqual('python', body['language'])

    def test_get_by_language_when_no_item(self):
        url = urljoin(self.endpoint, '999')
        response = self.client.get(
            url,
            content_type=TestSampleApi.CONTENT_TYPE
        )
        body = response.get_json()
        self.assertEqual(404, response.status_code)
        self.assertTrue('description' in body)
        self.assertEqual('Language not found', body['description'])

    def test_post(self):
        payload = json.dumps({
            'language': 'c++'
        })
        response = self.client.post(
            self.endpoint,
            content_type=TestSampleApi.CONTENT_TYPE,
            data=payload
        )
        body = response.get_json()
        self.assertEqual(201, response.status_code)

    def test_post_empty_request(self):
        payload = json.dumps({})
        response = self.client.post(
            self.endpoint,
            content_type=TestSampleApi.CONTENT_TYPE,
            data=payload
        )
        body = response.get_json()
        self.assertEqual(400, response.status_code)

    def test_put(self):
        url = urljoin(self.endpoint, '1')
        payload = json.dumps({
            'id': '1',
            'language': 'python 3'
        })
        response = self.client.put(
            url,
            content_type=TestSampleApi.CONTENT_TYPE,
            data=payload
        )
        body = response.get_json()
        self.assertEqual(200, response.status_code)

    def test_put_when_data_is_not_exists(self):
        url = urljoin(self.endpoint, '999')
        payload = json.dumps({
            'language': 'python 3'
        })
        response = self.client.put(
            url,
            content_type=TestSampleApi.CONTENT_TYPE,
            data=payload
        )
        body = response.get_json()
        self.assertEqual(404, response.status_code)
        self.assertEqual('Language is not exist', body['description'])

    def test_delete(self):
        url = urljoin(self.endpoint, '1')
        response = self.client.delete(
            url,
            content_type=TestSampleApi.CONTENT_TYPE
        )
        self.assertEqual(204, response.status_code)

    def test_delete_when_no_data(self):
        url = urljoin(self.endpoint, '999')
        response = self.client.delete(
            url,
            content_type=TestSampleApi.CONTENT_TYPE
        )
        self.assertEqual(404, response.status_code)
