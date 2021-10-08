from uuid import uuid4

from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from courses.models import Course


class CourseViewsetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course = mommy.make(Course, id=uuid4(), name='Course 1')
        self.headers = {}
        self.url = reverse('courses-list')

    def test_course_list(self):
        """
        GET /courses
        """
        response = self.client.get(self.url, **self.headers, format='json').json()
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['name'], 'Course 1')

    def test_get_course_by_id(self):
        """
        GET /courses/<id>
        """
        response = self.client.get(
            reverse('courses-detail', args=[str(self.course.id)]),
            **self.headers,
            format='json'
        ).json()
        self.assertEqual(len(response), 8)

    def test_create_new_course(self):
        """
        POST /courses
        """
        data = {
            "name": "New Course Test",
            "duration": 10,
            "holder_image": "https://keeps.com.br"
        }
        response = self.client.post(self.url, data=data, format='json').json()
        self.assertEqual(len(response), 8)
        self.assertEqual(response['name'], data['name'])
        self.assertEqual(response['duration'], data['duration'])

    def test_update_course(self):
        """
        PATCH /courses/<id>
        """
        data = {
            "name": "Course Updated Name"
        }
        response = self.client.patch(
            reverse('courses-detail', args=[str(self.course.id)]),
            data=data,
            **self.headers, format='json'
        ).json()

        self.assertEqual(len(response), 8)
        self.assertEqual(response['name'], data['name'])

    def test_delete_course(self):
        """
        DELETE /courses/<id>
        """
        response = self.client.delete(reverse('courses-detail', args=[str(self.course.id)]))
        self.assertEqual(response.status_code, 204)

    def test_error_create_new_course(self):
        """
        POST /courses
        """
        data = {
            "duration": 10
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    def test_error_create_new_course_holder_image_not_link(self):
        """
        POST /courses
        """
        data = {
            "name": "Course Updated Name",
            "duration": 10,
            "holder_image": 10

        }
        response = self.client.post(self.url, data=data, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['holder_image'][0], 'Enter a valid URL.')
