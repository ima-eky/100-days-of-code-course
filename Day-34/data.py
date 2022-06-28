import  requests
PARAMETERS={
    'amount':10,
    'type':"boolean",
    "category":18
}
response=requests.get("https://opentdb.com/api.php",params=PARAMETERS)
response.raise_for_status()
question_data=response.json()["results"]
