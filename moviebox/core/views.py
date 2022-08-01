import requests
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from moviebox.core.rapid_client import RapidClientMovieMiniData
from moviebox.core.rapid_client import RapidClientMovieData
from urllib.parse import urlparse


def index(request):
    return HttpResponseRedirect(reverse("home"))


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # upcoming movies
        rapid_client_upmovie = RapidClientMovieData()

        response = rapid_client_upmovie.get_upcoming_movie()
        upcoming_list = response["results"][:5]
        context["upcoming_list"] = upcoming_list

        # top rating and popular movies
        rapid_client = RapidClientMovieMiniData()

        response = rapid_client.get_orderby_popularity()
        popularity_list = response["results"][:5]
        context["popularity_list"] = popularity_list

        response = rapid_client.get_orderby_rating()
        rating_list = response["results"][:5]
        context["rating_list"] = rating_list

        return context


class MovieDetails(View):
    template_name = 'movie_details.html'

    def get(self, request, *args, **kwargs):
        rapid_client = RapidClientMovieMiniData()

        response_detail = rapid_client.get_movie_details(kwargs['id'])
        import ipdb; ipdb.set_trace()
        context = {
            "detail_list": response_detail["results"]
        }
        return render(request, self.template_name, context)


class ViewAllUpcoming(TemplateView):
    template_name = 'view_all_upcoming.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rapid_client = RapidClientMovieData()
        response_view_upcoming = rapid_client.get_upcoming_movie()
        view_all_upcoming = response_view_upcoming["results"][:15]
        context["view_all_upcoming"] = view_all_upcoming

        return context


class ViewAllRating(View):
    template_name = 'view_all_rating.html'

    def get(self, request):
        rapid_client = RapidClientMovieMiniData()
        rating_list = rapid_client.get_orderby_rating()

        context = {
            'next_link': rating_list["links"]["next"],
            'previous_link': rating_list["links"]["previous"]
        }

        obj = urlparse(context['next_link'])

        return render(request, self.template_name, context)


class ViewAllPopular(View):
    template_name = 'view_all_popular.html'

    def get(self, request):
        rapid_client = RapidClientMovieMiniData()
        response_view_popular = rapid_client.get_orderby_popularity()
        context = {
            "view_all_popular": response_view_popular["results"][:15]
        }
        return render(request, self.template_name, context)

