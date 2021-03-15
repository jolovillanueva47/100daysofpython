##################### Extra Hard Starting Project ######################
import smtplib
import random
import pandas as pd
import datetime as dt

my_email=""
password=""

now=dt.datetime.now()
print(str(now.date()))
year=now.year
month=now.month
day=now.day
# 2. Check if today matches a birthday in the birthdays.csv
data=pd.read_csv("birthdays.csv")
isBirthdayToday=data[(data['month']==month) & (data['day']==day)]

if not isBirthdayToday.empty:
    birthday_series=isBirthdayToday["name"]
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter=file.read().replace("Angela","Jolo")
    # 4. Send the letter generated in step 3 to that person's email address.
    for index,value in birthday_series.items():
        letter=letter.replace("[NAME]",value)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Happy Birthday {value}!\n\n{letter}")










