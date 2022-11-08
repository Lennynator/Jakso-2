import requests as requests


hakusana = input("Anna hakusana: ")
pyynto = "https://api.openweathermap.org/data/2.5/weather?q="+hakusana+"&appid=a78225eb4f8ef18db043775eb8ff9ad4&units=metric"
vastaus = requests.get(pyynto)
if vastaus.ok:
    vastaus_json = vastaus.json()
    print(vastaus_json['weather'])
    print(vastaus_json['main'])

else:
    print("Haku epäonnistui. ")