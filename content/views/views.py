from rest_framework import viewsets

from content.models import Content
from content.serializer.serializer import ContentSerializer


class ContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Content.objects.all()

    def get_serializer_class(self):
        return ContentSerializer

    def create(self, request, *args, **kwargs):
        """
        Salva a primary key no 'request.data' & posteriormente passa-o como um dos argumentos para o método super.create()

        request_data = {'content_id': 'xpto', 'course_id': 'xpto'}
        course_id in self.kwargs['pk']
        """
        request.data['course_content'] = self.kwargs['pk']
        return super(ContentViewSet, self).create(request, *args, **kwargs)