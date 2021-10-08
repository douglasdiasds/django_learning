from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT, HTTP_200_OK

from courses.models import Course, CourseContent
from courses.serializer.serializer import CourseSerializer, CourseContentSerializer, CourseContentListSerializer


class CourseViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        return Course.objects.all()

    def get_serializer_class(self):
        return CourseSerializer



class CourseContentViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        """
        Salva a primary key em uma variável & passa a mesma como argumento p/ o filtro
        """
        course_id = self.kwargs['pk']
        return CourseContent.objects.filter(course_id=course_id)#ONDE O PRIMEIRO 'course_id' FOI DEFINIDO?

    def get_serializer_class(self):
        """
        Aqui o serializador retornado é de acordo com o método HTTPS recebido
        GET => CourseContentListSerializer
        POST => CourseContentSerializer
        """
        return CourseContentListSerializer if self.request.method == 'GET' else CourseContentSerializer

    def create(self, request, *args, **kwargs):
        """
        Salva a primary key no 'request.data' & posteriormente passa-o como um dos argumentos para o método super.create()

        request_data = {'content_id': 'xpto', 'course_id': 'xpto'}
        course_id in self.kwargs['pk']
        """
        request.data['course'] = self.kwargs['pk']
        return super(CourseContentViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        contents - recebe tds os conteudos(contents) referentes ao curso(courses)
        content_id - recebe o id que está sendo buscado entre os conteudos
        course_content - recebe o resultado da busca que usou como parametro o id a cima
        course_content_data - serializa os dados recebdos em course_content
        """
        contents = self.get_queryset()
        content_id = self.kwargs['content_id']

        course_content = contents.filter(content_id=content_id).first()
        if not course_content:
            return Response(data={'i18n': 'not_found'}, status=HTTP_404_NOT_FOUND)

        course_content_data = self.get_serializer_class()(course_content).data
        return Response(data=course_content_data, status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        """
        contents - recebe tds os conteudos(contents) referentes ao curso(courses)
        content_id - recebe o id que está sendo buscado entre os conteudos
        course_content - recebe o resultado da busca que usou como parametro o id a cima
        """
        contents = self.get_queryset()
        content_id = self.kwargs['content_id']

        course_content = contents.filter(content_id=content_id).first()
        if not course_content:
            return Response(data={'i18n': 'not_found'}, status=HTTP_404_NOT_FOUND)

        course_content.delete()

        return Response(status=HTTP_204_NO_CONTENT)
