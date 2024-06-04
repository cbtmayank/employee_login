from django.shortcuts import render
from rest_framework import viewsets
from .models import cbtUser
from .serializer import loginAppSerializer
from loginPortal.cbt_loginResponse_api import loginResponse
from loginPortal.constant import *
from loginPortal.connection import *
from loginPortal.settings import *
import random
from django.contrib.auth import authenticate, login, logout



# from rest_framework import 



# Create your views here.

class userViewSet(viewsets.ModelViewSet):

    # Add USER HERE . 

    def addUser(self, request):

        try:
            data=request.data
            serializers=loginAppSerializer(data=data)
           
            if serializers.is_valid():
                serializers.save()
            
                return loginResponse( serializers.data, ApiStatus.Success, CbtMessage.SubmitSuccessMsg).cbtResponse()     
            return loginResponse(ApiStatus.Failure, CbtMessage.MessageNotValid, serializers.errors).cbtResponse()
            
        except Exception as ex:

            return loginResponse(ApiStatus.Failure, CbtMessage.MessageException, ex).cbtResponse()
        
    # END OF ADD USER
        
    # USER LOGIN CREATE HERE . 
      # USER LOGIN FUNCTION HERE
    def userLogin(self, request):
        try:
            data = request.data
            result = data.get('password')
            password = result
            
            email = data.get('email')
           
        
            user = authenticate(username=email,password = password)
            
            if user is not None:
                try:
                    login(request, user) 
                    user_obj = cbtUser.objects.get(email=data.get('email'), password=password)
                except:
                    return loginResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your login detail isn't valid!!")).cbtResponse()            
            else:
                try:
                    user_obj = cbtUser.objects.get(email=data.get('email'), password=password)
                except:
                    return loginResponse( ApiStatus.Failure, CbtMessage.cbtMsg("Your login my detail isn't valid!!")).cbtResponse()
            
            # user_data = tokenUpdate(user_obj)
            user_data = user_obj
            if user_data is not None:
                if user_data.state_active:
                    serializer = loginAppSerializer(user_data)
                    return loginResponse(serializer.data, ApiStatus.Success, CbtMessage.LoginSuccessMsg).cbtResponse()
            
                return loginResponse( ApiStatus.Failure, CbtMessage.cbtMsg("Your account is deactivate. Please contact with administrator!!")).cbtResponse()
                   
            return loginResponse( ApiStatus.Failure, CbtMessage.LoginFailedMsg).cbtResponse()
            
        except Exception as ex:
            return loginResponse( ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        
    # CHANGE PASSWORD HERE .

    def changePassword(self, request):

        try:
            data = request.data
            try:
                user_obj = cbtUser.objects.get(email=data.get('email'))
            except:
                user_obj = None

            if user_obj is None:
                return loginResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

            if user_obj.otp != data.get('otp'):
                return loginResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your otp isn't valid!!")).cbtResponse()

            old = str(user_obj.otp_time).split('.')[0]
            new = str(datetime.datetime.today()).split('.')[0]
            
            time = datetime.datetime.strptime(new, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(old, '%Y-%m-%d %H:%M:%S')
            
            minutes = time.total_seconds() / 60
            
            if minutes < 16:
                user_password = data.get('new_password')
                
                
                cbtUser.objects.filter(user_id=user_obj.user_id).update(password=user_password)

                return loginResponse([], ApiStatus.Success, CbtMessage.cbtMsg("Your password has been successfully changed!!")).cbtResponse()
            
            return loginResponse([], ApiStatus.Failure, CbtMessage.cbtMsg("Your otp has been expaired!!")).cbtResponse()
    
        except Exception as ex:
            return loginResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()   
        
    # FORGET PASSWORD HERE . 

    def forgetPassword(self, request):
        try:
            data=request.data
       
            if sendOTP(data.get('email')):
                               
                return loginResponse([], ApiStatus.Success, CbtMessage.cbtMsg("OTP send Successfully .")).cbtResponse()
           
            return loginResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()
        except Exception as ex:

            return loginResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()
    
    # VIEW FUNCTION HERE .
    def dataView(self, request):
        try:            
            data = request.data
           
            if data.get('user_id') is not None:
                data_obj = cbtUser.objects.get(user_id=data.get('user_id'))
                serializer = loginAppSerializer(data_obj)
                return loginResponse(serializer.data, ApiStatus.Success,  CbtMessage.SubmitSuccessMsg, ).cbtResponse()

                
            else:
                data_objs = cbtUser.objects.filter(state_active=1)
                serializer = loginAppSerializer(data_objs, many=True)

                return loginResponse(serializer.data, ApiStatus.Success,  CbtMessage.SubmitSuccessMsg, ).cbtResponse()
              
        except Exception as ex:
            return loginResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()  


            
# Update function here...
    def userUpdate(self, request):
        try:
            data = request.data
            
            data_obj = cbtUser.objects.get(user_id=data.get('user_id'))
            serializer = loginAppSerializer(data_obj, data=data)
            if serializer.is_valid():
                serializer.save()  
                return loginResponse(serializer.data, ApiStatus.Success, CbtMessage.UpdateSuccessMsg).cbtResponse()
            
            return loginResponse(serializer.errors, ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()

        except Exception as ex:
            return loginResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()  
  
# Delete Function here ....
    def deleteData(self, request):
        try:
            data=request.data
            if data.get('user_id') is not None:
                obj = cbtUser.objects.get(user_id=data.get('user_id'))

                # obj=cbtUser.objects.filter(id=data.get('user_id'))
                obj.delete()
                return loginResponse([], ApiStatus.Success, CbtMessage.DeleteSuccessMsg).cbtResponse()

                # return loginResponse({'message': 'data has been successfuly Deleted.','payload':data})
            
            # return loginResponse({'message': 'data is not valid.'})
            return loginResponse([], ApiStatus.Failure, CbtMessage.DataNotValid).cbtResponse()


        except Exception as ex:
            return loginResponse([], ApiStatus.Exception, CbtMessage.CbtExceptionMsg(ex)).cbtResponse()  


            # return loginResponse({'message':f'somthing went wrong. {ex}'})
