class CbtMessage:
    Successfully = 'Check-In Successfully!!'
    DataNotFound = 'Data Not Found'
    LoginSuccessMsg = 'Logged in has been successfully!!'
    LoginFailedMsg = "Login credential doesn't exist!!"
    SendSuccessMsg = 'Message has been successfully send!!'
    PermissionMsg = 'You do not have permission!!'
    SubmitSuccessMsg = 'Data has been successfully submited!!'
    UpdateSuccessMsg = 'Date has been successfully updated!!'
    DeleteSuccessMsg = 'Data has been successfully deleted!!'
    DataNotValid = "Data isn't valid!!"
    MessageFailed = "Message isn't send!!"
    MessageNotValid = "Data isn't valid!!"
    MessageException = 'Something went wrong!!'
    ExistMsg = 'already exist!!'
    UserDetailNotValid = "User details does't Valid!!"
    PendingDayplanMsg = "Please close pending day plan then create new one!!"

    def existMsg(message):
        return message+" "+CbtMessage.ExistMsg
    
    def cbtMsg(message)->str:
        return message
    
    def CbtExceptionMsg(ex)->str:
        return f"Something went wrong. Like !! - {ex}"
    
    def cbtImportMsg(count, total):
        return f"Data has been successfully Uploaded {count} in {total}.!!"
    

class ApiStatus:
    Success='SUCCESS'
    Status="STATUS"
    Exception='EXCAPTION'
    Message='MESSAGE'
    Failure='FAILURE'
    Permission = 'PERMISSION'
    Exist = 'EXIST'
    Pending = 'PENDING'
    