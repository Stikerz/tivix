from rest_framework.serializers import ModelSerializer
from .models import Teacher, Student, StarStudent


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'year']


class TeacherSerializer(ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ['username', 'first_name', 'last_name', 'email', 'students']


class StartStudentSerializer(ModelSerializer):
    student = StudentSerializer(many=True)
    teacher = TeacherSerializer(many=True)

    class Meta:
        model = StarStudent
        fields = ['teacher', 'student', 'star']