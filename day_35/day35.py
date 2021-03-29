import requests
import os
from twilio.rest import Client

api_key=os.environ.get("OWM_API_KEY")
account_sid = "AC67ae3cf0843b0ea8ebc3641014efb472"
auth_token =os.environ.get("TWILIO_AUTH_TOKEN")


parameters={
    "lat":13.755130,
    "lon":121.069338,
    "appid":api_key,
    "exclude":"current,minutely,daily"
}


response=requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data=response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
slice_num=slice(0,12)
weather_data_12hrs=weather_data["hourly"][slice_num]

weather_codes=[]
for data in weather_data_12hrs:
    temp_list=[]
    for item in data["weather"]:
        temp_list.append(item["id"])
    weather_codes.append(temp_list)
    temp_list=[]

test=[300]
weather_codes.append(test)
will_rain=False
for data in weather_codes:
    for item in data:
        if int(item) < 700:
            will_rain=True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_="",
    to="",
    body="It is going to rain today. Bring an umbrella ☂️")
    print(message.status)
else:
    print("It will not rain")

