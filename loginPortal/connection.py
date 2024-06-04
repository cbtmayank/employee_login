from django.conf import settings 
from django.core.mail import send_mail
from loginApp.models import *

import random
import datetime



# OTP SENDING FUNCTION

def sendOTP(myemail):
    try:
        
        try:
           
            user_obj = cbtUser.objects.get(email=myemail)
            # print(user_obj)
            # print("mayank",user_obj.email)

        except:
            return False

        otp_new = random.randint(100000,999999)
        current_day = datetime.datetime.today()

        cbtUser.objects.filter(user_id = user_obj.user_id).update(otp=otp_new, otp_time = current_day)
        user_obj = cbtUser.objects.get(user_id=user_obj.user_id)
        
        subject = "Forget you Password"
        messages = f'''
            Dear {user_obj.firstname},
            Your OTP is: {user_obj.otp}
            This is valid for 5min '''
        
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_obj.email]
        # print(user_obj.email,email_from)
        send_mail(subject, messages, email_from, recipient_list, fail_silently=False)

        return True
    
    except:
        return False