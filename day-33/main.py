import time

import  requests
from datetime import  datetime
import  smtplib
MY_LAT= "YOUR LATITUDE"
MY_LONG="YOUR LONGITUDE"
MY_EMAIL="YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"
def is_iss_overhead():
    response=requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data=response.json()
    longitude=float(data["iss_position"]["longitude"])
    latitude=float(data["iss_position"]["latitude"])
    if MY_LAT-5 <latitude <MY_LAT+5 and MY_LONG-5 <longitude <MY_LONG+5:
        return  True
def is_night():
    parameters={
        "lng":MY_LAT,
        "lat":MY_LONG,
        "formatted":0
    }
    reponse=requests.get(" https://api.sunrise-sunset.org/json",params=parameters)
    reponse.raise_for_status()
    data=reponse.json()
    sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset=data["results"]["sunset"].split("T")[1].split(":")[0]

    current_hour=datetime.now().hour
    if current_hour >= sunrise or current_hour<= sunset:
        return True
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection=smtplib.SMTP("smtp.gmail.com",port=587)
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look up\n\nThe ISS is above you in the sky."
        )