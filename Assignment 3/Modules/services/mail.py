from email.message import EmailMessage 
from email.utils import make_msgid, formatdate
import smtplib
from config import PASSWORD 
import random 
from Modules.utilities import validate_email

class EmailSender:
    def __init__(self):
        pass 

    def generate_otp(self) -> int:
        return random.randint(1000, 9999) 
    
    def send_otp(self, receiver: str, otp: int) -> bool: 
        if not validate_email(receiver):
            raise ValueError(f"Invalid recipient email: {receiver}")

        try: 
            sender = 'tharnishpalanisamy3@gmail.com' 
            password = PASSWORD
            if not password:
                raise ValueError("Email credentials not configured in environment.")

            msg = EmailMessage()
            msg["Subject"] = "Security Verification Code" 
            msg["From"] = sender
            msg["To"] = receiver
            msg["Date"] = formatdate(localtime=True)
            msg["Message-ID"] = make_msgid(domain='gmail.com')
            
            email_body = f"""Hello,

Your requested one-time security verification code is provided below to complete your profile update.

Verification Code: {otp}

This code will remain active for 10 minutes. For account security, do not share this code with anyone.

If you did not initiate this request, please safely disregard this notice.

Regards,
Secure Identity Team
"""
            msg.set_content(email_body)
        
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(sender, password)
                smtp.send_message(msg)
        
            return True 

        except Exception as e:
            print('Otp failed') 
            print(e) 
            return False

    def authenticate_user(self, receiver: str) -> bool:
        if not validate_email(receiver):
            raise ValueError(f"Invalid email: {receiver}")

        otp = self.generate_otp() 
        sent = self.send_otp(receiver=receiver, otp=otp)  
        if not sent:
            print("Failed to send OTP to email.")
            return False

        print(f'Otp has been sent to {receiver}') 

        attempts = 3 
        while attempts > 0:
            try:
                user_otp_input = input('Enter the received Otp : ').strip()
                user_otp = int(user_otp_input)
            except ValueError:
                attempts -= 1
                print(f'Invalid OTP format! Please enter a 4-digit number. {attempts} left')
                continue

            if user_otp != otp:
                attempts -= 1 
                print(f'Incorrect Otp ! {attempts} left') 
            else:
                return True 
        print('Authentication Failed')
        return False
