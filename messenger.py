import smtplib
from email.mime.text import MIMEText
#from dotenv import load_dotenv

# List the sender and recepient emails
sender = ''
recepient = ''
#PASSWORD


def messenger(symbol, price, level):
    if (level == "Ceiling"):
        msg = MIMEText(f"${symbol} has risen above your ceiling price marker to: ${float(price):,.2f}")
        msg['Subject'] = 'subject'
        msg['From'] = sender
        msg['To'] = recepient
        print(f"${symbol} has risen above your ceiling price marker to: ${float(price):,.2f}")
    else:
        msg = MIMEText(f"${symbol} has fallen below your floor price marker to: ${float(price):,.2f}")
        msg['Subject'] = 'subject'
        msg['From'] = sender
        msg['To'] = recepient
        print(f"${symbol} has fallen below your floor price marker to: ${float(price):,.2f}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, PASSWORD)
        smtp_server.sendmail(sender, recepient, msg.as_string())