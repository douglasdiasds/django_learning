from courses.models.course_content import CourseContent
from content.models.content import Content
from courses.models.course import Course


class CourseService:

    def calculate_duration(self, instance):
        duration = 0

        for course_content in instance.course.coursecontent_set.all():
            duration += course_content.content.duration

        instance.course.duration = duration
        instance.course.save()




