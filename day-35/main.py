#Note! For the code to work you need to replace all the placeholders with
#Your own details. e.g. account_sid, lat/lon, from/to phone numbers.

import  os
import  requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
api_key="YOUR OWM API KEY"
account_sid ="YOUR ACCOUNT SID"
auth_token = "Your AUTH TOKEN"
WEATHER_PARAMETERS={
    "lat":"YOUR LATITUDE",
    "lon":"YOUR LONGITUDE",
    "appid":api_key,
    "exclude":"current,minutely,daily"
}
response=requests.get("https://api.openweathermap.org/data/2.5/onecall",params=WEATHER_PARAMETERS)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]
will_rain=False
for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain=True
if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today.Remember to bring an umbrella",
        from_='YOUR TWILIO VIRTUAL NUMBER',
        to='YOUR TWILIO REAL NUMBER'
    )
    print(message.status)