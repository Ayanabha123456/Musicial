from django.contrib import admin
from musicial.models import UserProfile,FriendProfile, Post, Comment, FriendRequest
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(FriendProfile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FriendRequest)