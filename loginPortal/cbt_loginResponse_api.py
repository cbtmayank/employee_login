from django.http import JsonResponse, HttpResponse
from typing import Generic, TypeVar
from .constant import *
T = TypeVar('T')


class loginResponse(Generic[T]):

    def __init__(self, value:T, status:str, message:str=CbtMessage.SendSuccessMsg,) -> None:
        self.value=value
        self.status=status
        self.message=message
        

    def cbtResponse(self)->JsonResponse :

        if self.status==ApiStatus.Success:
            data={
                ApiStatus.Status: ApiStatus.Success,
                ApiStatus.Message: self.message,
                "DATA":self.value
                
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Exception:
            data={
                ApiStatus.Status:ApiStatus.Exception,
                ApiStatus.Message:self.message,
                # self.arrayName:[]
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Permission:
            data={
                ApiStatus.Status:ApiStatus.Permission,
                ApiStatus.Message:self.message,
                # self.arrayName:[]
            }
            return JsonResponse(data)

        elif self.status==ApiStatus.Exist:
            data={
                ApiStatus.Status:ApiStatus.Exist,
                ApiStatus.Message:self.message,
                # self.arrayName:[]
            }
            return JsonResponse(data)
            
        else :
            data={
                ApiStatus.Status:ApiStatus.Failure,
                ApiStatus.Message:self.message,
                # self.arrayName:[]
            }
            return JsonResponse(data)
