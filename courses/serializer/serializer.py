from rest_framework import serializers

from courses.models import Course
from courses.models.course_content import CourseContent


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseContentListSerializer(serializers.ModelSerializer):
    """
    GET
    Serializador de LISTAGEM

    depth = Recebe um valor inteiro que indica o quão profundo no relacionamento o serializador deve ir antes de retornar uma representação do dados
    """
    class Meta:
        model = CourseContent
        fields = '__all__'
        depth = 2


class CourseContentSerializer(serializers.ModelSerializer):
    """
    POST
    Serializador de INSERÇÃO
    """
    class Meta:
        model = CourseContent
        fields = '__all__'
