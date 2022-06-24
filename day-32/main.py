import  datetime as dt
import random
import pandas
import  smtplib

##################### Starting Project ######################

# 2. Check if today matches a birthday in the birthdays.csv
data=pandas.read_csv("birthdays.csv")
list_of_birthdays=data.to_dict(orient="records")
current_date=dt.datetime.now()
current_month=current_date.month
current_day=current_date.day

for birthdays in list_of_birthdays:
    if current_day ==birthdays["day"] and current_month == birthdays["month"]:
        with open (f"letter_templates/letter_{random.randint(1,3)}.txt") as data:
            content=data.read()
        new_letter=content.replace("[NAME]",birthdays["name"])
        my_email = "imaabasi00@gmail.com"
        password = "bqtnphfarsvfwbky"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays["email"],
                                msg=f"Subject:It's your birthday\n\n{new_letter}")




