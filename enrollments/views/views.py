from django.shortcuts import render
from rest_framework import viewsets
from enrollments.models import Enrollment
from enrollments.serializer.serializer import EnrollmentSerializer
from enrollments.services.service import EnrollmentsService


class EnrollmentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Enrollment.objects.all()

    def get_serializer_class(self):
        return EnrollmentSerializer


class FinishEnrollmentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Enrollment.objects.all()

    def get_serializer_class(self):
        return EnrollmentSerializer

    def partial_update(self, request, *args, **kwargs):
        service = EnrollmentsService()
        id = self.kwargs['pk']
        service.finish_enrollment(id)
        return super().partial_update(request)