from django.dispatch import receiver
from django.db.models.signals import post_save

from courses.services.service import CourseService
from courses.models.course_content import CourseContent


@receiver(post_save, sender=CourseContent)
def receiving_content_request(sender,  instance, created, **kwargs):
    print("Request finished!")
    service = CourseService()
    service.calculate_duration(instance)
