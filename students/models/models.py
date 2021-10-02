import uuid

from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    nick_name = models.CharField(verbose_name="Surename", max_length=200, null=False, blank=False)
    phone = models.CharField(verbose_name="Phone", max_length=20, null=True, blank=True)
    avatar = models.TextField(verbose_name='Avatar', null=True, blank=True)
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nick_name

    class Meta:
        verbose_name = "Student"
        db_table = "student"