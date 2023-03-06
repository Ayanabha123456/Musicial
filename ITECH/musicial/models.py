from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50,blank=False)
    picture = models.ImageField(upload_to='profile_images',blank=False)

    def __str__(self):
        return self.user.username

class FriendProfile(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='target_user')
    friend = models.ManyToManyField(UserProfile,related_name='target_friend')

    def __str__(self):
        return self.user.user.username

class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    class Meta:
        app_label = 'musicial'
        
        
class MyImage(models.Model):
    name = models.CharField(max_length=100)
    image_file=models.ImageField(upload_to='images/')

#any form field validators