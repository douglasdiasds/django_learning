from django.urls import path
from .views.views import EnrollmentViewSet, FinishEnrollmentViewSet

_list = {'get': 'list',
         'post': 'create',
         'put': 'update'}

_edit_and_remove = {'get': 'retrieve',
                    'put': 'update',
                    'delete': 'destroy',
                    'patch': 'partial_update'}

urlpatterns = [
    path('', EnrollmentViewSet.as_view(_list), name='enrollments-list'),
    path('/<uuid:pk>', EnrollmentViewSet.as_view(_edit_and_remove), name='enrollment-detail'),
    path('/finish/<uuid:pk>', FinishEnrollmentViewSet.as_view(_edit_and_remove), name='enrollment-detail'),
]