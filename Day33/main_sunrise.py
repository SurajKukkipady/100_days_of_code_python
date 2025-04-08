# This is a simple program to get the sunrise and sunset times for a given latitude
# and longitude using the Sunrise-Sunset API.

import requests
from datetime import datetime

MY_LAT = '28.704060'
MY_LNG = '77.102493'

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data['results']['sunrise']
sunset = data['results']['sunset']

print(sunrise.split('T')[1].split(':')[0])  #In UTC
print(sunset.split('T')[1].split(':')[0])

time_now = datetime.now()
print(time_now.hour)
