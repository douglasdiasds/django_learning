from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from courses.services.service import CourseService
from courses.models.course_content import CourseContent


@receiver(post_save, sender=CourseContent)
def receiving_content_request(sender,  instance, created, **kwargs):
    print("Request finished!")
    #course_id = kwargs['instance'].course_id
    #content_id = kwargs['instance'].content_id
    #content_couser_id = kwargs['instance'].id
    service = CourseService()
    #instance.course.coursecontent_set.all()
    service.calculate_duration(instance) ##O INSTANCE TEM TDS AS INFORMAÇÕES QUE EU PRECISO
