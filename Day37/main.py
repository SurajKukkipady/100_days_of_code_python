import requests
from datetime import datetime

USER_NAME = "kukki"
TOKEN = "abcd1234"


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "abcd1234",
    "username": "kukki",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Update the graph

today = datetime.now()

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "600"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)



