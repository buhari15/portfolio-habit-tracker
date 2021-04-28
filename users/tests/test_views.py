from django.test import TestCase
from django.urls import reverse, resolve
import pytest
from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model

from users.forms import LoginForm, RegisterForm, ProfileEditForm, UserEditForm
from users.views import register_view, user_login, user_profile, edit_profile, logout_view, user_forget


class RegistrationTest(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_registration_view(self):
        view = resolve('/register')
        self.assertEqual(view.func.__name__, register_view.__name__
                         )


class LoginTest(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_view(self):
        view = resolve('/login')
        self.assertEqual(view.func.__name__, user_login.__name__)


class LogoutTest(TestCase):
    def setUp(self):
        url = reverse('logout')
        self.response = self.client.get(url)

    def test_logout_view(self):
        view = resolve('/logout')
        self.assertEqual(view.func.__name__, logout_view.__name__)


class UserProfileTest(TestCase):
    def setUp(self):
        url = reverse('profile')
        self.response = self.client.get(url)

    def test_profile_view(self):
        view = resolve('/profile')
        self.assertEqual(view.func.__name__, user_profile.__name__)


class EditProfileTest(TestCase):
    def setUp(self):
        url = reverse('edit')
        self.response = self.client.get(url)

    def test_edit_profile(self):
        view = resolve('/edit')
        self.assertEqual(view.func.__name__, edit_profile.__name__)


class ForgetPasswordTest(TestCase):
    pass
