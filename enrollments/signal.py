from django.dispatch import receiver
from django.db.models.signals import post_save

from enrollments.models.enrollment import Enrollment
from enrollments.services.service import EnrollmentsService


@receiver(post_save, sender=Enrollment)
def check_enrollment(sender,  instance, created, **kwargs):
    print("Request finished!")
    service = EnrollmentsService()
    service.calculate_duration(instance, sender)