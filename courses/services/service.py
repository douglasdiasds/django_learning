class CourseService:

    """
    Serviço que calcula a duração de um 'course' de acordo com a duração de seus respectivos 'contents'

    instance: contém as informações do curso, duração, conteúdos e a duração dos mesmos.
    """
    def calculate_duration(self, instance):
        duration = 0

        for course_content in instance.course.coursecontent_set.all():
            duration += course_content.content.duration

        instance.course.duration = duration
        instance.course.save()




