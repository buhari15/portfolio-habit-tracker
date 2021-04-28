from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404,  redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Count, Q
from datetime import datetime
import datetime


from django.utils import timezone
from .models import HabitTracker, HabitAnalytics
from .forms import (HabitTrackerForm, HabitEditForm,
                    HabitDeleteForm, HabitDoneForm)


def index_page(request):
    """This is the index page"""
    return render(request, "tracker/index.html")


@login_required
def add_habit(request):
    """"Add new habit to the system"""

    if request.method != 'POST':
        """"We return blank form"""
        form = HabitTrackerForm()
    else:
        """"We return the form and process the data"""
        form = HabitTrackerForm(request.POST)
        if form.is_valid():

            create_habit = form.save(commit=False)
            create_habit.created_user = request.user
            create_habit.save()
            return redirect('list')

    context = {
        'form': form,
    }
    return render(request, "tracker/add_habit.html", context)


@login_required
def habit_update(request, pk=None):
    """This function will be use for updating the habit"""
    update_habit = get_object_or_404(HabitTracker, pk=pk)
    if request.method == "POST":
        form = HabitEditForm(request.POST, instance=update_habit)
        if form.is_valid():
            update_habit = form.save(commit=False)
            update_habit.created_by = request.user
            update_habit.save()
            return redirect('list')
    else:
        form = HabitEditForm(instance=update_habit)
    context = {
        'form': form,
        'update_habit': update_habit
    }
    return render(request, 'tracker/habit_update.html', context)


@login_required
def habit_delete(request, pk=None):
    """In case if the habit is not required, it can be deleted
    with this function"""
    habit = get_object_or_404(HabitTracker, pk=pk)
    if request.method == "POST":
        form = HabitDeleteForm(request.POST, instance=habit)
        if form.is_valid():
            habit.delete()
            return redirect('list')
    else:
        form = HabitDeleteForm(instance=habit)

    context = {
        'form': form,
        'habit': habit
    }
    return render(request, 'tracker/delete_habit.html', context)


@login_required
def habit_list(request):
    """With this function all the habit will be displayed"""
    all_habit = HabitTracker.objects.filter(created_user=request.user)
    context = {
        'all_habit': all_habit
    }
    return render(request, 'tracker/habit_list.html', context)


@login_required
def detail_habit(request, pk=None):
    """This function display details of a habit from from the
    habit_list function and dislapy the habit streak"""
    habit_detail = get_object_or_404(HabitTracker, pk=pk)
    check_off = HabitAnalytics.objects.filter(habit_done=True, habit_id=pk).count()

    context = {
        'habit_detail': habit_detail,
        'check_off': check_off
    }
    return render(request, 'tracker/detail.html', context)


@login_required
def setting_views(request):
    """This function display the setting page."""
    return render(request, 'tracker/settings.html')


@login_required
def check_habit(request, pk=None):
    """This function will be use for habit checkoffs
    if user already checked off the habit, the user will be prevented
    to the check the again.
    """
    if request.method != 'POST':
        already_checked = timezone.now() - timezone.timedelta(days=1)
        if HabitAnalytics.objects.filter(done_user=request.user, habit_id=pk,
                                         when_done__gt=already_checked).exists():
            return HttpResponseForbidden('Already Checked Today')
        else:
            form = HabitDoneForm(request.user)
    else:
        form = HabitDoneForm(request.user, request.POST)
        if form.is_valid():
            h_done = form.save(commit=False)
            h_done.done_user = request.user
            h_done.save()
        return redirect('profile')
    context = {
        'form': form,
     }
    return render(request, 'tracker/habit_done_form.html', context)


@login_required
def about_views(request):
    """This function display about page."""

    return render(request, 'tracker/about.html')


