from django.db import models

# Create your models here.
class cbtUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    user_code = models.CharField(max_length=255,null=True, blank=True, unique=True)
    email = models.CharField(max_length=255, unique=True, default='')
    phone = models.CharField(max_length=255, unique=True, default='')
    password = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=255, null=True, default="male")
    city = models.CharField(max_length=255, null=True,)
    state_active = models.IntegerField(null=True, blank=True,default=1)
    otp = models.CharField( max_length=255,null=True, blank=True, default='')
    otp_time = models.CharField(max_length=255, null=True,blank=True, default='')

    class Meta:

        db_table = "cbt_user"
    

    
