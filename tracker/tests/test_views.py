from django.test import TestCase
from django.urls import reverse, resolve
import pytest
from habittracker.models import HabitTracker, HabitAnalytics, HabitFrequency

from django.contrib.auth import get_user_model
from django.test import Client

from habittracker.views import (
        index_page, add_habit, habit_update, habit_delete, habit_list, detail_habit, setting_views,
        check_habit, about_views

)


class IndexPageTest(TestCase):
    def setUp(self):
        url = reverse('index_page')
        self.response = self.client.get(url)

    def test_registration_view(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, index_page.__name__
                         )


class AddHabitTest(TestCase):
    def setUp(self):
        url = reverse('add_habit')
        self.response = self.client.get(url)

    def test_login_view(self):
        view = resolve('/add')
        self.assertEqual(view.func.__name__, add_habit.__name__)


class HabitUpdateTest(TestCase):
    def setUp(self):

        url = reverse('habit_update', args=[5])
        self.response = self.client.get(url)
        # Redirect test to be added

    def test_update_view(self):

        view = resolve('/update/5/')
        self.assertEqual(view.func.__name__, habit_update.__name__
                         )


class HabitDeleteTest(TestCase):
    def setUp(self):
        url = reverse('habit_delete', args=[5])
        self.response = self.client.get(url)

    def test_profile_view(self):
        view = resolve('/delete/5/')
        self.assertEqual(view.func.__name__, habit_delete.__name__)


class HabitDetailTest(TestCase):
    def setUp(self):
        url = reverse('habit_delete', args=[5])
        self.response = self.client.get(url)

    def test_habit_details_view(self):
        view = resolve('/detail/5/')
        self.assertEqual(view.func.__name__, detail_habit.__name__)


# class HabitListTest(TestCase):
#     def setUp(self):
#         url = reverse('list')
#         self.response = self.client.get(url)
#
#     def test_list_view(self):
#         view = resolve('/list')
#         self.assertEqual(view.func.__name__, habit_list.__name__)
#
# #
# # class HabitCheckedTest(TestCase):
# #     def setUp(self):
# #         url = reverse('check_habit', args=[5])
# #         self.response = self.client.get(url)
# #
# #     def test_habit_details_view(self):
# #         view = resolve('/done/5/')
# #         self.assertEqual(view.func.__name__, check_habit.__name__)


class HabitSettingPageTest(TestCase):
    def setUp(self):
        url = reverse('settings')
        self.response = self.client.get(url)

    def test_habit_details_view(self):
        view = resolve('/settings')
        self.assertEqual(view.func.__name__, setting_views.__name__)


class HabitAboutPageTest(TestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_habit_about_view(self):
        view = resolve('/about')
        self.assertEqual(view.func.__name__, about_views.__name__)

