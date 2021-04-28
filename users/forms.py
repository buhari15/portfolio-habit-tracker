from django.contrib.auth import get_user_model
from django.db.models import Q
from django import forms
from django.forms import ModelForm, TextInput
from django.utils.translation import gettext_lazy as _

from tracker.models import HabitTracker
from .models import Profile, User

User = get_user_model()


class RegisterForm(forms.ModelForm):
    """This class will create the form to be displayed for the
     user to register in the application."""
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

        widgets = {
                'username': TextInput(attrs={'placeholder': 'Username'}),
                'first_name': TextInput(attrs={'placeholder': 'First Name'}),
                'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
                'email': TextInput(attrs={'placeholder': 'Email'}),
        }

        labels = {
            'username': _(''),
            'first_name': _(''),
            'last_name': _(''),
            'email': _(''),
        }
        help_texts = {
            'username': None,
        }

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 != password2:
            raise forms.ValidationError("Password do not match")
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """" The login class will render the form to the user, it is
    beautifully rendered with form crispy"""
    query = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
                Q(username__iexact=query) |
                Q(email__iexact=query)
            ).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("Invalid Credentials or User does no exists")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Credentials are not correct")
        self.cleaned_data["user_obj"] = user_obj
        return super(LoginForm, self).clean(*args, **kwargs)


class UserEditForm(forms.ModelForm):
    """docstring for ProfileEditForm."""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
                'username': TextInput(attrs={'placeholder': 'Username'}),
                'first_name': TextInput(attrs={'placeholder': 'First Name'}),
                'last_name': TextInput(attrs={'placeholder': 'Last Name'}),
                'email': TextInput(attrs={'placeholder': 'Email'}),
        }

        labels = {
            'username': _(''),
            'first_name': _(''),
            'last_name': _(''),
            'email': _(''),
        }
        help_texts = {
            'username': None,
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

        widgets = {
                'date_of_birth': TextInput(attrs={'placeholder': 'YYYY/MM/DD'}),

        }



