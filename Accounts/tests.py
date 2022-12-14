from django.test import TestCase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import json
def send_otp(email,otp,name):
    import smtplib

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()
    s.ehlo()
    s.login("khushaljangid.ai25@jecrc.ac.in", "Kh@130404")

    msg = MIMEMultipart()

    msg['From']="Lumi Incorporated"
    msg['To']=email
    msg['Subject']="Lumi: OTP for Verification"

    msg.attach(MIMEText(f"Hi {name},\nPlease use the OTP below to verify.It is only Valid for 3 minutes.\n\n{otp}\n\n\nPlease don't share your OTP with anyone.\nPlease ignore if you didn't asked for verification.", 'plain'))

    s.send_message(msg)

    s.quit()

def get_otp():
    import pyotp
    secret=pyotp.random_base32()
    otp = pyotp.TOTP(secret)
    return otp.now()

def send_to_phone(number,otp):
    url = "https://www.fast2sms.com/dev/bulk"
    # create a dictionary
    my_data = {
        # Your default Sender ID
        'sender_id': 'X-LMIAP', 
        
        # Put your message here!
        'message': f'\nHi,\nDid you login to lumi.com?\nHere is your OTP:\n{otp}\nPlease don`t share it with anyone.', 
        
        'language': 'english',
        'route': 'p',
        
        # You can send sms to multiple numbers
        # separated by comma.
        'numbers':number
    }
    
    # create a dictionary
    headers = {
        'authorization': '3IelyzdGBiQvpYVcgDMKn1AuRq5jErbs27w0kS9JZtFaoNU48OmYVK7T2nRG9uwifHWU1tA5p6Lzk0Z4',
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache"
    }
    response = requests.request("POST",
                            url,
                            data = my_data,
                            headers = headers)
    returned_msg = json.loads(response.text)
    
    # print the send message
    print(returned_msg['message'])


# if __name__=='__main__':
#     send_to_phone("9828126444",896545)

