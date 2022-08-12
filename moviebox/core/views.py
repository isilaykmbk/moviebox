import json

import ipdb
import requests
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from moviebox.core.rapid_client import RapidClientMovieMiniData
from urllib.parse import urlparse


def index(request):
    return HttpResponseRedirect(reverse("home"))


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        rapid_client = RapidClientMovieMiniData()
        search_input = self.request.GET.get("search")
        query = rapid_client.get_movie_title(search_input)

        search_view = query["results"]

        paginator = Paginator(search_view, 20)

        page_num = request.GET.get('page', 1)

        page = paginator.page(page_num)

        context = {
            'page': page,
            'search': search_input,

        }
        return render(request, self.template_name, context)


class GenreView(View):
    template_name = 'genre.html'

    def get(self, request, *args, **kwargs):
        rapid_client = RapidClientMovieMiniData()
        page_num = self.request.GET.get('page')

        genre_response = rapid_client.get_movie_genre(kwargs['category'], f'?page={page_num}')

        genre_list = genre_response['results']

        next_page = urlparse(genre_response["links"]["next"]).query
        previous_page = urlparse(genre_response["links"]["previous"]).query

        if previous_page == '':
            previous_page = 'page=1'

        context = {
            "genre_list": genre_list,
            'next_page': f'?{next_page}',
            'previous_page': f'?{previous_page}',
            'category': kwargs['category']
        }
        return render(request, self.template_name, context)


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

