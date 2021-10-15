from enrollments.models.enrollment import Enrollment


class EnrollmentsService:
    @staticmethod
    def check_enrollment(instance, sender):
        count = 0
        for enrollment in sender.objects.all():
            if enrollment.student_id == instance.student_id and enrollment.status == "AN":
                count += 1

            if count > 1:
                sender.objects.filter(id=instance.id).delete()
                break

    @staticmethod
    def finish_enrollment(enrollment_id):
        for enrollment in Enrollment.objects.filter(id=enrollment_id):

            if enrollment.score < 0.7:
                enrollment.status = "RE"

            else:
                enrollment.status = "AP"

        enrollment.save()
