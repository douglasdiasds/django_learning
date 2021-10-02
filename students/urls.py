from django.urls import path
from .views.views import StudentViewSet

_list = {'get': 'list',
         'post': 'create'}




urlpatterns = [
    path('', StudentViewSet.as_view(_list), name = 'list'),
]