import requests
import datetime as dt
parameters={
    "lat":14.599512,
    "lng":120.984222,
    "formatted":0
}
response=requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

time_now=dt.datetime.now()
print(data)
print(sunrise)
print(sunset)
print(time_now.hour)
