import smtplib

my_email=""
password=""
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="", msg="Subject:Hello\n\nHello test")
