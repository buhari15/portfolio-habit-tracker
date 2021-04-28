from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.contrib.auth import login, get_user_model, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.http import require_http_methods


from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Count, Max, Q, Case, When, BooleanField, Sum

from tracker.models import HabitTracker, HabitAnalytics
from tracker.forms import HabitTrackerForm, HabitEditForm, HabitDeleteForm

from .models import Profile
from django.contrib import messages

from .forms import LoginForm, RegisterForm, ProfileEditForm, UserEditForm


def register(request, *args, **kwargs):
    """"Registration view, this function will display
        the registration form to the user"""
    user_form = RegisterForm(request.POST or None)
    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.save()
        return render(request, 'users/registration_done.html', {'new_user': new_user})
    else:
        user_form = RegisterForm()
    return render(request, "users/register.html", {'user_form': user_form})


def user_login(request, *args, **kwargs):
    """"Login view, this function will display
    the login form to the user"""
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        return HttpResponseRedirect('/profile')

    context = {
        'form': LoginForm()

    }
    return render(request, "users/login.html", context)


@login_required
def user_profile(request, pk=None, *args, **kwargs):
    """"User Profile view, this function will display
        the User Dashboard"""

    check_on = HabitAnalytics.objects.values_list('habit__name').filter(habit_done=True, done_user=request.user). \
        annotate(checked_count=Count('habit'))
    queryset = HabitAnalytics.objects.filter(done_user=request.user, habit_done=1).aggregate(Count('habit_id'))
    habit_daily = HabitTracker.objects.filter(created_user=request.user, f_repeat_id=1)
    habit_weekly = HabitTracker.objects.filter(created_user=request.user, f_repeat_id=2)
    habit_monthly = HabitTracker.objects.filter(created_user=request.user, f_repeat_id=3)
    habit_yearly = HabitTracker.objects.filter(created_user=request.user, f_repeat_id=4)
    all_habit_profile = HabitTracker.objects.filter(created_user=request.user)

    context = {
        'habit_daily': habit_daily,
        'habit_weekly': habit_weekly,
        'habit_monthly': habit_monthly,
        'habit_yearly': habit_yearly,
        'queryset': queryset,
        'all_habit_profile': all_habit_profile,
        'check_on': check_on,


    }

    return render(request, "users/profile.html",  context)



@login_required
def edit_profile(request, *args, **kwargs):
    profile = Profile(user=request.user)
    form_user = UserEditForm(instance=request.user, data=request.POST)
    form_profile = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
    if form_user.is_valid() and form_profile.is_valid():
        form_user.save()
        form_profile.save()
        messages.success(request, 'Profile Updated' \
                                  'successfully')

    else:
        messages.error(request, 'Error Updating your profile')
        form_user = UserEditForm(instance=request.user)
        form_profile = ProfileEditForm(instance=request.user.profile)

    return render(request, "users/profile_edit.html", {'form_user': form_user, 'form_profile': form_profile})



def user_forget(request):
    return render(request, 'users/password_reset_form.html')


def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html')
