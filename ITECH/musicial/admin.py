from django.contrib import admin
from musicial.models import UserProfile,FriendProfile, Post, Comment
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FriendProfile)
admin.site.register(Post)
admin.site.register(Comment)