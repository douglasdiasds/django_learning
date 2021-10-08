import uuid

from django.db import models

TYPE_CHOICES = [
    ("V", "Video"),
    ("P", "Pdf"),
]


class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    description = models.CharField(verbose_name="Description", max_length=200, null=False, blank=False, default="Description")
    url = models.URLField(verbose_name="URL", max_length=1000)
    content_type = models.CharField(verbose_name="Content Type", choices=TYPE_CHOICES, max_length=1)
    duration = models.IntegerField(verbose_name="Duration", default=0)

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Content"
        db_table = "content"
