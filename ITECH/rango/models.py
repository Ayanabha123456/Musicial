from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128,unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    class Meta:
        app_label = 'rango'
        