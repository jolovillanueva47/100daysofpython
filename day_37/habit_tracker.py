import requests
from datetime import datetime 

USERNAME=""
TOKEN=""
GRAPH_ID="graph1"

pixela_endpoint="https://pixe.la/v1/users"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsofService":"yes",
    "notMinor":"yes"
}

# Create User
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":"graph1",
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}

headers={
    "X-USER-TOKEN":TOKEN
}

# Create Graph
# response=requests.post(url=graph_endpoint,json=graph_config, headers=headers)
# print(response.text)

today=datetime.now()

data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did you cycle today? ")
}

# Input data to graph
cycling_graph_endpoint=f"{graph_endpoint}/{GRAPH_ID}"
# response=requests.post(url=cycling_graph_endpoint,json=data,headers=headers)
# print(response.text)


pixel_data={
    "quantity":"4.5"
}

date_to_edit=today.strftime("%Y%m%d")

# Update pixel
cycling_graph_endpoint_date=f"{cycling_graph_endpoint}/{today.strftime('%Y%m%d')}"
response=requests.put(url=cycling_graph_endpoint_date,json=pixel_data,headers=headers)

# Delete pixel
# response=requests.delete(url=cycling_graph_endpoint_date,headers=headers)

print(response.text)