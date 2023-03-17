from django.shortcuts import render, HttpResponse, redirect
from django import forms



class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        required=True
    )





def login(request):

    if request.method == "GET":
        form = LoginForm()
        return render(request, "login.html", {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        print(form.cleaned_data)
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("password","用户名或密码错误")
            return render(request, "login.html", {'form': form})

        request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # return redirect("")
        return HttpResponse("校验成功")
    return render(request, "login.html", {'form': form})