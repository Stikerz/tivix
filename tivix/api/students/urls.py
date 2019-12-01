from django.urls import path

from ..views import (StudentAPIView, StudentDetailView)

urlpatterns = [
    path('', StudentAPIView.as_view(), name='student_list'),
    path('<int:pk>/', StudentDetailView.as_view(), name='student_detail')

]