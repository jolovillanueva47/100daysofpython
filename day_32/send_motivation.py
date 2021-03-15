import smtplib
import random
import datetime as dt

my_email=""
password=""

now=dt.datetime.now()
day=now.weekday()

with open("quotes.txt") as file:
    quotes=file.readlines()

quote_of_the_day=random.choice(quotes)
print(quote_of_the_day)
if day==0:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="", msg=f"Subject:Monday Quote\n\n{quote_of_the_day}")
