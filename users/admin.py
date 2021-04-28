from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import RegisterForm, LoginForm
from .models import User, Profile



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo')

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form = RegisterForm
    class Meta:
        model = Profile
        fields = ('user', 'date_of_birth', 'photo')
    list_display = ('username',
                    'first_name', 'last_name', 'email', 'is_admin', 'is_demo', 'is_user')
    list_filter = ('is_admin',)

    fieldsets = (
                                (None, {'fields': ('username', 'email','password')}),
                                ('Permissions', {'fields': ('is_admin','is_demo','is_user',)})
                )
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',  'first_name', 'last_name', 'email')
    filter_horizontal = ()


admin.site.unregister(Group)

