from django.db import models
from django.conf import settings

class Calendar(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
        related_name='edited_calendars'
    )

    class Meta:
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendars'

class CalendarSharePerm(models.Model):
    """
    Model determines what invited users can do with the calendar.

    Invited user can always see the calendar and it does not need it's 
    own permission
    """
    calendar = models.ForeignKey(
        Calendar,
        on_delete=models.CASCADE,
        related_name='share_perms'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shared_calendars'
    )

    can_edit_events = models.BooleanField(default=False)
    can_remove_events = models.BooleanField(default=False)
    can_edit_calendar = models.BooleanField(default=False)
    can_invite_users = models.BooleanField(default=False)

    invited_at = models.DateTimeField(auto_now_add=True)
    invited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='calendar_invites_sent'
    )

    edited_at = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, 
        blank=True,
        related_name='calendar_perms_edited'
    )
    
    class Meta:
        unique_together = ('calendar', 'user')  # Avoid giving multiple perms for same calendar
        verbose_name = 'Calendar share and permission'
        verbose_name_plural = 'Calendar shares and permissions'

    def __str__(self):
        return f'{self.user} permissions to {self.calendar}'
    