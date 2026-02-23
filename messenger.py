import smtplib
from email.mime.text import MIMEText

# List the sender and recepient emails
sender = ''
recepient = ''


def messenger(symbol, price, level):
    if (level == "Ceiling"):
        msg = MIMEText(f"${symbol} has risen above your ceiling price marker to: ${float(price):,.2f}")
        msg['Subject'] = 'subject'
        print(f"${symbol} has risen above your ceiling price marker to: ${float(price):,.2f}")
    else:
        msg = MIMEText(f"${symbol} has fallen below your floor price marker to: ${float(price):,.2f}")
        msg['Subject'] = 'subject'
        print(f"${symbol} has fallen below your floor price marker to: ${float(price):,.2f}")