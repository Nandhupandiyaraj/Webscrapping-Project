import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os

url = "https://en.wikipedia.org/wiki/ASEAN"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table",class_="sortable wikitable plainrowheaders")

cities = []
for row in table.find_all("tr"):
    ths = row.find_all("th")
    if len(ths) > 1:
        city_name = ths[1].find("a").text.strip()
        cities.append(city_name)

countries = []
for row in table.find_all("tr"):
    td = row.find_all("td")
    if len(td) > 2:
      country_name = td[2].find("a").text.strip()
      countries.append(country_name)

country_population = []
for row in table.find_all("tr"):
    tds = row.find_all("td")
    if len(tds) > 0:
        population = tds[0].text.strip()
        country_population.append(population)

City_Area = []
for row in table.find_all("tr"):
    tds = row.find_all("td")
    if len(tds) > 1:
        Area = tds[1].text.strip()
        City_Area.append(Area)


countries_dictionary = {
    "Core city": [city for city in cities if city != "Core city"],
    "Country": countries,
    "Population": country_population,
    "Area": City_Area,
    "Population_Density": [float(population.replace(",", "")) / float(area.replace(",", ""))
                        for population, area in zip(country_population, City_Area)]
}

df = pd.DataFrame(countries_dictionary)

print(df)
