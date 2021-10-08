from django.urls import path
from .views.views import CourseViewSet, CourseContentViewSet

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'delete': 'destroy',
           'patch': 'partial_update'}

_only_retrieve_and_delete = {'get': 'retrieve',
                             'delete': 'destroy'}

urlpatterns = [
    path('', CourseViewSet.as_view(_list), name='courses-list'),
    path('/<uuid:pk>', CourseViewSet.as_view(_detail), name='courses-detail'),

    path('/<uuid:pk>/contents', CourseContentViewSet.as_view(_list), name='course-contents-list'),
    path('/<uuid:pk>/contents/<uuid:content_id>', CourseContentViewSet.as_view(_only_retrieve_and_delete), name='course-contents-detail'),
]
