from django.shortcuts import render
from rest_framework import viewsets
from enrollments.models import Enrollment
from enrollments.serializer.serializer import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()