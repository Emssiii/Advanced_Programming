import tkinter as tk
from tkinter import ttk
from country_api import CountryAPI
from country import Country
from PIL import Image, ImageTk
import requests
from io import BytesIO


class CountryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Country Explorer")
        self.root.geometry("500x600")
        self.root.resizable(False, False)

        self.api = CountryAPI()

        self.create_widgets()

    def create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="Country Explorer",
            font=("Arial", 18, "bold")
        )
        title.pack(pady=10)

        # Search frame
        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=10)

        self.country_entry = tk.Entry(search_frame, width=25)
        self.country_entry.pack(side=tk.LEFT, padx=5)

        search_button = tk.Button(
            search_frame,
            text="Search",
            command=self.search_country
        )
        search_button.pack(side=tk.LEFT)

        # Info display
        self.info_label = tk.Label(
            self.root,
            text="Enter a country name and click Search",
            justify=tk.LEFT,
            wraplength=450
        )
        self.info_label.pack(pady=10)

        # Flag placeholder
        self.flag_label = tk.Label(self.root)
        self.flag_label.pack(pady=10)

    def load_flag_image(self, url):
        try:
            response = requests.get(url)
            image_data = response.content

            image = Image.open(BytesIO(image_data))
            image = image.resize((160, 100))

            self.flag_image = ImageTk.PhotoImage(image)
            self.flag_label.config(image=self.flag_image, text="")

        except Exception:
            self.flag_label.config(text="Flag not available", image="")

    def search_country(self):
        country_name = self.country_entry.get().strip()

        if not country_name:
            self.info_label.config(text="Please enter a country name.")
            return

        data = self.api.get_country_by_name(country_name)

        if not data:
            self.info_label.config(text="Country not found.")
            return

        country_data = data[0]

        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["N/A"])[0]
        population = country_data.get("population", 0)
        region = country_data.get("region", "N/A")

        currencies = ", ".join(
            currency["name"]
            for currency in country_data.get("currencies", {}).values()
        ) or "N/A"

        languages = ", ".join(
            country_data.get("languages", {}).values()
        ) or "N/A"

        flag_url = country_data["flags"]["png"]

        country = Country(
            name,
            capital,
            population,
            region,
            currencies,
            languages,
            flag_url
        )

        self.load_flag_image(flag_url)
        self.info_label.config(text=country.get_summary())


if __name__ == "__main__":
    root = tk.Tk()
    app = CountryApp(root)
    root.mainloop()
