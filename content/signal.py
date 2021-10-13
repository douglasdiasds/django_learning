from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import pre_save

from content.models.content import Content
from .models.course_content import CourseContent

@receiver(pre_save, sender=Content)
def create_content(sender, instance, created, **kwargs):
    if created:
            CourseContent.objects.create(content=instance)
