from uuid import uuid4

from django.urls import reverse
from django.test import TestCase
from model_mommy import mommy
from rest_framework.test import APIClient

from enrollments.models import Enrollment
from courses.models import Course
from students.models import Student


class EnrollmentViewsetTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.course = mommy.make(Course, id=uuid4(), name='New Course')
        self.student = mommy.make(Student, id=uuid4(), name='New Student')
        self.enrollment = mommy.make(Enrollment, id=uuid4(), student=self.student, course=self.course)
        self.headers = {}
        self.url = reverse('enrollments-list')


    def test_enrollment_list(self):
        """
        #GET /enrollments
        """
        response = self.client.get(self.url, **self.headers, format='json').json()
        self.assertEqual(len(response), 1)
        self.assertEqual(response[0]['student'], str(self.student.id))

    def test_get_enrollment_by_id(self):
        """
        #GET /enrollments/<id>
        """
        response = self.client.get(reverse('enrollment-detail', args=[str(self.enrollment.id)]),
                                           **self.headers, format='json').json()
        self.assertEqual(len(response), 7)

    def test_create_new_enrollment(self):
        """
        #POST /enrollments
        """
        data = {
            "student": self.student.id,
            "course": self.course.id
        }
        response = self.client.post(self.url, data=data, format='json').json()
        self.assertEqual(len(response), 7)
        self.assertEqual(response['student'], str(data['student']))
        self.assertEqual(response['course'], str(data['course']))

    def test_update_enrollment(self):
        """
        #PATCH /enrollments/<id>
        """
        data = {
            "student": self.student.id
        }
        response = self.client.patch(reverse('enrollment-detail', args=[str(self.enrollment.id)]), data=data,
                                     **self.headers, format='json').json()

        self.assertEqual(len(response), 7)
        self.assertEqual(response['student'], str(data['student']))

    def test_delete_enrollment(self):
        """
        #DELETE /enrollments/<id>
        """
        response = self.client.delete(reverse('enrollment-detail', args=[str(self.enrollment.id)]))
        self.assertEqual(response.status_code, 204)

    def test_error_create_new_enrollment(self):
        """
        #POST /enrollments
        """
        data = {
            "duration": 10
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, 400)