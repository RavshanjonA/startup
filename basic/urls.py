from django.urls import path
from .views import  index, register, login_user, logout_user, startapper_account

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login_user'),
    path('logout_user/', logout_user, name='logout_user'),
    #startapper profile
    path('startapper/', startapper_account, name='startapper_account')
]

