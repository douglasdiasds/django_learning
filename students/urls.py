from django.urls import path
from .views.views import StudentViewSet

_list = {'get': 'list',
         'post': 'create',
         'put': 'update'}

_edit_and_remove = {'get': 'retrieve',
                    'put': 'update',
                    'delete': 'destroy',
                    'patch': 'partial_update'}

#_detail = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
#_ready_only = {'get': 'list'}
#_delete_only = {'delete': 'destroy'}

urlpatterns = [
    path('', StudentViewSet.as_view(_list), name='students-list'),
    path('/<uuid:pk>', StudentViewSet.as_view(_edit_and_remove), name='students-detail')
]
