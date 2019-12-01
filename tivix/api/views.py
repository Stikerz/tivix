from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Student, StarStudent
from .serializers import StudentSerializer

# Create your views here.


class StudentAPIView(ListCreateAPIView):
    """view for listing a queryset or creating a model instance."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class StudentDetailView(RetrieveUpdateDestroyAPIView):
    """view for retrieving, updating or deleting a model instance."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]