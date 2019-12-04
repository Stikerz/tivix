from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from .models import Teacher, Student, StarStudent
from .serializers import StudentSerializer, TeacherSerializer, StartStudentSerializer

# Create your views here.
# TODO : User Permission check - only user can edit own instance info ect


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


class TeacherAPIView(ListCreateAPIView):
    """view for listing a queryset or create"""

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = []


class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    """view for retrieving, updating or deleting a model instance."""

    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    # def perform_update(self, serializer):
    #     serializer.save(user=self.request.user)

    # def perform_destroy(self, serializer):
    #     serializer.save(user=self.request.user)


class StudentStarAPIView(ListCreateAPIView):
    """view for listing a queryset."""

    serializer_class = StartStudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned star studenta to a given teacher,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = StarStudent.objects.all()
        params = self.request.query_params.get("star", None)
        star = True

        if params:
            if params.lower() == "true" or params.lower() == "false":
                star = params.lower() == "true"
        queryset = queryset.filter(star=star, teacher=self.request.user)
        return queryset


class StudentStarDetailView(RetrieveUpdateDestroyAPIView):
    """view for retrieving, updating or deleting a model instance."""

    queryset = StarStudent.objects.all()
    serializer_class = StartStudentSerializer
    permission_classes = [IsAuthenticated]
