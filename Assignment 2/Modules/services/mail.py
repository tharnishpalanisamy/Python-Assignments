from email.message import EmailMessage 
from email.utils import make_msgid, formatdate  # Crucial for bypassing spam filters
import smtplib
from config import PASSWORD 
import random 


class EmailSender:
    def __init__(self):
        pass 


    def generate_otp(self) ->int :
        return random.randint(1000 , 9999) 
    
    def send_otp(self , receiver, otp): 
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

    def authenticate_user(self , receiver : str ) ->bool  :
        otp = self.generate_otp() 

        self.send_otp(receiver=receiver , otp=otp)  
        print(f'Otp has been sent to {receiver}') 

        attempts = 3 
        while attempts > 0 :
            user_otp : int = int(input('Enter the received Otp : ')) 

            if user_otp != otp :
                attempts -= 1 
                print(f'Incorrect Otp ! {attempts} left') 
            elif user_otp == otp :
                return True 
        return False 






        
