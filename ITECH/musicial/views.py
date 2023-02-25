from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'musicial/homepage.html')

def signInPage(request):
    return render(request,'musicial/sign-in.html')

def registerPage(request):
    return render(request,'musicial/registerPage.html')
