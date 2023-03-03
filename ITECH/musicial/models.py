from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    age = models.IntegerField(blank=False)
    gender = models.CharField(max_length=50,blank=False)
    picture = models.ImageField(upload_to='profile_images',blank=False)

    def __str__(self):
        return self.user.username



#any form field validators