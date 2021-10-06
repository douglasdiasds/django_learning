from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from courses.models import Course
from courses.serializer.serializer import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Course.objects.all()

    def get_serializer_class(self):
        return CourseSerializer
