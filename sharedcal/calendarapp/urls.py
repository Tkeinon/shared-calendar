from django.urls import path
from calendarapp.views import register_view


urlpatterns = [
    path('register_user/', register_view.register_user, name='register_user'),
]