import uuid

from django.db import models

from content.models import Content
from courses.models import Course


class CourseContent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, verbose_name="Course", on_delete=models.CASCADE)
    content = models.ForeignKey(Content, verbose_name="Content", on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "CourseContent"
        unique_together = ("course", "content")
        db_table = "course_content"
