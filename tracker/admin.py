from django.contrib import admin

from django.contrib.auth.models import Group

from .forms import HabitTrackerForm
from .models import HabitTracker, HabitFrequency, HabitAnalytics

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportMixin, ImportExportMixin



class HabitResources(resources.ModelResource):

    class Meta:
        model = HabitAnalytics
        # skip_unchanged = False
        # report_skipped = False
        # dry_run = True
        # exclude = ('id', 'habit', 'habit_done', 'when_done', '')

@admin.register(HabitFrequency)
class HabitFrequencyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


class HabitVisualisationInline(admin.TabularInline):
    model = HabitAnalytics


@admin.register(HabitTracker)
class HabitTrackerAdmin(admin.ModelAdmin):
    list_display = ('habit', 'habit_done', 'when_done', 'done_user')
    inlines = [
        HabitVisualisationInline,

    ]
    add_form = HabitTrackerForm
    list_display = ('name', 'reminder_question', 'start_habit', 'end_habit', 'f_repeat', 'creation_day', 'created_user')
    list_filter = ('name',)

    search_fields = ('name', 'reminder_question', 'f_repeat')
    ordering = ('name', 'reminder_question', 'f_repeat')
    filter_horizontal = ()

@admin.register(HabitAnalytics)
class AnalyticsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = HabitResources
    list_display = ('habit', 'habit_done', 'when_done', 'done_user')
    list_filter = ('habit', 'done_user', 'habit_done')





