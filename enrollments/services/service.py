from datetime import datetime

from enrollments.models.enrollment import Enrollment


class EnrollmentsService:
    """
    Método que checa se a matrícula que está sendo registrada ñ possuiu o msm estudante que outra ja registrada e que está em andamento

    instace:
    sender:
    """
    @staticmethod
    def check_enrollment(instance, sender):
        count = 0
        for enrollment in sender.objects.all():
            if enrollment.student_id == instance.student_id and enrollment.status == "AN":
                count += 1

            if count > 1:
                sender.objects.filter(id=instance.id).delete()
                break

    """
    Método que checa se a matrícula que está sendo registrada ñ possuiu o msm estudante que outra ja registrada e que está em andamento

    enrollment_id: id da matricula
    """
    @staticmethod
    def finish_enrollment(enrollment_id):
        for enrollment in Enrollment.objects.filter(id=enrollment_id):

            if enrollment.score < 0.7:
                enrollment.status = "RE"
                enrollment.date_close = datetime.now()

            else:
                enrollment.status = "AP"
                enrollment.date_close = datetime.now()

        enrollment.save()

    """
        Método que checa se a matrícula que está sendo registrada ñ possuiu o msm estudante que outra ja registrada e que está em andamento

        enrollment_id: id da matricula
        """
    @staticmethod
    def restart_enrollment(enrollment_id):

        for enrollment in Enrollment.objects.filter(id=enrollment_id):
            if (enrollment.status == "AP" or "ER") and (enrollment.course.mandatory == False):
                enrollment.date_close = None
                enrollment.score = 0.0
                enrollment.status = "AN"

        enrollment.save()
