from django import template
from ..models import HabitTracker, HabitAnalytics
import datetime
from django.shortcuts import render, get_object_or_404

from django.db.models import Count, Q, Case, When, Max, Sum
from django.utils import timezone
from datetime import datetime, timedelta

from itertools import chain
register = template.Library()


@register.simple_tag()
def get_streak():
    d = HabitAnalytics.objects.filter(done_user=1,  habit_done=1).values('habit').annotate(score=Sum('habit_done')).order_by('score')
    return d


@register.simple_tag
def testing_d(pk=None):
    #habit_daily = HabitTracker.objects.filter(f_repeat_id=1)
    check_off = HabitAnalytics.objects.filter(habit_done=True, done_user=2).annotate(Count('habit'), Count('habit_done'))

    return check_off
    #return list(chain(habit_daily, habit_done_daily))

@register.simple_tag
def get_result():
    now = timezone.now()
    habit_time = now - timedelta(hours=2)
    return habit_time



@register.simple_tag
def total_habit_done():
    done = HabitAnalytics.objects.filter(habit_done=True).count()
    return f' {done} Days'


@register.simple_tag
def total_habit_not_done():
    return HabitAnalytics.objects.filter(habit_done=False).count()



@register.simple_tag
def habit_streak(f_repeat=None):
    dataset = HabitAnalytics.objects \
        .values('when_done').filter(done_user=2) \
        .annotate(when_count=Count('when_done', filter=Q(habit_done=1)),
                  not_when_done_count=Count('when_done', filter=Q(habit_done=False))) \
        .order_by('when_done')

    return f'Testing the visualization: {dataset} '

@register.simple_tag
def new_count(pk=None):
    return HabitAnalytics.objects.filter(habit_done=True, habit_id=pk).count()









