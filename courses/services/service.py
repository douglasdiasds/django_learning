from courses.models.course_content import CourseContent
from content.models.content import Content
from courses.models.course import Course


class CourseService:

    def calculate_duration(self, instance):
        duration = 0
        for content in instance.course.coursecontent_set(): ##existem métodos como este 'coursecontent_set' que apontam para os items correspondentes a FK de instance, neste caso course & content
            duration += content.duration




