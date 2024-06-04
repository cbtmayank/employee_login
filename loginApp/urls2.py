from . import views
from django.urls import path

urlpatterns = [

    path('user_data', views.userViewSet.as_view({'post': 'addUser'})),
    path('user_login', views.userViewSet.as_view({'post':'userLogin'})),
    path('password_change',views.userViewSet.as_view({'post':'changePassword'})),
    path("forget_password", views.userViewSet.as_view({'post':'forgetPassword'})),
    path("user_update", views.userViewSet.as_view({'post':'userUpdate'})),
    path('dataview',views.userViewSet.as_view({'post':'dataView'})),
    path('log_out',views.userViewSet.as_view({'post':'logOut'})),
    path('delete_user',views.userViewSet.as_view({'post':'deleteData'}))

   
]
