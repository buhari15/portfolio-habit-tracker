from django.test import TestCase

from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model
import pytz
from unittest import mock
from datetime import datetime, date
import datetime


class HabitTrackerModelTest(TestCase):
    def setUp(self):
        freq = HabitFrequency.objects.create(
             name='Daily'
         )

        User = get_user_model()
        user = User.objects.create(
            username='buharikwmbo',
            first_name='markus',
            last_name='joseph',
            email='email@user.com',
            password='foo1468'
        )
        self.habit = HabitTracker.objects.create(
            name='Python Learning',
            reminder_question='Do not forget to Learn learn Python today',
            created_user=user,
            start_habit='2021-03-24 01:00:00',
            end_habit='2021-04-30 02:00:00',
            creation_day='2021-03-24 13:48:52',
            f_repeat=freq
        )

    def test_model_all_labels(self):

        self.assertEqual(f'{self.habit.name}', 'Python Learning')
        self.assertEqual(f'{self.habit.reminder_question}', 'Do not forget to Learn learn Python today')
        self.assertEqual(f'{self.habit.created_user}', 'markus')
        self.assertEqual(f'{self.habit.start_habit}', '2021-03-24 01:00:00')
        self.assertEqual(f'{self.habit.end_habit}', '2021-04-30 02:00:00')
        #self.assertEqual(f'{self.habit.creation_day}', '2021-03-24 13:48:52')
        self.assertEqual(f'{self.habit.f_repeat}', 'Daily')


class HabitAnalyticsModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create(
            username='buharikwmbo',
            first_name='markus',
            last_name='joseph',
            email='email@user.com',
            password='foo1468'
        )
        self.freq = HabitFrequency.objects.create(
            name='Daily'
        )

        self.analytics = HabitTracker.objects.create(
            name='Python Learning',
            reminder_question='Do not forget to Learn learn Python today',
            created_user=user,
            start_habit='2021-03-24 01:00:00',
            end_habit='2021-04-30 02:00:00',
            creation_day='2021-03-24 13:48:52',
            f_repeat=self.freq
        )
        self.analytics_model = HabitAnalytics.objects.create(
            habit=self.analytics,
            habit_done=1,
            when_done='2021-04-30 02:00:00',
            done_user=user
        )

    def test_analytics_models_all(self):
        self.assertEqual(f'{self.analytics_model.habit}', 'Python Learning')
        self.assertEqual(f'{self.analytics_model.habit_done}', '1')
        #self.assertEqual(f'{self.analytics_model.when_done}', '2021-04-30 02:00:00')
        self.assertEqual(f'{self.analytics_model.done_user}', 'markus')






