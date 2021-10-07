from django.db import models
import uuid

from django.db import models
from courses.models import Course
from students.models import Student


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, related_name='enrollments', on_delete=models.PROTECT, null=False)
    course = models.ForeignKey(Course, related_name='enrollments', on_delete=models.PROTECT, null=True)
    date_enroll = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    date_close = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)
    STATUS_CHOICES = [
        ("AN", "Andamento"),
        ("AP", "Aprovado"),
        ("RE", "Reprovado"),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default="AN")
    score = models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)

    def __str__(self):
        return self.id
