#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
#Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
#Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
#Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
CITY = input("Syötä kaupunki: ")
API_KEY = "a16abeb973ed3f89951688f7a244be8b"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
try:
    vastaus = requests.get(URL)
    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        lampotila = (json_vastaus["main"]["temp"])
        kuvaus = (json_vastaus["weather"][0]["description"])
        celcius = lampotila - 273.15
        print(f"Kaupungin sää on {kuvaus} ja lämpötila {celcius:.1f} on celsiusta.")
except requests.exceptions.RequestException as e:
    print("Haku ei onnistunut!")