from django.db import models
from datetime import datetime, date

from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.conf import settings

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


class HabitFrequency(models.Model):
    """This class handle the creation of the occurrence
    i.e. daily, weekly, monthly to the system"""
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Habit Frequencies"

    def __str__(self):
        return self.name


class HabitTracker(models.Model):
    """This class will handle the habit creation,
    deletion, update etc."""
    name = models.CharField(max_length=250)
    reminder_question = models.CharField(max_length=250)
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_user')
    start_habit = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_habit = models.DateTimeField(auto_now=False, auto_now_add=False)
    creation_day = models.DateTimeField(_("Created on"), auto_now_add=True)
    f_repeat = models.ForeignKey('HabitFrequency', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Habit Tracker"

    def __str__(self):
        return str(self.name) if self.name else ''


class HabitAnalytics(models.Model):
    """This is the analytic model, in this class
    the habit analytics will be done.
     taking track of the habit that is done, and the undone habit"""
    HABIT_DONE = 1
    HABIT_NOT_DONE = 0
    HABIT_CHOICES = ((HABIT_DONE, 'Yes'),
                     (HABIT_NOT_DONE,  'No'))

    habit = models.ForeignKey('HabitTracker', on_delete=models.CASCADE)
    habit_done = models.IntegerField(_("Done"), choices=HABIT_CHOICES, default=HABIT_NOT_DONE, blank=True, null=True)
    when_done = models.DateTimeField(blank=True,  null=True, auto_now=True, auto_now_add=False)
    done_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='done_user')

    class Meta:
        verbose_name_plural = "Habit Analytics"

    def __str__(self):
        return str(self.habit) if self.habit else ''











from django.db import models

# Create your models here.
