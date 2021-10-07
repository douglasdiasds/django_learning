from django.db import models
import uuid

from django.db import models

class Content(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False)
    description = models.CharField(verbose_name="Name", max_length=200, null=False, blank=False, default="Description")
    TYPE_CHOICES = [
        ("F", "File"),
        ("L", "Link"),
    ]

    content_type = models.CharField(choices=TYPE_CHOICES, max_length=1, null=False, blank=False)

    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Content"
        db_table = "content"
