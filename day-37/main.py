from datetime import  datetime
import requests
TOKEN="YOUR TOKEN"
USERNAME="YOUR SELF GENERATED USERNAME"
pixela_endpoint="https://pixe.la/v1/users"
GRAPH_ID="YOUR GRAPH ID"

user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#POST
# response=requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
graph_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai"
}
headers={
     "X-USER-TOKEN":TOKEN
}
# response=requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_creation_endpoint= f"{graph_endpoint}/{GRAPH_ID}"

today=datetime.now()

new_pixel_data={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometers did you cycle today?:")
}
response=requests.post(pixel_creation_endpoint, json=new_pixel_data, headers=headers)
print(response.text)


update_endpoint= f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"
new_pixel_data= {
     "quantity": "23",
 }
#PUT
# response=requests.put(url=update_pixel, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint=update_pixel
# response=requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)