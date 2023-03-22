from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
import uuid

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #creating a one-to-one field on user - will comprise of username and password

    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50,blank=False)
    picture = models.ImageField(upload_to='profile_images',blank=False)

    def __str__(self):
        return self.user.username

class FriendProfile(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='target_user')
    friend = models.ManyToManyField(UserProfile,related_name='target_friend') #a many-to-many field on UserProfile - basically like a list of friends for every user

    def __str__(self):
        return self.user.user.username
    
    def get_num_friends(self):
        return self.friend.count() #return the no. of friends

class FriendRequest(models.Model):
    sender = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='friend_send')
    receiver = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='friend_receive')

    def __str__(self):
        return self.sender.user.username + '<-->' + self.receiver.user.username
    
class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_post')
    picture = models.ImageField(upload_to='posts',blank=False)
    caption = models.CharField(max_length=200,blank=True,default='')
    date = models.DateField(default=datetime.now())
    likes = models.ManyToManyField(UserProfile,related_name='post_likes') #a many-to-many field on UserProfile - basically like a list of likes for every user

    def __str__(self):
        return self.user.user.username + ':' + self.caption
    
    def get_date(self):
        return datetime.strftime(self.date,"%a, %b %d, %Y") #get the date of upload in a specific format
    
    def total_likes(self):
        return self.likes.count() #return no. of likes

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=512,blank=False) #username of the UserProfile who commented on the post
    body = models.TextField() #content of the comment
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.caption,self.name)
    

class Song(models.Model):
    songid = models.CharField(max_length=512,blank=False,primary_key=True) #we use the Spotify songid as the primary key
    name = models.TextField(blank=True)
    artist = models.CharField(max_length=512,blank=True)
    music_url = models.URLField(max_length=600,blank=True) #url for a small preview audio of the song - to be played using <audio> tag
    image_url = models.URLField(max_length=600,blank=True)

    def __str__(self):
        return self.songid+' : '+self.name

class Playlist(models.Model):
    playlistid = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=512,blank=False)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name='user_playlist')
    songs = models.ManyToManyField(Song,related_name='playlist_songs') #a many-to-many field on UserProfile - basically like a list of songs for every user-specific playlist

    def __str__(self):
        return str(self.playlistid)+' : '+self.name
    
    def get_num_songs(self):
        return self.songs.count() #return the no. of songs
