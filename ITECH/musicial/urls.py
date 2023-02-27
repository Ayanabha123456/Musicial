from django.urls import path
from musicial import views

app_name ='musicial'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signInPage,name='signin'),
    path('register',views.registerPage,name='register'),
    path('landing',views.userHomepage,name='landing'),
]