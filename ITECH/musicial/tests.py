from musicial.views import registerPage
from musicial import views
from django.db import DatabaseError
from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import reverse
from musicial.models import UserProfile,Post
from django.contrib.auth.models import User
from django.db import transaction
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class UserProfileTestCase(TestCase):
    ""
    #Test for register a new normal user
    ""
    def setUp(self):
      self.user = User.objects.create_user(username="user1", password='123456')
      self.profile = UserProfile.objects.create(user=self.user, age=20, gender='Male', picture='images/rango.jpg')
    
    def test_useProfile_creation(self):
      self.assertEqual(self.profile.user.username,"user1")
      self.assertTrue(self.profile.user.check_password('123456'))
      self.assertEqual(self.profile.age, 20)
      self.assertEqual(self.profile.gender, 'Male')
      self.assertEqual(self.profile.gender,'Male')
      self.assertEqual(self.profile.picture.name,'images/rango.jpg') 
    
class RegisterPageTestCase(TestCase):
    def setUp(self):
      self.client=Client()
      self.register_url = reverse('musicial:register')
      #check register unsuccessfully 
    def test_register_user_invalid(self):
      #create a user
      username="user2"
      password="password"
      email="user2@123.com"
      picture='images/rango.jpg'
      data={
        'username':username,
        'password':password,
        'email':email,
        'picture':picture,
      }
      
      #Post data to register URL
      response = self.client.post(self.register_url,data)
      #check register form
      self.assertEqual(response.status_code,200)
      self.assertFalse(User.objects.filter(username=username).exists())
    
    def test_register_user_valid(self):
      data={
          'username': 'testuser',
          'email': 'testuser@example.com',
          'password': 'testpassword',
          'age': 25,
          'gender': 'M',
          'picture': open('ITECH/static/images/rango.jpg','rb')
      }
       #Post data to register URL
      response = self.client.post(self.register_url,data)
      #check register form
      self.assertEqual(response.status_code,302)
      #check if it is registered successfully or not
      self.assertRedirects(response, '/musicial/landing')
      self.assertTrue(User.objects.filter(username="testuser").exists())
    
    def test_register_existing_user(self):
      data={
          'username': 'testuser',
          'email': 'testuser@example.com',
          'password': 'testpassword',
          'age': 25,
          'gender': 'M',
          'picture': open('ITECH/static/images/rango.jpg','rb')
      }
      response = self.client.post(self.register_url, data)
      #register again
      response = self.client.post(self.register_url, data)
      self.assertEqual(response.status_code, 200)
      self.assertContains(response, 'User already exists')
        
class SignInPageTestCase(TestCase):
  def setUp(self):
    self.client=Client()
    self.username ='testuser'
    self.password= 'testpass'
    self.user=User.objects.create_user(
      username=self.username,
      password=self.password,
    )   
    self.profile =UserProfile.objects.create(user=self.user, age=20, gender='Male', picture='images/rango.jpg')
  #test valid input information
  def test_valid_credentials(self):
    url=reverse('musicial:signin')
    data={
      'username':self.username,
      'password':self.password,
    }
    response = self.client.post(url,data)
    self.assertRedirects(response,'/musicial/landing')
   #test wrong password
  def test_invalid_credentials_wrong_password(self):
    url=reverse('musicial:signin')
    data={
      'username':self.username,
      'password':'wrong',
    }
    response = self.client.post(url,data) 
    self.assertContains(response,'Wrong Password')
  #test invalid input information   
  def test_invalid_credentials_input(self):
    url=reverse('musicial:signin')
    data={
      'username':'none',
      'password':'wrong',
    }
    response = self.client.post(url,data)
    self.assertContains(response,'Invalid login details')
    
#Test post page
class CreatePostPageTestCase(TestCase):
  def setUp(self):
    self.client=Client()
    self.username ='testuser'
    self.password= 'testpass'
    self.user=User.objects.create_user(
      username=self.username,
      password=self.password,
    )   
    self.profile =UserProfile.objects.create(user=self.user, age=20, gender='Male', picture='images/rango.jpg')
  
  #Test a successful upload
  def test_upload_picture_with_capture(self):
    url=reverse('musicial:create-post')
    with open('ITECH/static/images/rango.jpg', 'rb') as f:
        picture = SimpleUploadedFile('ITECH/static/images/rango.jpg', f.read(), content_type='image/jpeg')
    data={
      'picture':picture,
      'caption':'caption',
    }
    self.client.login(username=self.username, password=self.password)
    response=self.client.post(url,data)
    self.assertEqual(response.status_code,200)
    self.assertTemplateUsed(response,'musicial/createPage.html')
    self.assertEquals(response.context['status'],'Uploaded')
    
  def test_upload_picture_without_capture(self):
    url=reverse('musicial:create-post')
    with open('ITECH/static/images/rango.jpg', 'rb') as f:
        picture = SimpleUploadedFile('ITECH/static/images/rango.jpg', f.read(), content_type='image/jpeg')
    data={
      'picture':picture,
     
    }
    self.client.login(username=self.username, password=self.password)
    response=self.client.post(url,data)
    self.assertEqual(response.status_code,200)
    self.assertTemplateUsed(response,'musicial/createPage.html')
    self.assertEquals(response.context['status'],'Uploaded')

#Tets like and comment post    
class UserHomepageTestCase(TestCase):
  def setUp(self):
    self.client=Client()
    self.username ='testuser'
    self.password= 'testpass'
    self.user=User.objects.create_user(
      username=self.username,
      password=self.password,
    )   
    self.profile =UserProfile.objects.create(user=self.user, age=20, gender='Male', picture='images/rango.jpg')
    url=reverse('musicial:create-post')
    with open('ITECH/static/images/rango.jpg', 'rb') as f:
        picture = SimpleUploadedFile('ITECH/static/images/rango.jpg', f.read(), content_type='image/jpeg')
    self.post=Post.objects.create(
      user=self.profile,
      picture=picture,
      caption='caption',
    )
    
  def test_userhomepage_POST_like(self):
    #test like the post
    self.client.login(username=self.username, password=self.password)
    response=self.client.post(reverse('musicial:landing'), {'type': 'like', 'picture_id':self.post.id})
    self.assertEqual(response.status_code, 200)
    self.post.refresh_from_db()
    self.assertEqual(self.post.total_likes(), 1)
    
  def test_userhomepage_POST_comment(self):
    #test comment the post
    self.client.login(username=self.username, password=self.password)
    response=self.client.post(reverse('musicial:landing'), {'type': 'comment', 'picture_id':self.post.id, 'comment':'nice'})
    self.assertEqual(response.status_code, 200)
    self.post.refresh_from_db()
    self.assertIn('nice', [comment.body for comment in self.post.comments.all()])
    
  
 
    
