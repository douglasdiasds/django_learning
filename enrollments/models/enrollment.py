from django.db import models
import uuid

from django.db import models
from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, related_name='enrollments')
    course = models.ForeignKey(Course, related_name='enrollments')
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)
    STATUS_CHOICES = [
        ("AN", "Andamento"),
        ("AP", "Aprovado"),
        ("RE", "Reprovado"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)

    def __str__(self):
        return self.nick_name
