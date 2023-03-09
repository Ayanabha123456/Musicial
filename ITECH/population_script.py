import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'ITECH.settings')

import django
django.setup()
from django.contrib.auth.models import User
from musicial.models import UserProfile,FriendProfile

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
        {'username': 'Emma',
         'password': '123456',
         'age': 25,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Noah',
         'password': 'password1',
         'age': 40,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Ava',
         'password': 'qwerty',
         'age': 20,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Mason',
         'password': 'letmein',
         'age': 35,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Sophia',
         'password': 'iloveyou',
         'age': 30,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Ethan',
         'password': '123456',
         'age': 18,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Mia',
         'password': 'password1',
         'age': 45,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Liam',
         'password': 'qwerty',
         'age': 22,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Isabella',
         'password': 'letmein',
         'age': 33,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Oliver',
         'password': 'iloveyou',
         'age': 28,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Charlotte',
         'password': '123456',
         'age': 26, 'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'William',
         'password': 'password1',
         'age': 30,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Amelia',
         'password': 'qwerty',
         'age': 21,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Benjamin',
         'password': 'letmein',
         'age': 32,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Evelyn',
         'password': 'iloveyou',
         'age': 23,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Lucas',
         'password': '123456',
         'age': 37,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Abigail',
         'password': 'password1',
         'age': 24,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Alexander',
         'password': 'qwerty',
         'age': 29,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Emily',
         'password': 'letmein',
         'age': 19,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Daniel',
         'password': 'iloveyou',
         'age': 31,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Lily',
         'password': 'letmein',
         'age': 27,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Elijah',
         'password': 'iloveyou',
         'age': 34,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Chloe',
         'password': 'password1',
         'age': 22,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Logan',
         'password': 'qwerty',
         'age': 29,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Grace',
         'password': '123456',
         'age': 25,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'James',
         'password': 'letmein',
         'age': 31,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Aria',
         'password': 'password1',
         'age': 23,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Henry',
         'password': 'qwerty',
         'age': 26,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Aaliyah',
         'password': 'iloveyou',
         'age': 29,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Jackson',
         'password': '123456',
         'age': 32,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Madison',
         'password': 'letmein',
         'age': 24,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Samuel',
         'password': 'password1',
         'age': 35,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Ella',
         'password': 'qwerty',
         'age': 21,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Oscar',
         'password': 'iloveyou',
         'age': 30,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Victoria',
         'password': '123456',
         'age': 26,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Jacob',
         'password': 'letmein',
         'age': 33,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Natalie',
         'password': 'password1',
         'age': 28,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Caleb',
         'password': 'qwerty',
         'age': 30,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Hannah',
         'password': 'iloveyou',
         'age': 22,
         'gender': 'Female',
         'picture': 'profile_images/music_test_profile.jpg'},
        {'username': 'Wyatt',
         'password': '123456',
         'age': 37,
         'gender': 'Male',
         'picture': 'profile_images/music_test_profile.jpg'}

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
    for profile in profiles:
        print(profile)
        user = add_user(profile['username'],profile['password'])
        if user:
            print(user)
            add_profile(user,profile['age'],profile['gender'],profile['picture'])

    for user,friend_data in user_friends.items():
        add_friend(user,friend_data)
    
    for p in UserProfile.objects.all():
        print(f'-{p}')

    for f in FriendProfile.objects.all():
        print('User: ',f)
        print('Friends: ',f.friend.all())
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

if __name__ == '__main__':
    print('Starting Musicial population script...')
    populate()
