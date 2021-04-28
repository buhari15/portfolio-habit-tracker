from django.test import TestCase
from django.urls import reverse
import pytest
from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model
import pytz
from unittest import mock
from datetime import datetime, date
import datetime


class UsersTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='buharikwmbo',
            first_name='markus',
            last_name='joseph',
            email='email@user.com',
            password='foo1468'
        )

    def create_user_test(self):
        self.assertEqual(self.user.username, 'buharikwmbo')
        self.assertEqual(self.user.first_name, 'markus')
        self.assertEqual(self.user.last_name, 'joseph')
        self.assertEqual(self.user.email, 'email@user.com')
        self.assertEqual(self.user.password, 'foo1468')

    def create_super_user_test(self):
        pass


class RegistrationTest(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_registration_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'users/register.html')
        self.assertContains(self.response, 'Create an account')








