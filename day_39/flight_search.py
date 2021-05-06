import requests
from pprint import pprint
from datetime import datetime,timedelta

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_SEARCH_ENDPOINT="https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = "Bng1kCvE9Y35ZizmmcbFIMVFwvWhYB_z"

auth_header={
            "apikey": TEQUILA_API_KEY
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
    def get_iata_code(self,city): 
        data={"term":city}
        response = requests.get(TEQUILA_ENDPOINT,params=data,headers=auth_header)
        response.raise_for_status()
        result=response.json()["locations"][0]
        iata_code=result["code"]
        return iata_code
    def search_flight(self,city):
        now=datetime.now()
        tomorrow=datetime.now()+timedelta(days=1)
        six_months_from_tomorrow=tomorrow+timedelta(days=180)
        print(tomorrow.strftime("%d/%m/%Y"))
        print(six_months_from_tomorrow.strftime("%d/%m/%Y"))
        data={
            "fly_from":"LON",
            "fly_to":city,
            "date_from":tomorrow.strftime("%d/%m/%Y"),
            "date_to":six_months_from_tomorrow.strftime("%d/%m/%Y"),
            "night_in_dst_from":7,
            "night_in_dst_to":28,
            "fly_type":"round",
            "curr":"GBP"
        }
        response=requests.get(TEQUILA_SEARCH_ENDPOINT,params=data,headers=auth_header)
        response.raise_for_status()
        print(response.json())
test=FlightSearch()
test.search_flight("PAR")