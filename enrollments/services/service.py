from enrollments.models.enrollment import Enrollment

class EnrollmentsService:

    def check_enrollment(self, instance, sender):
        count = 0
        for enrollment in sender.objects.all():
            if enrollment.student_id == instance.student_id and enrollment.status == "AN":
                count += 1

            if count > 1:
                sender.objects.filter(id=instance.id).delete()
                #Enrollment.objects.filter(student=instance.student_id).delete()
                break;