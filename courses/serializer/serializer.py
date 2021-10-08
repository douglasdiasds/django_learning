from rest_framework import serializers

from courses.models import Course
from courses.models.course_content import CourseContent


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = '__all__'
        depth = 2


class CourseContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseContent
        fields = '__all__'
