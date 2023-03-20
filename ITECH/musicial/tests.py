from musicial.views import registerPage
from musicial import views
from django.db import DatabaseError
from django.forms import ValidationError
from django.test import Client, TestCase
from django.urls import reverse
from musicial.models import UserProfile
from django.contrib.auth.models import User
from django.db import transaction


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
      #check register successfully 
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
          'first_name': 'Test',
          'last_name': 'User',
          'email': 'testuser@example.com',
          'password': 'testpassword',
          'confirm_password': 'testpassword',
          'age': 25,
          'gender': 'M',
          'picture': 'images/rango.jpg'
      }
       #Post data to register URL
      response = self.client.post(self.register_url,data)
      #check register form
      self.assertEqual(response.status_code,302)
      
      
     
    
