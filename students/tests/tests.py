from uuid import uuid4

from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from students.models import Student


class CourseViewsetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course = mommy.make(Student, id=uuid4(), name='Student 1')
        self.headers = {}
        self.url = reverse('students-list')

    def test_student_list(self):
        """
        GET /students
        """
        response = self.client.get(self.url, **self.headers, format='json').json()
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['name'], 'Student 1')

    def test_get_student_by_id(self):
        """
        GET /students/<id>
        """
        response = self.client.get(reverse('students-detail', args=[str(self.course.id)]),
                                           **self.headers, format='json').json()
        self.assertEqual(len(response), 7)

    def test_create_new_student(self):
        """
        POST /students
        """
        data = {
            "name": "New Student",
            "nick_name": "Test"
        }
        response = self.client.post(self.url, data=data, format='json').json()
        self.assertEqual(len(response), 7)
        self.assertEqual(response['name'], data['name'])
        self.assertEqual(response['nick_name'], data['nick_name'])

    def test_update_student(self):
        """
        PATCH /courses/<id>
        """
        data = {
            "name": "Student Updated Name"
        }
        response = self.client.patch(reverse('students-detail', args=[str(self.course.id)]), data=data,
                                     **self.headers, format='json').json()

        self.assertEqual(len(response), 7)
        self.assertEqual(response['name'], data['name'])

    def test_delete_student(self):
        """
        DELETE /courses/<id>
        """
        response = self.client.delete(reverse('students-detail', args=[str(self.course.id)]))
        self.assertEqual(response.status_code, 204)

    def test_error_create_new_student(self):
        """
        POST /courses
        """
        data = {
            "duration": 10
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, 400)

    """
    def test_error_create_new_course_holder_image_not_link(self):
       
        POST /courses
       
        data = {
            "name": "Course Updated Name",
            "duration": 10,
            "holder_image": 10

        }
        response = self.client.post(self.url, data=data, format='json')
        response_data = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data['holder_image'][0], 'Enter a valid URL.')
    """