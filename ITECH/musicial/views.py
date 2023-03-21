from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout as django_logout
from musicial.forms import UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from musicial.models import UserProfile, FriendProfile, Post, Comment, FriendRequest, Playlist, Song
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control
import base64
import requests
from datetime import date
import json
# Create your views here.

def index(request):
    return render(request,'musicial/homepage.html')
  
def noSuchAccount(request):
    return render(request,'musicial/NoAccount.html')

def invalidLogin(request):
    return render(request,'musicial/invalidLogin.html')

def userExists(request):
    return render(request,'musicial/userExists.html')

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
            post.save() #save the post
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
        current_user_friends = FriendProfile.objects.get_or_create(user=current_user)[0]
        context_dict = {'posts':[]}
        
        posts = [Post.objects.filter(user=f) for f in current_user_friends.friend.all()]
        posts = [p for post in posts for p in post.all()]
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
    context_dict = {}
    if request.method == 'POST':
        picture = request.FILES['picture']
        caption = request.POST.get('caption')
        if caption:
            p = Post.objects.create(user=UserProfile.objects.get(user=request.user),picture=picture,caption=caption)
            p.save()
            context_dict['status'] = 'Uploaded'
        else:
            p = Post.objects.create(user=UserProfile.objects.get(user=request.user),picture=picture)
            p.save()
            context_dict['status'] = 'Uploaded'
    
    return render(request,'musicial/createPage.html',context=context_dict)

@csrf_exempt
def userSocialPage(request):
    context_dict = {'requests':[]}
    if request.method == 'POST':
        if 'friending' in request.POST.keys():
            #create new friend request
            user = UserProfile.objects.get(user=User.objects.get(username=request.POST['friending']))
            f_req = FriendRequest.objects.create(sender=UserProfile.objects.get(user=request.user),receiver=user)
        if 'accept' in request.POST.keys():
            #accept friend request
            user1, user2 = UserProfile.objects.get(user=User.objects.get(username=request.POST['accept'])), UserProfile.objects.get(user=request.user)
            friendlist1, friendlist2 = FriendProfile.objects.get_or_create(user=user1)[0], FriendProfile.objects.get_or_create(user=user2)[0]
            friendlist1.friend.add(user2)
            friendlist2.friend.add(user1)
            FriendRequest.objects.filter(sender=UserProfile.objects.get(user=User.objects.get(username=request.POST['accept'])),receiver=UserProfile.objects.get(user=request.user)).delete()
        if 'reject' in request.POST.keys():
            #reject friend request
            FriendRequest.objects.filter(sender=UserProfile.objects.get(user=User.objects.get(username=request.POST['reject'])),receiver=UserProfile.objects.get(user=request.user)).delete()

        friend_query = request.POST.get('friend-query')
        try:
            user = User.objects.get(username=friend_query)
            user = UserProfile.objects.get(user=user)
            current_friendlist = FriendProfile.objects.filter(user=UserProfile.objects.get(user=request.user))
            is_friend = False
            for f in current_friendlist[0].friend.all():
                if user.user.username == f.user.username: # check if friend is already in friendlist
                    is_friend = True
                    break
            check_req_sent  = FriendRequest.objects.filter(sender=UserProfile.objects.get(user=request.user),receiver=user)
            check_req_received = FriendRequest.objects.filter(sender=user,receiver=UserProfile.objects.get(user=request.user))

            if friend_query == request.user.username: #searching for myself
                context_dict['status'] = 'Me'
            elif is_friend: # already a friend
                context_dict['status'] = 'Friend'
                context_dict['request_to'] = user
            elif check_req_received.count() != 0: #incoming request from user pending
                context_dict['status'] = 'Received'
                context_dict['request_to'] = user
            elif check_req_sent.count() == 0: # found user to send request
                context_dict['status'] = 'Display'
                context_dict['request_to'] = user
            else: # request already sent
                context_dict['status'] = 'Sent'
                context_dict['request_to'] = user
        except User.DoesNotExist:
            context_dict['status'] = 'Invalid'
        except UserProfile.DoesNotExist:
            context_dict['status'] = 'Invalid'
    
    #see how many friend requests current user has received
    current_user = UserProfile.objects.get(user=request.user)
    received_requests = [FriendRequest.objects.filter(receiver=current_user)]
    received_requests = [fq for req in received_requests for fq in req.all()]
        
    for req in received_requests:
        context_dict['requests'].append({
                'username':req.sender.user.username,
                'picture':req.sender.picture
            })
    #get the friends of the current user
    current_user_friends = FriendProfile.objects.get_or_create(user=current_user)[0]
    friends = [f for f in current_user_friends.friend.all()]
    context_dict['friends'] = friends
    return render(request,'musicial/socialPage.html',context=context_dict)

