"""habittracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from users.views import (
        user_login, user_profile, register, user_forget,
        edit_profile, logout_view,

)

from tracker.views import (
    index_page,
    setting_views, about_views, add_habit, habit_update, habit_delete,
    detail_habit, habit_list, check_habit

)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Users app
    path('', index_page, name='index_page'),
    path('register/', register, name='register'),
    path('login', user_login, name='login'),
    path('logout', logout_view, name='logout'),
    path('profile', user_profile, name='profile'),
    path('forget', user_forget, name='forget'),

    # Habit Tracker app
    path('add', add_habit, name='add_habit'),
    path('list', habit_list, name='list'),
    path('detail/<int:pk>/', detail_habit, name='detail_habit'),
    path('done/<int:pk>/', check_habit, name='check_habit'),
    path('edit', edit_profile, name='edit'),
    path('update/<int:pk>/', habit_update, name='habit_update'),
    path('delete/<int:pk>/', habit_delete, name='habit_delete'),
    path('about', about_views, name='about'),
    path('settings', setting_views, name='settings'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
