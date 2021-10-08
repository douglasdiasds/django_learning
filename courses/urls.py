from django.urls import path
from .views.views import CourseViewSet, CourseContentViewSet

_list = {'get': 'list',
         'post': 'create'}

_edit_and_remove = {'get': 'retrieve',
                    'put': 'update',
                    'delete': 'destroy',
                    'patch': 'partial_update'}

urlpatterns = [
    path('', CourseViewSet.as_view(_list), name='courses-list'),
    path('/<uuid:pk>', CourseViewSet.as_view(_edit_and_remove), name='courses-detail'),
    path('/<uuid:pk>/cotents', CourseContentViewSet.as_view(_edit_and_remove), name='courses-contents'),
]
