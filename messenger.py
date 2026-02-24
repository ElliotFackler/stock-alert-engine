import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv() 

# List the sender and recepient emails
EMAIL1 = os.getenv("EMAIL1")
EMAIL2 = os.getenv("EMAIL2")
PASSWORD = os.getenv("PASSWORD")


def send_messenge(msg):
    """Form email and send it via gmail server"""
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(EMAIL2, PASSWORD)
        smtp_server.sendmail(EMAIL2, EMAIL1, msg.as_string())


def build_email(symbol, price, level):
    msg = MIMEText(f"${symbol} has reached your ${level} level and is now ${float(price):,.2f}")
    msg['Subject'] = 'Important ${symbol} Price Update: ${level} Price Reached'
    msg['From'] = EMAIL2
    msg['To'] = EMAIL1

    print(f"${symbol} has reached your ${level} level and is now ${float(price):,.2f}")

    send_messenge(msg)