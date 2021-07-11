from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render

from basic.forms import CustomUserForm, LoginForm, StartapperAccountForm, SimpleCustomForm, IdeaStartApperForm
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
                return render(request, 'account/register.html', {'form': registr_form})
            elif CustomUser.objects.filter(email=email).exists():
                registr_form = CustomUserForm()
                messages.info(request, 'Elektron pochta mavjud')
                return render(request, 'account/register.html', {'form': registr_form})
            elif CustomUser.objects.filter(phone=phone).exists():
                registr_form = CustomUserForm()
                messages.info(request, "Bunday telefon nomer avval ro`yxatdan o'tgan!")
                return render(request, 'account/register.html', {'form': registr_form})
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
        return render(request, 'account/register.html', {'form': registr_form})


def index(request):
    return render(request, 'index.html')

def login_user(request):
    if request.method == 'GET':
        user = LoginForm()
        return render(request, 'account/login.html', {'form':user})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html', {'form':LoginForm(), 'error':'Login yoki parol xato kiritildi!'})
        else:
            login(request, user)
            return render(request, 'index.html')

def logout_user(request):
    logout(request)
    return render(request, 'index.html')


def announcement(request):
    idea_form = IdeaStartApperForm(instance=request.user)
    if request.method == 'GET':
        return render(request,'announcement.html',{'form':idea_form})
    else:

        idea_form = IdeaStartApperForm(request.POST, request.FILES, instance=request.user)
        if idea_form.is_valid():
            idea_form.save()
        return render(request, 'index.html')

def startapper_account(request):
    user = CustomUser.objects.get(username=request.user.username)
    customForm = SimpleCustomForm(instance=user)
    startapper = Startapper.objects.get(user=request.user)
    startappForm = StartapperAccountForm(instance=startapper)

    if request.method == 'GET':
        return render(request, 'account/startapper_account.html',{"obj": customForm,'form':startappForm})
    else:
        s_form = StartapperAccountForm(request.POST, request.FILES, instance=startapper)
        c_form = SimpleCustomForm(request.POST, request.FILES, instance=startapper)
        if s_form.is_valid() and c_form:
            c_form.save()
            s_form.save()
        return render(request, 'index.html')

