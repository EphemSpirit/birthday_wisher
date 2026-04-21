import os
import smtplib
from dotenv import load_dotenv

load_dotenv()

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=os.getenv("GMAIL_ADDRESS"), password=os.getenv("GMAIL_APP_PASSWORD"))
    connection.sendmail(
        from_addr=os.getenv("GMAIL_ADDRESS"),
        to_addrs=os.getenv("YAHOO_ADDRESS"),
        msg="Subject:Hello\n\nThis is the body of my email."
    )