def userProfilePage(request):
    #get no. of friends
    current_user = UserProfile.objects.get(user=request.user)
    current_user_friends = FriendProfile.objects.get_or_create(user=current_user)[0]
    context_dict = {'num_friends':current_user_friends.get_num_friends(),'posts':[]}
    #get posts of user
    posts = [Post.objects.filter(user=current_user)]
    posts = [p for post in posts for p in post.all()]
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
    return render(request,'musicial/ProfilePage.html',context=context_dict)

@csrf_exempt
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

    if request.method == 'PUT':
        song_data = json.loads(request.body)['song']
        selected_song = Song.objects.get_or_create(songid=song_data['songid'],name=song_data['name'],artist=song_data['artist'],music_url=song_data['music_url'],image_url=song_data['image_url'])[0]
        selected_playlist = Playlist.objects.get(user=UserProfile.objects.get(user=request.user),name=song_data['playlist'])
        selected_playlist.songs.add(selected_song)

    r = requests.get(request_URL,headers={"Authorization":access_token})

    songs = r.json()['tracks']['items']
    context_dict = []
    for i in range(len(songs)):
        artists = ', '.join([ele['name'] for ele in songs[i]['artists']])
        context_dict.append({'id':songs[i]['id'],'name':songs[i]['name'],'artists':artists,'image':songs[i]['album']['images'][1]['url'],'preview_url':songs[i]['preview_url']})
    #getting available playlists for current user
    playlists = Playlist.objects.filter(user=UserProfile.objects.get(user=request.user))
    playlists = [playlist.name for playlist in playlists]
    return render(request,'musicial/songPage.html',context={'songs':context_dict,'data_present':True,'playlists':playlists})

@csrf_exempt
def userPlaylistPage(request):
    context_dict = {}
    songs = []
    if request.method == 'POST':
        if 'disp_playlist' in request.POST.keys():
            disp_playlist = request.POST['disp_playlist']
            disp_playlist = Playlist.objects.filter(name=disp_playlist,user=UserProfile.objects.get(user=request.user))
            disp_songs = [s for ele in disp_playlist.all() for s in ele.songs.all()]
            for song in disp_songs:
                songs.append({'id':song.songid,'name':song.name,'artist':song.artist,'music_url':song.music_url,'image_url':song.image_url})
            return JsonResponse({'songs':songs})
        else:
            playlist_name = request.POST.get('playlist')
            playlist = Playlist.objects.filter(name=playlist_name,user=UserProfile.objects.get(user=request.user))
            if playlist.count() == 0:
                Playlist.objects.create(name=playlist_name,user=UserProfile.objects.get(user=request.user))
                context_dict['status'] = 'Created'
            else:
                context_dict['status'] = 'Present'

    current_user_playlists = Playlist.objects.filter(user=UserProfile.objects.get(user=request.user))
    current_user_playlists = [playlist.name for playlist in current_user_playlists]
    context_dict['playlists'] = current_user_playlists
    return render(request,'musicial/PlaylistPage.html',context=context_dict)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/musicial')

