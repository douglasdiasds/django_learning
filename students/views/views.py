from rest_framework import viewsets

from students.models import Student
from students.serializer.serializer import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Student.objects.all()

    def get_serializer_class(self):
        return StudentSerializer

    def list(self, request, *args, **kwargs):
        return super(StudentViewSet, self).list(request, *args, **kwargs)
