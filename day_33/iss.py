import requests
import smtplib
from datetime import datetime
import time

MY_LAT = -10.4621 # Your latitude
MY_LONG = -92.1221 # Your longitude

my_email=""
password=""

#Your position is within +5 or -5 degrees of the ISS position.
def iss_is_close_to_me():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(iss_latitude)
    print(iss_longitude)
    if (MY_LAT-5<=iss_latitude<=MY_LAT+5) and (MY_LONG-5<=iss_longitude<=MY_LONG+5):
        print("True")
        return True
    else:
        print("False")
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour
    print(time_now)
    if time_now>=sunset or time_now<=sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if iss_is_close_to_me() and is_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:ISS Overhead\n\nISS is now overhead")



