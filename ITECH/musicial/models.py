from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import uuid

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
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_post')
    picture = models.ImageField(upload_to='posts',blank=False)
    caption = models.CharField(max_length=200,blank=True,default='')
    date = models.DateField(default=datetime.now())
    likes = models.ManyToManyField(UserProfile,related_name='post_likes')

    def __str__(self):
        return self.user.user.username + ':' + self.caption
    
    def get_date(self):
        return datetime.strftime(self.date,"%a, %b %d, %Y")
    
    def total_likes(self):
        return self.likes.count()

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=512,blank=False)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.name)


#any form field validators