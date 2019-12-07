from rest_framework.serializers import ModelSerializer
from .models import Teacher, Student, StarStudent
from django.db import IntegrityError


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "age", "year"]


class TeacherSerializer(ModelSerializer):
    students = StudentSerializer(many=True)

    class Meta:
        model = Teacher
        extra_kwargs = {
            "password": {"required": False, "write_only": True},
            "students": {"required": False},
        }
        fields = [
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "students",
        ]

    def create_link(self, teacher, students):
        for student in students:
            try:
                data = {"teacher": teacher, "student": student, "star": False}
                StarStudent.objects.get_or_create(**data)
            except IntegrityError as e:
                continue

    def create(self, validated_data):
        password = validated_data.pop("password")
        students = validated_data.pop("students")
        teacher_instance = Teacher.objects.create(**validated_data)
        teacher_instance.set_password(password)
        student_instances = [Student.objects.get(**student) for student in students]
        teacher_instance.students.add(*student_instances)
        teacher_instance.save()
        self.create_link(teacher_instance, student_instances)
        return teacher_instance

    def update(self, instance, validated_data):
        instance.username = validated_data["username"]
        instance.first_name = validated_data["first_name"]
        instance.last_name = validated_data["last_name"]
        instance.email = validated_data["email"]
        student_instances = [
            Student.objects.get(**student) for student in validated_data["students"]
        ]
        instance.students.clear()
        instance.students.add(*student_instances)
        instance.save()
        self.create_link(instance, student_instances)
        return instance


class StartStudentSerializer(ModelSerializer):
    student = StudentSerializer()

    def create(self, validated_data):
        teacher = validated_data["teacher"]
        student = Student.objects.get(**validated_data["student"])
        star = validated_data["star"]
        d = {"teacher": teacher, "student": student, "star": star}
        star_instance, created = StarStudent.objects.get_or_create(**d)

        return star_instance

    def update(self, instance, validated_data):
        instance.star = validated_data["star"]
        instance.save()
        return instance

    class Meta:
        model = StarStudent
        fields = ["id", "teacher", "student", "star"]
