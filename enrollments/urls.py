from django.urls import path
from .views.views import EnrollmentViewSet

_list = {'get': 'list','post': 'create','put': 'update'}

_edit_and_remove ={'put': 'update','delete': 'destroy'}

urlpatterns = [
    path('', EnrollmentViewSet.as_view(_list), name = 'list'),
    path('/<uuid:pk>', EnrollmentViewSet.as_view(_edit_and_remove), name = 'update'),
]