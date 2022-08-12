import requests
import json

from moviebox import settings


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
            endpoint_url = f"{self.API_URL}/movie/order/byPopularity/{page}"
        return self.get(endpoint_url)

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

    def get_movie_genre(self, category, page='?page=1'):
        if page == '?page=1':
            endpoint_url = f"{self.API_URL}/movie/byGen/{category}/"
        else:
            endpoint_url = f"{self.API_URL}/movie/byGen/{category}/{page}"

        return self.get(endpoint_url)
