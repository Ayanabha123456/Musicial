from django.shortcuts import render 
from django.shortcuts import redirect 
from django.http import HttpResponse
from rango.forms import LoginForm

#Create your views here

def login(request):

    # if request.method == "GET":
    #     form = LoginForm()
    #     return render(request, "login.html", {'form': form})

    # form = LoginForm(data=request.POST)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
    #     if not admin_object:
    #         form.add_error("password","用户名或密码错误")
    #         return render(request, "login.html", {'form': form})

    #     request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
    #     # return redirect("")
    #     return HttpResponse("校验成功")
    # return render(request, "login.html", {'form': form})
    return render(request, "login.html")