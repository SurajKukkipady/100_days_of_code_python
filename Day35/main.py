import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = 'bd5e378503939ddaee76f12ad7a97608'
account_sid = 'TWILIO_ACCOUNT_SID'
auth_token = 'TWILIO_AUTH_TOKEN'

weather_parameters = {
    "lat": 12.971599,
    "lon": 77.594566,
    "appid": API_KEY,
    "cnt": 4,
}

response = requests.get(
    url=OWN_Endpoint,
    params=weather_parameters
)
response.raise_for_status()
weather_data = response.json()

weather_ids = [item['weather'][0]['id'] for item in weather_data['list']]

if any(id < 700 for id in weather_ids):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+17632474113',
        body='Hi from twilio, get your umbrella☔☔',
        to='+918660153482'
    )
    print(message.status)


