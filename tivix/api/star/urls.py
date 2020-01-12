from django.urls import path

from api.views import (StudentStarAPIView, StudentStarDetailView)

urlpatterns = [
    path('', StudentStarAPIView.as_view(), name='student_star_list'),
    path('<int:pk>/', StudentStarDetailView.as_view(),
         name='student_star_detail')

]