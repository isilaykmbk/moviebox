from django.urls import path

from moviebox.core.views import index, DashboardView

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', DashboardView.as_view(), name='home'),
]