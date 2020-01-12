from django.test import TestCase

from rest_framework.utils import json
from rest_framework import status

from api.tests.h_data import STUDENTS, TEACHERS, STARS, INVALID_STAR, UPDATED_STAR

from api.models import Student, Teacher, StarStudent
from api.serializers import StartStudentSerializer


class StarViewTest(TestCase):
    def setUp(self):
        teacher = Teacher.objects.create(**TEACHERS[0])
        teacher.set_password("gamora")
        teacher.save()
        for student in STUDENTS:
            student_instance = Student.objects.create(**student)
            student_instance.save()

    def login(self) -> bool:
        user_login: bool = self.client.login(
            username=TEACHERS[0]["username"], password="gamora"
        )
        return user_login

    def create_star(self) -> None:
        for star in STARS:
            self.client.post(
                "/api/star/", data=json.dumps(star), content_type="application/json",
            )

    def test_create_valid_star(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/star/", data=json.dumps(STARS[0]), content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.post(
            "/api/star/",
            data=json.dumps(INVALID_STAR),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_star_list(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.get("/api/star/")

        star_students = StarStudent.objects.all().filter(
            teacher=STARS[0]["teacher"], star=True
        )
        serializer = StartStudentSerializer(star_students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(star_students), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_unstar_list(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.get("/api/star/?star=false")

        star_students = StarStudent.objects.all().filter(
            teacher=STARS[0]["teacher"], star=False
        )
        serializer = StartStudentSerializer(star_students, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(star_students), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_star_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.get("/api/star/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_star_detailed(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/api/star/1/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.put(
            "/api/star/1/",
            data=json.dumps(UPDATED_STAR),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invalid_data(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.put(
            "/api/star/1/",
            data=json.dumps(INVALID_STAR),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_student(self):
        user_login = self.login()
        self.assertTrue(user_login)
        self.create_star()
        response = self.client.delete("/api/star/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
