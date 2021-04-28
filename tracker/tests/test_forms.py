from django.test import TestCase

from habittracker.forms import HabitTrackerForm, HabitEditForm
from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model
import pytz
from unittest import mock
from datetime import datetime, date
import datetime

class HabitTrackerFormTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='buharikwmbo',
            first_name='markus',
            last_name='joseph',
            email='email@user.com',
            password='foo1468'
        )
        self.freq = HabitFrequency.objects.create(
            name='Daily'
        )

        self.habit = HabitTracker.objects.create(
            name='Python Testing',
            reminder_question='Do not forget to tests',
            f_repeat=self.freq,
            start_habit='2021-03-24 01:00:00',
            end_habit='2021-04-30 02:00:00',
            created_user=self.user
        )

    def test_form_create_habit(self):
        self.assertEqual(self.habit.name, 'Python Testing')
        self.assertEqual(self.habit.reminder_question, 'Do not forget to tests')
        self.assertEqual(self.freq.name, 'Daily')
        self.assertEqual(self.habit.start_habit, '2021-03-24 01:00:00')
        self.assertEqual(self.habit.end_habit, '2021-04-30 02:00:00')
        self.assertEqual(self.user.username, 'buharikwmbo')




