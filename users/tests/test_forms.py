from django.test import TestCase
from django.urls import reverse
import pytest
from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model

from users.forms import LoginForm, RegisterForm, ProfileEditForm, UserEditForm, EventEditForm


class RegistrationTest(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_registration_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, RegisterForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')


class LoginTestForm(TestCase):
    def setUp(self):
        url = reverse('login')
        self.response = self.client.get(url)

    def test_login_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, LoginForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')



