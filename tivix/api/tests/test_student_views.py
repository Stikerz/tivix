from django.test import TestCase

from rest_framework.utils import json
from rest_framework import status

from api.tests.h_data import STUDENTS, TEACHERS, INVALID_STUDENT

from api.models import Student, Teacher
from api.serializers import StudentSerializer


class StudentViewTest(TestCase):
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

    def test_create_valid_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/students/",
            data=json.dumps(STUDENTS[0]),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/students/",
            data=json.dumps(INVALID_STUDENT),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_students_list(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/students/")
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_student_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/students/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_student_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/students/6/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.put(
            "/api/students/1/",
            data=json.dumps(STUDENTS[1]),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_data(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.put(
            "/api/students/1/",
            data=json.dumps(INVALID_STUDENT),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.delete("/api/students/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
