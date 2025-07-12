from django.contrib.auth.models import AbstractUser


class CalendarUser(AbstractUser):
    def __str__(self):
        return self.username