from django.conf import settings
from django.db import models


class CalendarEvent(models.Model):
    calendar = models.ForeignKey(
        'Calendar',
        on_delete=models.CASCADE,
        related_name='events'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    start = models.DateTimeField()
    end = models.DateTimeField()

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='events_created'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    last_edited_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='events_modified'
    )
    last_edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['start']
        verbose_name = 'Calendar Event'
        verbose_name_plural = 'Calendar Events'

    def __str__(self):
        return f"{self.title} ({self.start:%Y-%m-%d %H:%M})"
    