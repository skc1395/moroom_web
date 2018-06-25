from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from .models import Profile
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from .forms import UserForm, ProfileForm, LoginForm, FileFieldForm


def signup(request):


    providers = []
    for provider in get_providers():

    # social_app속성은 provider에는 없는 속성입니다.
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            obj = User.objects.get(username=user_form.cleaned_data['username'])
            profile = Profile.objects.get(user=obj)
            profile.contact = profile_form.cleaned_data['contact']
            profile.is_updated = True
            profile.save()

            messages.success(request, '회원가입이 완료되었습니다.')

            return redirect('log_in')

    else:
        # messages.warning(request, '회원정보가 올바르지않습니다.')
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'accounts/signup.html', {
                        'user_form': user_form,
                        'profile_form': profile_form,
                        'providers': providers
                })



def log_in(request):

    providers = []
    for provider in get_providers():

# social_app속성은 provider에는 없는 속성입니다.
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, '로그인되었습니다.')
            return redirect('main')

        else:
            messages.warning(request, '아이디나 비밀번호가 틀립니다.')

            return redirect('log_in')

    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {
            'form': form,
            'providers': providers
            })


def log_out(request):
    logout(request)
    messages.success(request, '로그아웃되었습니다.')

    return redirect('main')


def profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            user = Profile.objects.get(user=request.user.id)
            user.contact = form.cleaned_data['contact']
            user.is_updated = True
            user.save()

            return redirect('main')

    else:
        form = ProfileForm()

    return render(request, 'accounts/profile.html', {
        'form': form
    })
