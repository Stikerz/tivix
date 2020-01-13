from django.test import TestCase

from rest_framework import status

from api.tests.h_data import STUDENTS, TEACHERS

from api.models import Student, Teacher


class TivixViewTest(TestCase):
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

    def test_login_view_with_user_loggedout(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "login.html")

    def test_login_view_with_user_loggedin(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_login_view_valid_signin(self):
        data = {"username": TEACHERS[0]["username"], "password": "gamora"}

        response = self.client.post("", data=data, content_type="application/json",)
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_login_view_invalid_signin(self):
        data = {"username": TEACHERS[0]["username"], "password": ""}

        response = self.client.post("", data=data, content_type="application/json",)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register_view(self):
        response = self.client.get("/register/")
        self.assertTemplateUsed(response, "register.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_register_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_teachers_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/teachers/")
        self.assertTemplateUsed(response, "teachers.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teachers_view_logged_out(self):
        response = self.client.get("/teachers/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_mystudents_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/mystudents/")
        self.assertTemplateUsed(response, "mystudents.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_mystudents_view_logged_out(self):
        response = self.client.get("/mystudents/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_student_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/student/")
        self.assertTemplateUsed(response, "student.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_view_logged_out(self):
        response = self.client.get("/student/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_profile_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/profile/")
        self.assertTemplateUsed(response, "profile.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_view_logged_out(self):
        response = self.client.get("/profile/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_star_view_logged_in(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/star/")
        self.assertTemplateUsed(response, "star.html")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_star_view_logged_out(self):
        response = self.client.get("/star/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_signout_view(self):
        user_login = self.login()
        self.assertTrue(user_login)
        response = self.client.get("/logout/")
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
