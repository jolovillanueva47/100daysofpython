import requests,os
from datetime import datetime
from requests.auth import HTTPBasicAuth

APP_ID=os.environ.get("NUTRIONIX_APP_ID")
API_KEY=os.environ.get("NUTRIONIX_API_KEY")

EXERCISE_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT=""

headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
    "x-remote-user-id":"0"
}

data={
    "query":input("Tell me which exercises you did: "),
    "gender":"male",
    "weight_kg":80,
    "height_cm":167.64,
    "age":30
}

response=requests.post(url=EXERCISE_ENDPOINT,json=data,headers=headers)
exercise_data=response.json()["exercises"]
today=datetime.now()
year_today=today.strftime("%Y")
month_today=today.strftime("%m")
day_today=today.strftime("%d")
formatted_date=f"{year_today}/{month_today}/{day_today}"
time_today=today.strftime("%X")

auth_bearer_header={
    "Authorization": ""
}


for exercise in exercise_data:
    exercise_json={
        "workout":{
            "date": formatted_date,
            "time": time_today,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response=requests.post(url=SHEETY_ENDPOINT,json=exercise_json, headers=auth_bearer_header)
    print(response.text)


