from django.dispatch import receiver
from django.db.models.signals import post_save

from courses.services.service import CourseService
from courses.models.course_content import CourseContent

"""
Método responsável por fazer a chamada do serviço todas vez que um conteúdo é adicionado ou alterado

instance: contém as informações do curso, duração, conteúdos e a duração dos mesmos, é passado na chamada do service.
"""

@receiver(post_save, sender=CourseContent)
def receiving_content_request(sender,  instance, created, **kwargs):
    service = CourseService()
    service.calculate_duration(instance)
