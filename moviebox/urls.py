from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from moviebox.core import views


urlpatterns = [
    path('', include('moviebox.core.urls')),
]