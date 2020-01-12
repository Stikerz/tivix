from django.urls import path

from api.views import (TeacherAPIView, TeacherDetailView)

urlpatterns = [
    path('', TeacherAPIView.as_view(), name='teacher_list'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail')
]