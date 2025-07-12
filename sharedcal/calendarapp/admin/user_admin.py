from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from calendarapp.models import CalendarUser


class CalendarUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name') 
    readonly_fields = ('last_login', 'date_joined')


admin.site.register(CalendarUser, CalendarUserAdmin)
