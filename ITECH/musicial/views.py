from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login
from musicial.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from musicial.models import UserProfile, FriendProfile, Post, Comment
from django.views.decorators.csrf import csrf_exempt
import base64
import requests
from datetime import date
# Create your views here.

def index(request):
    return render(request,'musicial/homepage.html')

def signInPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                user = authenticate(username=username,password=password)
                if user:
                    if user.is_active:
                        login(request,user)
                        return HttpResponseRedirect('landing')
                    else:
                        return HttpResponse("Your Musicial account does not exist")
                else:
                    return HttpResponse('Invalid login details')
            else:
                return HttpResponse('Wrong Password')
        except User.DoesNotExist:
            return HttpResponse('Invalid login details')
        
    else:
        return render(request,'musicial/sign-in.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user:
                return HttpResponse('User already exists')
        except User.DoesNotExist:
            user_form = UserForm(request.POST)
            profile_form = UserProfileForm(request.POST,request.FILES)

            if user_form.is_valid() and profile_form.is_valid():
                user = user_form.save()
                user.set_password(user.password)
                user.save()

                profile = profile_form.save(commit=False)
                profile.user = user

                if 'picture' in request.FILES:
                    print('Picture acquired')
                    profile.picture = request.FILES['picture']
                profile.save()

                user = authenticate(username=username,password=password)
                login(request,user)
                return HttpResponseRedirect('landing')
            else:
                print(user_form.errors,profile_form.errors)
    else:
        return render(request,'musicial/registerPage.html')

@csrf_exempt
def userHomepage(request):
    if request.method == 'POST':
        type_of_request = request.POST['type']
        picture_id = request.POST['picture_id']
        print('Got ',picture_id)
        post = Post.objects.get(id=picture_id)
        if type_of_request == 'like':
            post.likes.add(UserProfile.objects.get(user=request.user))
            return JsonResponse({'likes':str(post.total_likes())+' likes'})
        else:
            #add the new comment
            com = Comment.objects.create(post=post,name=request.user.username,body=request.POST['comment'])
            #retrieve all comments
            comms = Comment.objects.filter(post=post)
            comments = [c.name+' '+c.date_added.strftime("%a %m %y")+' '+c.body+'\n' for c in comms]
            return JsonResponse({'comments':''.join(comments)})
    else:
        #get posts of friends and send to frontend for displaying
        current_user = UserProfile.objects.get(user=request.user)
        current_user_friends = FriendProfile.objects.get(user=current_user)
        posts = [Post.objects.filter(user=f) for f in current_user_friends.friend.all()]
        posts = [p for post in posts for p in post.all()]
        context_dict = {'posts':[]}
        for post in posts:
            comments = [c.name+' '+c.date_added.strftime("%a %m %y")+' '+c.body+'\n' for c in Comment.objects.filter(post=post)]
            context_dict['posts'].append({
                        'id':post.id,
                        'username':post.user.user.username,
                        'time':post.get_date(),
                        'picture':post.picture,
                        'caption':post.caption,
                        'likes': str(post.total_likes()) + ' likes',
                        'comments':''.join(comments)
                    })
        return render(request,'musicial/userhomepage.html',context=context_dict)

def userCreatePostPage(request):
    return render(request,'musicial/createPage.html')

def userSocialPage(request):
    return render(request,'musicial/socialPage.html')

def userProfilePage(request):
    return render(request,'musicial/ProfilePage.html')

def songPage(request):
    #Spotify authorization
    client_id = '350eb16772f243f2a403853b013ed7fe' # Your client id
    client_secret = 'c3440e5b15ce4277a6eb63dd075818bb' # Your secret

    auth_url = 'https://accounts.spotify.com/api/token'
    auth_str = '{}:{}'.format(client_id, client_secret)
    b64_auth_str = base64.b64encode(auth_str.encode()).decode('utf-8')
    headers = {
            'Authorization': 'Basic ' + b64_auth_str
        }
    payload = {
            'grant_type': 'client_credentials'
        }

    response = requests.post(auth_url, headers=headers, data=payload)
    auth_token = response.json()['access_token']
    access_token = 'Bearer '+auth_token

    if request.method == 'POST':
        #Spotify request
        song_query = request.POST.get('song-query')
        filter = request.POST.get('filter')

        if filter == 'track':
            request_URL = "https://api.spotify.com/v1/search?q="+song_query+"&type="+filter+"&include_external=audio&limit=50"
        elif filter == 'genre':
            request_URL = "https://api.spotify.com/v1/search?q=genre:"+song_query+"&type=track&include_external=audio&limit=50"
        elif filter == 'artist':
            request_URL = "https://api.spotify.com/v1/search?q=artist:"+song_query+"&type=track&include_external=audio&limit=50"
        else:
            request_URL = "https://api.spotify.com/v1/search?q=year:"+song_query+"&type=track&include_external=audio&limit=50"
    else:
        request_URL = "https://api.spotify.com/v1/search?q=year:"+str(date.today().year)+"&type=track&include_external=audio&limit=50"

    r = requests.get(request_URL,headers={"Authorization":access_token})

    songs = r.json()['tracks']['items']
    context_dict = []
    for i in range(len(songs)):
        artists = ', '.join([ele['name'] for ele in songs[i]['artists']])
        context_dict.append({'name':songs[i]['name'],'artists':artists,'image':songs[i]['album']['images'][1]['url'],'preview_url':songs[i]['preview_url']})
    return render(request,'musicial/songPage.html',context={'songs':context_dict,'data_present':True})

def userPlaylistPage(request):
    return render('request','musicial/PlaylistPage.html')

