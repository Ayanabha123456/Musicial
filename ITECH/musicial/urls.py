from django.urls import path
from musicial import views

app_name ='musicial'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signInPage,name='sigin'),
    path('register',views.registerPage,name='register')
]