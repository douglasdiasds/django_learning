from django.shortcuts import render
from rest_framework import viewsets
from students.models import Student
from students.serializer.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()