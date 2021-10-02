from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    description = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    #holder_image
    duration = models.IntegerField()
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)

    class Meta:
        verbose_name = "Course"
        db_table = "course"