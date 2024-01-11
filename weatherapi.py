import datetime as dt
import requests

base_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "412c6fc197bba66aadf429e7e1a835f2"
city = input("Enter City Name: ")

def kel_to_cel_fahren(kelvin):
    celsius = kelvin - 273
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit

url = base_url + 'appid=' + api_key + '&q=' + city
response=requests.get(url).json()

temp_kelvin=response['main']['temp']
temp_celsius, temp_fahrenheit=kel_to_cel_fahren(temp_kelvin)
max_temp=response['main']['temp_max']
tempc,tempf=kel_to_cel_fahren(max_temp)
min_temp=response['main']['temp_min']
temc,temf=kel_to_cel_fahren(min_temp)
humidity=response['main']['humidity']
description=response['weather'][0]['description']
sunrise=dt.datetime.utcfromtimestamp(response['sys']['sunrise']+response['timezone'])
sunset=dt.datetime.utcfromtimestamp(response['sys']['sunset']+response['timezone'])

print(f"\nWeather Details For {city}")
print(f"\nTempertature: {temp_celsius:.2f}'C or {temp_fahrenheit}'F")
print(f"Maximum Tempertature: {tempc:.2f}'C or {tempf}'F")
print(f"Minimum Tempertature: {temc:.2f}'C or {temf}'F")
print(f"Humidity in {city}: {humidity}%")
print(f"General Weather in {city}: {description}")
print(f"Sunrises in {city} at {sunrise}.")
print(f"Sunsets in {city} at {sunset}.\n")

