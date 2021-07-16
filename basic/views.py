from django.contrib import messages, auth
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.decorators import login_required

from basic.forms import CustomUserForm, LoginForm, StartapperAccountForm, SimpleCustomForm, \
    IdeaStartApperForm, ApplicationDeveloperForm, ApplicationPractitionerForm
from basic.models import CustomUser, Startapper, Staff, IdeaStartapper, ApplicationStaff, AllUsersIdea
from django.views.generic import CreateView
from .forms import AllUserIdeaForm, DeveloperAccountorm


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
                    startapper = Startapper.objects.create(user=user)
                    startapper.save()
                    return redirect('startapper')
                if user_type.user_type == CustomUser.DEVELOPER:
                    Staff.objects.create(user=user).save()
                    return redirect('developer')
                if user_type.user_type == CustomUser.PRACTITIONER:
                    Staff.objects.create(user=user).save()
                    return redirect('practitioner')
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
        return render(request, 'account/login.html', {'form': user})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'account/login.html',
                          {'form': LoginForm(), 'error': 'Login yoki parol xato kiritildi!'})
        else:
            login(request, user)
            return render(request, 'index.html')


@login_required
def logout_user(request):
    logout(request)
    return render(request, 'index.html')


# create announcement
@login_required
def announcement(request):
    startapper = Startapper.objects.get(user=request.user)
    idea_startapper = IdeaStartapper.objects.filter(user=startapper).order_by('-created_at')[:6]
    if request.method == "POST" and request.FILES:
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES.get('file')
        elonlar = IdeaStartapper(
            title=title,
            description=description,
            file=file,
            user=startapper
        )
        elonlar.save()
        messages.info(request, "Your announcement successfully created!")
        return render(request, 'index.html', {'idea_startapper': idea_startapper})
    else:
        return render(request, 'announcement.html', {'idea_startapper': idea_startapper})


# startapper_account by function based view
# def startapper_account(request):
#     startapper = Startapper.objects.get(user=request.user)
#     print(startapper,'startapper+++++++++++++++++')
#     startappForm = StartapperAccountForm(instance=startapper)
#     print(startappForm,'startapperForm+++++++++++++++++')
#
#     if request.method == 'GET':
#         return render(request, 'account/startapper_account.html', {'form': startappForm})
#     else:
#         s_form = StartapperAccountForm(request.POST, request.FILES, instance=startapper)
#         print(s_form, 's_form +++++++++++++++++')
#         if s_form.is_valid():
#             s_form.save()
#         return render(request, 'index.html')

# startapper_account by class based view
class Startapper_update(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        startapper_ = Startapper.objects.get(user=self.request.user)
        form = StartapperAccountForm(instance=startapper_)
        login_url = 'login'
        context = {'form': form}
        return render(request, 'account/startapper_account.html', context)

    def post(self, request, *args, **kwargs):
        form = StartapperAccountForm(self.request.POST, self.request.FILES, instance=self.request.user.startapper)
        if form.is_valid():
            form.save()
            messages.info(self.request, "Your announcement successfully created!")
            return redirect(reverse('startapper_account'))
        return redirect('home')


class Developer_update(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        print(self.request.user,'++++++++++++++++++++++++++++++++')
        developer = Staff.objects.get(user=self.request.user)
        form = DeveloperAccountorm(instance=developer)
        login_url = 'login'
        context = {'form': form}
        return render(request, 'account/dev_account.html', context)

    def post(self, request, *args, **kwargs):
        form = DeveloperAccountorm(self.request.POST, self.request.FILES, instance=self.request.user.staff)
        print(form, '--------------------------')
        if form.is_valid():
            form.save()
            print(form, '--------------------------')
            messages.info(self.request, "ytttttttttttttour application has been successfully created!")
            return redirect(reverse('developer_update'))



# announcement detail
class announcementView(DetailView):
    model = IdeaStartapper
    template_name = 'idea_detail_startapper.html'
    success_url = reverse_lazy('announcement')
    context_object_name = 'object'
    login_url = 'login'  # new


@login_required
def announcement_delete(request, id):
    ann = get_object_or_404(IdeaStartapper, pk=id)
    if request.method == "POST":
        ann.delete()
        return redirect('home')


@login_required
def developer_home(request):
    developer = Staff.objects.get(user=request.user)
    if request.method == "POST":
        form = ApplicationDeveloperForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = Staff.objects.get(user=request.user)
            data = ApplicationStaff()
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            try:
                data.resume = request.FILES['resume']
            except MultiValueDictKeyError:
                messages.warning(request, 'resume where?')
                return redirect('developer')
            data.work_type = form.cleaned_data['work_type']
            data.user = current_user
            data.save()
            messages.success(request, 'Successfully send!')
            return redirect('developer')
        else:
            messages.warning(request, 'Announcement error!')
            return redirect('developer')
    form = ApplicationDeveloperForm()
    obj = ApplicationStaff.objects.filter(user=developer)
    return render(request, 'developer.html', {'developer': developer, 'form': form, 'obj': obj})


def startapper_home(request):
    startapper = Startapper.objects.get(user=request.user)
    return render(request, 'startapper.html', {'startapper': startapper})


def practitioner_home(request):
    practitioner = Staff.objects.get(user=request.user)
    if request.method == "POST":
        form = ApplicationPractitionerForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = Staff.objects.get(user=request.user)
            data = ApplicationStaff()
            data.title = form.cleaned_data['title']
            data.description = form.cleaned_data['description']
            data.resume = form.cleaned_data['resume']
            data.work_type = form.cleaned_data['work_type']
            data.user = current_user
            data.save()
            messages.success(request, 'Successfully send message!')
            return redirect('practitioner')
        else:
            messages.warning(request, 'Application error!')
            return redirect('practitioner')
    form = ApplicationPractitionerForm()
    obj = ApplicationStaff.objects.filter(user=practitioner)
    return render(request, 'practitioner.html', {'practitioner': practitioner, 'form': form, 'obj': obj})


#All User Idea create
class AllUserIdea(generic.CreateView):
    model = AllUsersIdea
    template_name = None
    form_class = AllUserIdeaForm

    def post(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        form = self.form_class(self.request.POST, self.request.FILES)
        form.instance.user = self.request.user
        if form.is_valid():
            form.save()
            return redirect(url)
        messages.error(self.request, "Forma tuliq bulmadi")
        return redirect(url)
