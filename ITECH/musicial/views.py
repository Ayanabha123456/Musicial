from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from musicial.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from musicial.models import UserProfile
# Create your views here.

def index(request):
    return render(request,'musicial/homepage.html')

def signInPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                user = authenticate(username=username,password=password)
                if user:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect('landing')
                    else:
                        return HttpResponse("Your Musicial account does not exist")
                else:
                    return HttpResponse('Invalid login details')
            else:
                return HttpResponse('Wrong Password')
        except User.DoesNotExist:
            return HttpResponse('Invalid login details')
        
    else:
        return render(request,'musicial/sign-in.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user:
                return HttpResponse('User already exists')
        except User.DoesNotExist:
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST,request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    print('Picture acquired')
                    profile.picture = request.FILES['picture']
                profile.save()

                user = authenticate(username=username,password=password)
                login(request,user)
                return HttpResponseRedirect('landing')
            else:
                print(user_form.errors,profile_form.errors)
    else:
        return render(request,'musicial/registerPage.html')

def userHomepage(request):
    return render(request,'musicial/userhomepage.html')

def userCreatePostPage(request):
    return render(request,'musicial/createPage.html')

def userSocialPage(request):
    return render(request,'musicial/socialPage.html')

