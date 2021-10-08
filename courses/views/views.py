from rest_framework import viewsets

from courses.models import Course
from courses.serializer.serializer import CourseSerializer
from content.models import Content
from content.serializer.serializer import ContentSerializer


class CourseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Course.objects.all()

    def get_serializer_class(self):
        return CourseSerializer


class CourseContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Content.objects.all()

    def get_serializer_class(self):
        return ContentSerializer
