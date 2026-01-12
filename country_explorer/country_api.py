import requests

class CountryAPI:
    BASE_URL = "https://restcountries.com/v3.1"

    def get_country_by_name(self, name):
        url = f"{self.BASE_URL}/name/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        return None

    def get_countries_by_region(self, region):
        url = f"{self.BASE_URL}/region/{region}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json()
        return None
