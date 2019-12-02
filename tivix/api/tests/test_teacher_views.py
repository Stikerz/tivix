from django.test import TestCase

from rest_framework.utils import json
from rest_framework import status

from .h_data import STUDENTS, TEACHERS, INVALID_TEACHER

from ..models import Student, Teacher
from ..serializers import TeacherSerializer


class TeacherViewTest(TestCase):
    def setUp(self):
        teacher = Teacher.objects.create(**TEACHERS[0])
        teacher.set_password("gamora")
        teacher.save()
        student = Student.objects.create(**STUDENTS[2])
        student.save()

    def login(self) -> bool:
        user_login = self.client.login(
            username=TEACHERS[0]["username"], password="gamora"
        )
        return user_login

    def test_create_valid_teacher(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/teachers/",
            data=json.dumps(TEACHERS[1]),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_teacher(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/teachers/",
            data=json.dumps(INVALID_TEACHER),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_teachers_list(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/teachers/")
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_teacher_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/teachers/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_teacher_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/teachers/6/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_teacher(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.put(
            "/api/teachers/1/",
            data=json.dumps(TEACHERS[2]),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_data(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.put(
            "/api/teachers/1/",
            data=json.dumps(INVALID_TEACHER),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_teacher(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.delete("/api/teachers/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
