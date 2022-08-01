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

    def get(self, endpoint_url):
        response = requests.get(
            endpoint_url,
            headers=self.headers,
        )

        return json.loads(response.text)

    def get_orderby_popularity(self):
        endpoint_url = f"{self.API_URL}/movie/order/byPopularity/"
        return self.get(endpoint_url)

    def get_orderby_rating(self):
        endpoint_url = f"{self.API_URL}/movie/order/byRating/"
        return self.get(endpoint_url)

    def get_movie_details(self, movie_id):
        endpoint_url = f"{self.API_URL}/movie/id/{movie_id}/"
        return self.get(endpoint_url)
