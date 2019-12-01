from django.shortcuts import render
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     ListAPIView)

from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Student, StarStudent
from .serializers import StudentSerializer, TeacherSerializer

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


class TeacherAPIView(ListAPIView):
    """view for listing a queryset."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]


class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    """view for retrieving, updating or deleting a model instance."""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

    # def perform_destroy(self, serializer):
    #     serializer.save(user=self.request.user)
