from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from content.models import Content


class ContentViewsetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.content = mommy.make(Content, content_type='V', url='https://www.youtube.com/watch?v=ln6t3uyTveQ')
        self.headers = {}
        self.url = reverse('contents-list')

    def test_content_list(self):
        """
        GET /contents
        """
        response = self.client.get(self.url, **self.headers, format='json').json()
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['name'], self.content.name)

    def test_get_content_by_id(self):
        """
        GET /contents/<id>
        """
        response = self.client.get(
            reverse('contents-detail', args=[str(self.content.id)]),
            **self.headers,
            format='json'
        ).json()
        self.assertEqual(len(response), 8)

    def test_create_new_content(self):
        """
        POST /contents
        """
        data = {
            "name": "New Content Test",
            "duration": 10,
            "content_type": "V",
            "url": "https://keeps.com.br"
        }
        response = self.client.post(self.url, data=data, format='json')
        response_json = response.json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response_json), 8)
        self.assertEqual(response_json['name'], data['name'])
        self.assertEqual(response_json['duration'], data['duration'])

    def test_update_Content(self):
        """
        PATCH /Contents/<id>
        """
        data = {
            "name": "Content Updated Name"
        }
        response = self.client.patch(
            reverse('contents-detail', args=[str(self.content.id)]),
            data=data,
            **self.headers, format='json'
        ).json()

        self.assertEqual(len(response), 8)
        self.assertEqual(response['name'], data['name'])

    def test_delete_content(self):
        """
        DELETE /Contents/<id>
        """
        response = self.client.delete(reverse('contents-detail', args=[str(self.content.id)]))
        self.assertEqual(response.status_code, 204)

    def test_error_create_new_Content(self):
        """
        POST /Contents
        """
        data = {
            "duration": 10
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, 400)
