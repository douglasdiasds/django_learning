from django.urls import path
from .views.views import CourseViewSet

_list = {'get': 'list',
         'post': 'create'}

_edit ={'put': 'update'}

_delete ={'delete': 'destroy'}

urlpatterns = [
    path('', CourseViewSet.as_view(_list), name = 'list'),
    path('/<uuid:pk>', CourseViewSet.as_view(_edit), name = 'update'),
]