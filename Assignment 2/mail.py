import smtplib
from email.message import EmailMessage 
from config import PASSWORD

sender = "tharnishpalanisamy3@gmail.com"
receiver = "sastha00007@gmail.com"
password = PASSWORD

msg = EmailMessage()
msg["Subject"] = "Test Email"
msg["From"] = sender
msg["To"] = receiver
msg.set_content("Hello! This email was sent using Python.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent successfully!")