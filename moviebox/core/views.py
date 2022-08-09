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
        context = {
            "detail_list": response_detail["results"]
        }
        return render(request, self.template_name, context)


class SearchView(View):
    template_name = 'search_result.html'

    def get(self, request, **kwargs):
        #print(dir(request))
        rapid_client = RapidClientMovieMiniData()
        search_input = self.request.GET.get("search")
        query = rapid_client.get_movie_title(search_input)
        search_view = query["results"]

        context = {
            'search_view': search_view

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

    def get(self, request, *args, **kwargs):
        rapid_client = RapidClientMovieMiniData()
        page = kwargs['page']
        rating_list = rapid_client.get_orderby_rating(page)

        rating_list_view_all = rating_list["results"]

        next_page = urlparse(rating_list["links"]["next"]).query
        previous_page = urlparse(rating_list["links"]["previous"]).query

        context = {
            'rating_list_view_all': rating_list_view_all,
            'next_page': f'?{next_page}',
            'previous_page': f'?{previous_page}',

        }

        return render(request, self.template_name, context)


class ViewAllPopular(View):
    template_name = 'view_all_popular.html'

    def get(self, request, *args, **kwargs):
        rapid_client = RapidClientMovieMiniData()
        page = kwargs['page']
        popularity_list = rapid_client.get_orderby_popularity(page)

        popularity_list_view_all = popularity_list["results"]

        next_page = urlparse(popularity_list["links"]["next"]).query

        previous_page = urlparse(popularity_list["links"]["previous"]).query

        context = {
            'popularity_list_view_all': popularity_list_view_all,
            'next_page': f'?{next_page}',
            'previous_page': f'?{previous_page}'

        }
        return render(request, self.template_name, context)

