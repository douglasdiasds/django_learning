from django.urls import path
from .views.views import StudentViewSet

_list = {'get': 'list',
         'post': 'create',
         'put': 'update'}

_edit ={'put': 'update'}

urlpatterns = [
    path('', StudentViewSet.as_view(_list), name = 'list'),
    path('/<uuid:pk>', StudentViewSet.as_view(_edit), name = 'update'),
]