from django.db import IntegrityError
from django.test import TestCase
import mock

from api.tests.h_data import TEACHERS

from api.models import Teacher

from social_django.models import UserSocialAuth


class TestSocialAuthUser(TestCase):
    def test_user_relationship_none(self):
        """Accessing Teacher.social_user outside of the pipeline doesn't
        work"""
        user = Teacher.objects.create(**TEACHERS[0])
        with self.assertRaises(AttributeError):
            user.social_user

    def test_user_existing_relationship(self):
        """Accessing Teacher.social_user outside of the pipeline doesn't work"""
        user = Teacher.objects.create(**TEACHERS[0])
        UserSocialAuth.objects.create(user=user, provider="my-provider", uid="1234")
        with self.assertRaises(AttributeError):
            user.social_user

    def test_get_social_auth(self):
        user = Teacher.objects.create(**TEACHERS[0])
        user_social = UserSocialAuth.objects.create(
            user=user, provider="my-provider", uid="1234"
        )
        other = UserSocialAuth.get_social_auth("my-provider", "1234")
        self.assertEqual(other, user_social)

    def test_get_social_auth_none(self):
        other = UserSocialAuth.get_social_auth("my-provider", "1234")
        self.assertIsNone(other)


class TestUserSocialAuth(TestCase):
    def setUp(self):
        self.user_model = Teacher
        self.user = self.user_model.objects.create(**TEACHERS[0])
        self.usa = UserSocialAuth.objects.create(
            user=self.user, provider="my-provider", uid="1234"
        )

    def test_changed(self):
        self.user.email = eml = "test@example.com"
        self.assertTrue(self.user.has_email())
        UserSocialAuth.changed(user=self.user)
        db_eml = self.user_model.objects.get(username=self.user.username).email
        self.assertEqual(db_eml, eml)

    def test_set_extra_data(self):
        self.usa.set_extra_data({"a": "b"})
        self.usa.refresh_from_db()
        db_data = UserSocialAuth.objects.get(id=self.usa.id).extra_data
        self.assertEqual(db_data, {"a": "b"})

    def test_disconnect(self):
        m = mock.Mock()
        UserSocialAuth.disconnect(m)
        self.assertListEqual(m.method_calls, [mock.call.delete()])

    def test_username_field(self):
        self.assertEqual(UserSocialAuth.username_field(), "username")
        with mock.patch(
            "social_django.models.UserSocialAuth.user_model",
            return_value=mock.Mock(USERNAME_FIELD="test"),
        ):
            self.assertEqual(UserSocialAuth.username_field(), "test")

    def test_user_exists(self):
        self.assertTrue(UserSocialAuth.user_exists(username=self.user.username))
        self.assertFalse(UserSocialAuth.user_exists(username="test"))

    def test_get_username(self):
        self.assertEqual(UserSocialAuth.get_username(self.user), self.user.username)

    def test_create_user(self):
        # Catch integrity error and find existing user
        UserSocialAuth.create_user(username=self.user.username)

    def test_create_user_reraise(self):
        with self.assertRaises(IntegrityError):
            UserSocialAuth.create_user(username=self.user.username, email=None)
