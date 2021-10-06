from django.urls import path
from .views.views import StudentViewSet

_list = {'get': 'list', 'post': 'create'}
_detail = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
_ready_only = {'get': 'list'}
_delete_only = {'delete': 'destroy'}

urlpatterns = [
    path('', StudentViewSet.as_view(_ready_only), name='student-list'),
    path('/<uuid:pk>', StudentViewSet.as_view(_detail), name='student-detail')
]
