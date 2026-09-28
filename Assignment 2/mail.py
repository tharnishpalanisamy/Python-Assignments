from email.message import EmailMessage 
from email.utils import make_msgid, formatdate  # Crucial for bypassing spam filters
import smtplib
from config import PASSWORD 

def send_otp(receiver, otp): 
    try: 
        sender = 'tharnishpalanisamy3@gmail.com' 
        password = PASSWORD
        msg = EmailMessage()
        
        # 1. Neutralize trigger words slightly & set standard headers
        msg["Subject"] = "Security Verification Code" 
        msg["From"] = sender
        msg["To"] = receiver
        
        # 2. ANTI-SPAM HEADERS: This is what your script was missing
        msg["Date"] = formatdate(localtime=True)
        msg["Message-ID"] = make_msgid(domain='gmail.com')
        
        # 3. Soften the email body language
        email_body = f"""\
Hello,

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
