from datetime import datetime


import requests
GENDER="female"
WEIGHT_KG = 56
HEIGHT_CM = 12
AGE = 18
APP_ID="8a279f4c"
API_KEY="c6cf8ce50d64c5935c3c45efa0764027"
headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY,
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint="https://api.sheety.co/e8c5b0b1f35ffc408b70eccca67aba97/workoutTracking/workouts"

exercise = input("Tell me which exercises you did: ")

parameters = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

######################
today_date = datetime.now().strftime("%d%m%Y")
now_time=datetime.now().strftime("%X")
print(result)
for exercise in result["exercises"]:
    sheet_inputs ={
            "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
        }
    bearer_headers = {
        "Authorization": "Bearer YOUR_TOKEN_BEARER"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(sheet_response.text)