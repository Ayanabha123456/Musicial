from django.urls import path
from musicial import views

app_name ='musicial'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signInPage,name='signin'),
    path('register',views.registerPage,name='register'),
    path('landing',views.userHomepage,name='landing'),
    path('create-post',views.userCreatePostPage,name='create-post'),
    path('social',views.userSocialPage,name='social'),
    path('profile',views.userProfilePage,name='profile'),
    path('songs',views.songPage,name='songs'),
    path('playlist',views.userPlaylistPage,name='playlist'),
    path('logout',views.logout,name='logout')
]