import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ITECH.settings')

import django
django.setup()
from django.contrib.auth.models import User
from musicial.models import UserProfile,FriendProfile, Post

def populate():
    profiles = [
        {'username':'Ayanabha',
         'password':'12345',
         'age':23,
         'gender':'Male',
         'picture':'profile_images/music_test_profile.jpg'},
         {'username':'Jun',
         'password':'Nice',
         'age':23,
         'gender':'Male',
         'picture':'profile_images/music_test_profile.jpg'},
         {'username':'Vivian',
         'password':'121',
         'age':23,
         'gender':'Female',
         'picture':'profile_images/music_test_profile.jpg'},
         {'username':'Borui',
         'password':'45',
         'age':23,
         'gender':'Male',
         'picture':'profile_images/music_test_profile.jpg'},
         {'username':'Xinhong',
         'password':'Glasgow24',
         'age':23,
         'gender':'Male',
         'picture':'profile_images/music_test_profile.jpg'},
    ]

    u1, u2, u3, u4, u5 = User.objects.get(username='Ayanabha'), User.objects.get(username='Jun'), User.objects.get(username='Vivian'),User.objects.get(username='Borui'),User.objects.get(username='Xinhong')
    u1, u2, u3, u4, u5 = UserProfile.objects.get(user=u1), UserProfile.objects.get(user=u2), UserProfile.objects.get(user=u3),UserProfile.objects.get(user=u4),UserProfile.objects.get(user=u5)

    user_friends = {
        u1:[u3,u5],
        u2:[u3,u4],
        u3:[u1,u2,u5],
        u4:[u2],
        u5:[u1,u3]
    }

    posts = [
        {'user':u3,
         'picture':'posts/sunset.jpg',
         'caption':'Looking for dreams across the sun'}
    ]
    for profile in profiles:
        print(profile)
        user = add_user(profile['username'],profile['password'])
        if user:
            print(user)
            add_profile(user,profile['age'],profile['gender'],profile['picture'])

    for user,friend_data in user_friends.items():
        add_friend(user,friend_data)
    
    for post in posts:
        add_post(post['user'],post['picture'],post['caption'])

    for p in UserProfile.objects.all():
        print(f'-{p}')

    for f in FriendProfile.objects.all():
        print('User: ',f)
        print('Friends: ',f.friend.all())
        print('\n')
    
    for post in Post.objects.all():
        print('Picture ID: ',post.id)
        print('User: ',post.user)
        print('Picture: ',post.picture)
        print('Caption: ',post.caption)
        print('Date: ',post.date)
        print('Likes: ',post.likes.all())
        print('\n')

def add_user(username,password):
    try:
        u = User.objects.get(username=username)
    except:
        u = User.objects.create_user(username=username,password=password)
        return u

def add_profile(user,age,gender,picture):
    p = UserProfile.objects.get_or_create(user=user,age=age,gender=gender,picture=picture)[0]
    p.age = age
    p.gender = gender
    p.picture = picture
    p.save()
    return p

def add_friend(user,friends):
    f = FriendProfile.objects.get_or_create(user=user)[0]
    f.friend.add(*friends)
    return f

def add_post(user,picture,caption):
    post = Post.objects.create(user=user,picture=picture,caption=caption)
    return post

if __name__ == '__main__':
    print('Starting Musicial population script...')
    populate()
