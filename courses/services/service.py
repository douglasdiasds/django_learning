class CourseService:

    def calculate_duration(self, instance):
        duration = 0

        for course_content in instance.course.coursecontent_set.all():
            duration += course_content.content.duration

        instance.course.duration = duration
        instance.course.save()




