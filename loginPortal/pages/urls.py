from . import views
from .views import *
from django.urls import path

urlpatterns = [
    
    path('singin/', views.singin),
    path('singUp',views.singUp),
    path('singUp/<int:data_id>',views.singUp),
    path('singout',views.singout),
    path("forget", views.ForgetPassword),
    path("changePassword", views.changePassword),
    path("view-call",views.viewCall),
    path("view-call/<int:data_id>",views.viewCall)


    # path('password_reset',auth_views.PasswordResetView.as_view(), name='password-reset'),
    # path('password_reset/done',auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('p',auth_views.PasswordResetConfirmView.as_view(), name="pass_reset_confirm"),
    # path('m',auth_views.PasswordResetCompleteView.as_view(), name="pass_reset_complet")

]
