import smtplib
import  datetime as dt
import  random

now=dt.datetime.now()
week_day=now.weekday()
if week_day ==4:
    with open("quotes.txt") as quotes_source:
        list_of_quotes=quotes_source.readlines()
    message=random.choice(list_of_quotes)
    my_email="imaabasi00@gmail.com"
    password="bqtnphfarsvfwbky"
    with smtplib.SMTP ("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=f"ekanemima2022@yahoo.com",
                            msg=f"Subject:Friday Motivation\n\n{message}")
