import os
import smtplib
from dotenv import load_dotenv
import pandas
import datetime as dt
import random

load_dotenv()

today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_data = pandas.read_csv("birthdays.csv")

birthday_dict = {(row.month, row.day):row for (_, row) in birthday_data.iterrows()}

def send_birthday_email():
    birthday_haver = birthday_dict[today]
    files = os.listdir("letter_templates")

    with open(f"letter_templates/{random.choice(files)}") as file:
        data = file.read()
        data = data.replace("[NAME]", birthday_haver["name"])

    with smtplib.SMTP(os.getenv("SMTP_HOST"), 587) as connection:
        connection.starttls()
        connection.login(user=os.getenv("GMAIL_ADDRESS"), password=os.getenv("GMAIL_APP_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("GMAIL_ADDRESS"),
            to_addrs=os.getenv("YAHOO_ADDRESS"),
            msg=f"Subject:Happy Birthday!\n\n{data}."
        )

if today in birthday_dict:
    send_birthday_email()



