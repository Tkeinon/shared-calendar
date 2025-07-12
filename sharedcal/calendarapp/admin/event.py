from django.contrib import admin
from calendarapp.models import CalendarEvent


class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'calendar', 'start', 'end', 'created_by')
    list_filter = ('calendar', 'start')
    search_fields = ('title', 'description', 'location')
    autocomplete_fields = ('calendar', 'created_by', 'last_edited_by')
    readonly_fields = ('created_at', 'last_edited_at')

admin.site.register(CalendarEvent, CalendarEventAdmin)