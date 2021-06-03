import requests
import datetime

USERNAME = "nikhil123"
TOKEN = "bv94862v3m9c4nv2ytynv39"
GRAPH_ID = "mygraph123"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_PARAMS = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)

header = {
    "X-USER-TOKEN": TOKEN
}

graph_end_point = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#
# graph_config ={
#     "id": GRAPH_ID,
#     "name": "Learning",
#     "unit": "minutes",
#     "type": "int",
#     "color": "ajisai",
# }

# response = requests.post(graph_end_point, json=graph_config, headers=header)
# print(response.text)

graph_pixel_endpoint = f"{graph_end_point}/{GRAPH_ID}"
# print(datetime.date.today().strftime("%Y%m%d"))
graph_pixel_config = {
    "date": datetime.date.today().strftime("%Y%m%d"),
    "quantity": "180"
}

response = requests.post(graph_pixel_endpoint, json=graph_pixel_config, headers=header)
print(response.text)