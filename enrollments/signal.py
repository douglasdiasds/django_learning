from django.dispatch import receiver
from django.db.models.signals import post_save

from enrollments.models.enrollment import Enrollment
from enrollments.services.service import EnrollmentsService

"""
Método responsável por fazer a chamada do serviço todas vez que uma matrícula é adicionada

instance: contém as informações do curso, duração, conteúdos e a duração dos mesmos, é passado na chamada do service.
sender:
"""
@receiver(post_save, sender=Enrollment)
def check_enrollment(sender,  instance, created, **kwargs):
    service = EnrollmentsService()
    service.check_enrollment(instance, sender)