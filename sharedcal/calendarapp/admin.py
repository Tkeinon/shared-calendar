from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CalendarUser


class CalendarUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name') 


admin.site.register(CalendarUser, CalendarUserAdmin)