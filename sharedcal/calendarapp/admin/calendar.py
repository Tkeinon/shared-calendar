from django.contrib import admin

from calendarapp.models import Calendar, CalendarSharePerm


class CalendarSharePermAdmin(admin.ModelAdmin):
    list_display = (
        'calendar', 
        'user',
        'can_edit_events',
        'can_remove_events',
        'can_edit_calendar',
        'can_invite_users',
    )
    list_filter = (
        'can_edit_calendar',
        'can_edit_events',
        'can_invite_users',
        'can_remove_events',
        'invited_at',
    )
    search_fields = (
        'calendar__name',
        'user__email',
        'user__username',
        'invited_by__email',
        'edited_by__email'
    )
    autocomplete_fields = ('calendar', 'user', 'invited_by', 'edited_by')
    readonly_fields = ('invited_at', 'edited_at')

class CalendarSharePermInline(admin.TabularInline):
    model = CalendarSharePerm
    extra = 1
    autocomplete_fields = ('user', 'invited_by', 'edited_by')
    readonly_fields = ('invited_at', 'edited_at')
    fields = (
        'user',
        'can_edit_events',
        'can_remove_events',
        'can_edit_calendar',
        'can_invite_users',
        'invited_by',
        'edited_by', 
        'invited_at',
        'edited_at'
    )


class CalendarAdmin(admin.ModelAdmin):
    inlines = [CalendarSharePermInline]
    list_display = ('name', 'owner', 'created_at') 
    list_filter = ('created_at',)
    search_fields = ('name', 'owner__email', 'owner__username')
    autocomplete_fields = ('owner', 'edited_by')
    readonly_fields = ('created_at', 'last_edited')


admin.site.register(Calendar, CalendarAdmin)
admin.site.register(CalendarSharePerm, CalendarSharePermAdmin)
