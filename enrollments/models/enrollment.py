from django.db import models
import uuid

from django.db import models
from courses.models import Course
from students.models import Student

STATUS_CHOICES = [
        ("AN", "Andamento"),
        ("AP", "Aprovado"),
        ("RE", "Reprovado"),
]


class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.PROTECT)
    course = models.ForeignKey(Course, related_name='courses', on_delete=models.PROTECT)
    date_enroll = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    date_close = models.DateTimeField(verbose_name="Updated Date", auto_now=False, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default="AN")
    #score = models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True)
    score = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Enrollment"
        db_table = "enrollment"
