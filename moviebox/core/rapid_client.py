import requests
import json

from moviebox import settings


class RapidClientMovieData:
    API_URL = "https://moviesdatabase.p.rapidapi.com"

    def __init__(self):
        self.headers = {
            'x-rapidapi-key': settings.RAPIDAPI_KEY,
            'x-rapidapi-host': settings.RAPIDAPI_HOST2
        }

    def get(self, endpoint_url):
        response = requests.get(
            endpoint_url,
            headers=self.headers,
        )

        return json.loads(response.text)

    def get_upcoming_movie(self):
        endpoint_url = f"{self.API_URL}/titles/x/upcoming"
        return self.get(endpoint_url)


class RapidClientMovieMiniData:
    API_URL = "https://moviesminidatabase.p.rapidapi.com"

    def __init__(self):
        self.headers = {
            'x-rapidapi-key': settings.RAPIDAPI_KEY,
            'x-rapidapi-host': settings.RAPIDAPI_HOST
        }

    def get(self, endpoint_url, params=None):
        response = requests.get(
            endpoint_url,
            headers=self.headers,
            params=params
        )

        return json.loads(response.text)

    def get_orderby_popularity(self, page='?page=1'):
        if page == '?page=1':
            endpoint_url = f"{self.API_URL}/movie/order/byPopularity/"
        else:
            endpoint_url = f"{self.API_URL}/movie/order/byPopularity/"
        return self.get(endpoint_url, {"page": 1, "page_size": 10},)

    def get_orderby_rating(self, page='?page=1'):
        if page == '?page=1':
            endpoint_url = f"{self.API_URL}/movie/order/byRating/"
        else:
            endpoint_url = f"{self.API_URL}/movie/order/byRating/{page}"
        return self.get(endpoint_url)

    def get_movie_details(self, movie_id):
        endpoint_url = f"{self.API_URL}/movie/id/{movie_id}/"
        return self.get(endpoint_url)

    def get_movie_title(self, search):
        endpoint_url = f"{self.API_URL}/movie/imdb_id/byTitle/{search}/"
        return self.get(endpoint_url)
