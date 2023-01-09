#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
#Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
#Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests

request = "https://api.chucknorris.io/jokes/random"

try:
    answer = requests.get(request)
    if answer.status_code == 200:
        json_answer = answer.json()
        print(json_answer["value"])
    elif answer.status_code == 404:
        print("Yhteys onnistui, mutta osoitetta ei löydy palvelimelta")
    else:
        print(f"Yhteys onnistui, mutta joku virhekoodi: {answer.status_code}")
except requests.exceptions.RequestException as e:
    print("Invalid request: " + str(e))