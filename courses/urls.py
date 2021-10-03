from django.urls import path
from .views.views import CourseViewSet

_list = {'get': 'list',
         'post': 'create'}

urlpatterns = [
    path('', CourseViewSet.as_view(_list), name = 'list'),
]