travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country,num_of_visits,cities_visited):
    entry={}
    entry["country"]=country
    entry["visits"]=num_of_visits
    entry["cities"]=cities_visited
    travel_log.append(entry)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print(travel_log[2]["country"])
