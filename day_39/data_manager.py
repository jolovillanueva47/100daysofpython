import requests
from pprint import pprint


SHEETY_ENDPOINT="https://api.sheety.co/98cccb71ad2bb34e2f75d224cdde7163/flightDeals/prices"


auth_headers={
    "Authorization": "Bearer qwertyasdf"
}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data={}
    
    def get_data(self):
        response=requests.get(SHEETY_ENDPOINT,headers=auth_headers)
        self.data=response.json()
        return self.data
        
    def update(self,id,body):
        endpoint_update=f"{SHEETY_ENDPOINT}/{id}"
        response=requests.put(endpoint_update,json=body,headers=auth_headers)
        response.raise_for_status()
        print(response.text)
