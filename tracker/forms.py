from django import forms
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from .models import HabitTracker, HabitAnalytics
from users.models import User
from datetime import datetime, date
import datetime
from django.utils import timezone

from django.core.exceptions import ValidationError
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class HabitTrackerForm(forms.ModelForm):
    """This class render the form for the creation of habit ."""

    start_habit = forms.DateTimeField(widget=DateTimePicker(
        attrs={
            'input_toggle': True,
            'input_group': False,

        },
    )
    )

    end_habit = forms.DateTimeField(widget=DateTimePicker(
        attrs={
            'input_toggle': True,
            'input_group': False,

        },
    )
    )

    class Meta:
        model = HabitTracker
        fields = ('name', 'reminder_question', 'f_repeat', 'start_habit', 'end_habit')
        labels = {
            'name': _(''),
            'reminder_question': _(''),
            'f_repeat': _('Repeat'),
            'start_habit': _(''),
            'end_habit': _(''),
        }
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Habit Name'}),
            'reminder_question': TextInput(attrs={'placeholder': 'Did you walk with your Dog today?'}),
            # 'reminder_time': forms.TimeInput(attrs={
            #     'class': 'form-control datetimepicker-input',
            #     'data-target': '#datetimepicker1',
            # })

        }


class HabitEditForm(forms.ModelForm):
    """This class is responsible for editing Habit, in case of mistake or change the data Inputed"""

    start_habit = forms.DateTimeField(widget=DateTimePicker(
        attrs={
            'input_toggle': True,
            'input_group': False,

        },
    )
    )

    end_habit = forms.DateTimeField(widget=DateTimePicker(
        attrs={
            'input_toggle': True,
            'input_group': False,

        },
    )
    )

    class Meta:
        model = HabitTracker
        fields = ('name', 'reminder_question', 'f_repeat', 'start_habit', 'end_habit')
        labels = {
            'name': _(''),
            'reminder_question': _(''),
            'f_repeat': _('Repeat'),
            'start_habit': _(''),
            'end_habit': _('')
        }
        labels = {
            'name': _(''),
            'reminder_question': _(''),
            'f_repeat': _('Repeat'),
            'start_habit': _(''),
            'end_habit': _(),

        }

        help_texts = {
            'name': None,
            'reminder_time': None,
            'f_repeat': None,
        }


class HabitDeleteForm(forms.ModelForm):
    """"In case user want to delete his inputed Habit in the system, this class will do the action"""

    class Meta:
        model = HabitTracker
        fields = ('name', 'reminder_question', 'f_repeat', 'start_habit')
        labels = {
            'name': _(''),
            'reminder_question': _(''),
            'f_repeat': _('Repeat'),
            'start_habit': _(''),
        }
        labels = {
            'name': _(''),
            'reminder_question': _(''),
            'f_repeat': _('Repeat'),
            'start_habit': _(''),

        }

        help_texts = {
            'name': None,
            'reminder_time': None,
            'f_repeat': None,
        }


class HabitDoneForm(forms.ModelForm):
    """" This class will render the form, the habit checkoff"""

    class Meta:
        model = HabitAnalytics
        fields = ('habit', 'habit_done')

    def __init__(self, user, *args, **kwargs):
        super(HabitDoneForm, self).__init__(*args, **kwargs)
        self.fields['habit'].queryset = HabitTracker.objects.filter(created_user=user)




















