from django.contrib import messages, auth
from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render

from basic.forms import CustomUserForm
from basic.models import CustomUser, Startapper, Staff


def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        user_type = request.POST['user_type']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if CustomUser.objects.filter(username=username).exists():
                registr_form = CustomUserForm()
                messages.info(request, "Foydalanuvchi nomi mavjud boshqa nom kiritng !!!")
                return render(request, 'register.html', {'form': registr_form})
            elif CustomUser.objects.filter(email=email).exists():
                registr_form = CustomUserForm()
                messages.info(request, 'Elektron pochta mavjud')
                return render(request, 'register.html', {'form': registr_form})
            elif CustomUser.objects.filter(phone=phone).exists():
                messages.info(request, "Bunday telefon nomer avval ro`yxatdan o'tgan!")
                return redirect('/')
            else:
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
                user_type = CustomUser.objects.get(email=request.user.email)
                if user_type.user_type == CustomUser.STARTAPPER:
                    Startapper.objects.create(user=user).save()
                    return render(request, 'startapper.html')
                if user_type.user_type == CustomUser.DEVELOPER:
                    Staff.objects.create(user=user).save()
                    return render(request, 'developer.html')
                if user_type.user_type == CustomUser.PRACTITIONER:
                    Staff.objects.create(user=user).save()
                    return render(request, 'practitioner.html')
        else:
            messages.info(request, "Parollar bir biriga to'g'ri kelmaydi !!!")
            return redirect('/')

        user = auth.authenticate(username=username, password=password1)
        auth.login(request, user)
        print("Autorizatsiya bolmadi")

        return redirect('/')
    else:
        registr_form = CustomUserForm()
        return render(request, 'register.html', {'form': registr_form})


def index(request):
    return render(request, 'index.html')
