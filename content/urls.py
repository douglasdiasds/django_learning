from django.urls import path
from content.views.views import ContentViewSet

_list = {'get': 'list',
         'post': 'create'}

_detail = {'get': 'retrieve',
           'put': 'update',
           'delete': 'destroy',
           'patch': 'partial_update'}

urlpatterns = [
    path('', ContentViewSet.as_view(_list), name='contents-list'),
    path('/<uuid:pk>', ContentViewSet.as_view(_detail), name='contents-detail')
]
