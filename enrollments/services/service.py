class EnrollmentsService:

    def calculate_duration(self, instance, sender):
        print("calculate_duration")
        for enrollment in sender.objects.all():
            if enrollment.student_id == instance.student_id:
                print("igual")