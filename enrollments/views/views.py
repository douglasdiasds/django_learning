from django.shortcuts import render
from rest_framework import viewsets
from enrollments.models import Enrollment
from enrollments.serializer.serializer import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Enrollment.objects.all()

    def get_serializer_class(self):
        return EnrollmentSerializer
