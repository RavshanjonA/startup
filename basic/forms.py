from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.contrib.auth import login
from .models import *


class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mt-2', 'name':'password1', 'placeholder':'enter the password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mt-2', 'name':'password2', 'placeholder':'Repeat the password...'}))
    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'user_type', 'phone', 'password1', 'password2', 'username')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'full_name'}),
            'username': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control mt-2', 'name': 'email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control mt-2', 'name': 'phone'}),
            'user_type': forms.Select(attrs={'class': 'form-control mt-2', 'name': 'user_type'}),
        }

# class CustomUserForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('full_name', 'email', 'user_type','phone', 'password1', 'password2','username')
#         widgets = { 
#             'user_type':forms.Select(attrs={'class': 'form-control mt-2'}), 
#         }

# class CustomUserForm(forms.Form):
#     full_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'full_name',
#             'class':'form-control',
#             'required':'required'
#         })
#     )

#     user_type = forms.Select(
#     )

#     email = forms.EmailField(
#         max_length=40,
#         widget=forms.EmailInput(attrs={
#             'name':'email',
#             'class':'form-control',
#             'placeholder':'elektronpochta@gmail.com',
#             'required':'required'
#         })
#     )

#     username = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'username',
#             'class':'form-control',
#             'id':'usernameInput',
#             'placeholder':'Loginni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     phone = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(attrs={
#             'name':'phone',
#             'class':'form-control',
#             'id':'usernameInput',
#             'placeholder':'Loginni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     password1 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={
#             'name':'password1',
#             'class':'form-control',
#             'id':'InputPassword',
#             'placeholder':'Parolni kiriting va eslab qoling..',
#             'required':'required'
#         })
#     )

#     password2 = forms.CharField(
#         max_length=30,
#         widget=forms.PasswordInput(attrs={
#             'name':'password2',
#             'class':'form-control',
#             'id':'InputPassword',
#             'placeholder':'Parolni qayta kiriting..',
#             'required':'required'
#         })
#     )
