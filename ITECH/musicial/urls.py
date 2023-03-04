from django.urls import path
from musicial import views
from django.conf import settings
from django.conf.urls.static import static

app_name ='musicial'

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signInPage,name='signin'),
    path('register',views.registerPage,name='register'),
    path('landing',views.userHomepage,name='landing'),
<<<<<<< HEAD
    path('createPhoto', views.createPhotoPage,name='createPhoto'),
    
]

#server uplaod media files
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
=======
    path('create-post',views.userCreatePostPage,name='create-post'),
    path('social',views.userSocialPage,name='social'),
    path('profile',views.userProfilePage,name='profile')
]
>>>>>>> origin/main
