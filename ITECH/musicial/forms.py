from django import forms
from django.contrib.auth.models import User
from musicial.models import UserProfile

#forms for all the user details we need
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('age','gender','picture')