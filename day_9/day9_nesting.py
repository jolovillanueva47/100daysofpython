#Nesting
capitals={
    "France":"Paris",
    "Germany":"Berlin",
}

#Nesting list in dictionary
travel_list={
    "France":["Paris","Lille","Dijon"],
    "Germany":["Berlin","Hamburg","Stuttgart"],
}

#Nesting dictionary in a dictionary
travel_dict={
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_visits":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5},
}
print(travel_dict["France"])

#Nesting a dictionary in a list

travel_log=[
    {
        "country":"France",
        "cities_visited":["Paris","Lille","Dijon"],
        "total_visits":12
    },
    {
       "country":"Germany",
       "cities_visited":["Berlin","Hamburg","Stuttgart"],
       "total_visits":5
    },
]
print(travel_log[0])