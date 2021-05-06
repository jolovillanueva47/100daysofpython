#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data=data_manager.get_data()
flight_search=FlightSearch()
for data in sheet_data["prices"]:
    code=flight_search.get_iata_code(data["city"])
    data["iataCode"]=code
    id=data["id"]
    body={
        "price":{
            "iataCode": code
        }
    }
    data_manager.update(id,body)
data_manager.data=sheet_data
print(data_manager.data)


