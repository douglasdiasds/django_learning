from django.db import models
import uuid

from django.db import models

class Enrollment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #student
    #enrollment
    #status
    created_date = models.DateTimeField(verbose_name="Created Date", auto_now_add=True, null=True, blank=True)
    updated_date = models.DateTimeField(verbose_name="Updated Date", auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.nick_name
