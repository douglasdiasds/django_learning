import uuid

from django.db import models


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    description = models.CharField(verbose_name="Description", max_length=200, null=False, blank=False, default="Description")
    duration = models.IntegerField(max_length=10)
    holder_image = models.URLField(max_length=200, null=False, default="http://keeps.com.br")
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)
    mandatory = models.BooleanField(verbose_name="Mandatory", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        db_table = "course"
