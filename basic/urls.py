from django.urls import path
from .views import  index, register

urlpatterns = [
    path('', index, name='home'),
    path('register/', register, name='register'),
]

