import requests as requests

pyynto = "https://api.chucknorris.io/jokes/random"

vastaus = requests.get(pyynto)
if vastaus.ok:
    vastaus_json = vastaus.json()
    print(vastaus_json['value'])

else:
    print("Haku epäonnistui. ")

