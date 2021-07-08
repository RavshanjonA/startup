from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CustomUserForm
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from .models import *
from django.db import IntegrityError
# Create your views here.

def home(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email'] 
        phone = request.POST['phone'] 
        user_type = request.POST['user_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = CustomUser.objects.create_user(
                                                        full_name=full_name,
                                                        username=username, 
                                                        phone=phone, 
                                                        password=password1, 
                                                        user_type=user_type,  
                                                        email=email,
                                                        )         
                user.save()
                login(request, user)
            except IntegrityError:
                messages.info(request, "Bunday telefon nomer avval ro`yxatdan o'tgan!")
                registr_form = CustomUserForm()
                return render(request, 'home.html', {'form':registr_form})

        else:
            messages.info(request, "Parollar bir xil emas!")
            return redirect('/')
        
        return redirect('/')
    else:
        registr_form = CustomUserForm()
        return render(request, 'home.html', {'form':registr_form})

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserForm(request.POST)
#         print(form,'post metodi ishladiiiiiiii')
#         if form.is_valid():
#             form.save()
#             full_name = form.cleaned_data.get('full_name')
#             password = form.cleaned_data.get('password')
#             user_type = form.cleaned_data.get('user_type')
#             user = auth.authenticate(username=full_name, password=password)
#             login(request, user)
#             # if user_type in CustomUser.USER_TYPE:
#             current_user = request.user
#             if user_type == CustomUser.STARTAPPER:
#                 data = Startapper()
#                 data.user_id = current_user.id
#                 data.save()
#                 return render(request, 'startapper.html')
#             if user_type == CustomUser.DEVELOPER:
#                 print("Deweloper")
#             if user_type == CustomUser.PRACTITIONER:
#                 print("Amaliyotchi")
#             return redirect('register')
#         else:
#             print(form,'xatolik metodi ishladiiiiiiii')
#             messages.warning(request, "Registration error!")
#             return HttpResponseRedirect('/')
#     form = CustomUserForm()
#     print(form,'get metodi ishladiiiiiiii')
#     return render(request, 'home.html', {'form': form})


# def home(request):
#     model = CustomUser()
#     form = CustomUserForm(request.POST or None)
#     if request.POST:
#         print('--------------------------------------')
#         if form.is_valid():
#             form.save()
#             login(request, model)
#             return render(request, 'index.html')

#         else:
#             HttpResponseRedirect('/')
#     ctx = {
#         'form': form
#     }
#     return render(request, 'home.html', ctx)