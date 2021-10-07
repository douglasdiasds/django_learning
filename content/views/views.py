from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView

from content.models import Content
from content.serializer.serializer import ContentSerializer

class ContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Content.objects.all()

    def get_serializer_class(self):
        return ContentSerializer


