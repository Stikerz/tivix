from rest_framework.serializers import ModelSerializer
from .models import Teacher, Student, StarStudent


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "age", "year"]


class TeacherSerializer(ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Teacher
        extra_kwargs = {"password": {"write_only": True}}
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "students",
        ]

    def create(self, validated_data):
        password = validated_data.pop("password")
        students = validated_data.pop("students")
        teacher_instance = Teacher.objects.create(**validated_data)
        teacher_instance.set_password(password)
        teacher_instance.students.add(
            *[Student.objects.get(**student) for student in students]
        )
        return teacher_instance

    def update(self, instance, validated_data):
        instance.username = validated_data["username"]
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]
        instance.students.add(
            *[Student.objects.get(**student) for student in validated_data["students"]]
        )

        return instance


class StartStudentSerializer(ModelSerializer):
    class Meta:
        model = StarStudent
        fields = ["teacher", "student", "star"]
