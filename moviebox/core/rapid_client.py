import requests
import json

from moviebox import settings


class RapidClient:
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

    def get_upcoming_movies(self):
        endpoint_url = f"{self.API_URL}/movie/order/upcoming/"
        return self.get(endpoint_url)
