from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

from moviebox.core.rapid_client import RapidClient


def index(request):
    return HttpResponseRedirect(reverse("home"))


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rapid_client = RapidClient()
        response = rapid_client.get_upcoming_movies()
        upcoming_list = response["Movies Upcoming"][:5]
        context["upcoming_list"] = upcoming_list

        return context
