class Country:
    def __init__(self, name, capital, population, region, currencies, languages, flag_url):
        self.name = name
        self.capital = capital
        self.population = population
        self.region = region
        self.currencies = currencies
        self.languages = languages
        self.flag_url = flag_url

    def get_summary(self):
        return (
            f"Name: {self.name}\n"
            f"Capital: {self.capital}\n"
            f"Region: {self.region}\n"
            f"Population: {self.population:,}\n"
            f"Currencies: {self.currencies}\n"
            f"Languages: {self.languages}"
        )
