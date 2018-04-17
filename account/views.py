from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .forms import UserForm, ProfileForm, LoginForm, FileFieldForm


def home(request):

    return render(request, 'account/home.html', {})

def signup(request):

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        a = request.FILES.getlist('file_field')
        print(a)
        print(user_form.is_valid())
        print(profile_form.is_valid())

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            obj = User.objects.get(username=user_form.cleaned_data['username'])
            profile = Profile.objects.get(user=obj)
            profile.contact = profile_form.cleaned_data['contact']
            profile.save()

            messages.success(request, '회원가입이 완료되었습니다.')

            return redirect('log_in')


    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        file_form = FileFieldForm()

    return render(request, 'account/signup.html', {
                        'user_form': user_form,
                        'profile_form': profile_form,
                        'file_form': file_form
                })


def log_in(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')

        else:
            return HttpResponse('로그인이 실패하였습니다')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
            'form': form
            })

def log_out(request):
    logout(request)

    return redirect('main')


# def check_id(request):
#     if request.method == 'POST':
#         user = User.objects.get(username=request.POST['username'])
#
#         if user is not None:
#             print('이미 가입된 아이디가 있습니다')
#
#             return redirect('signup')
#
#         else:
#             print('가입이 가능합니다 ')
#
