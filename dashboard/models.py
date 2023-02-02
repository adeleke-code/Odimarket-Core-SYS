from django.db import models
from accounts.models import User



# Create your models here.

class Profile(models.Model):
    user = models.CharField(max_length=150, unique=True, null=False, blank=False)
    name = models.CharField(max_length=200)
    profile_picture = models.ImageField(blank=True, upload_to='image/')
    location = models.CharField(max_length=200)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.name
from django.db import models


class Post(models.Model):
    content = models.TextField(blank=False)
    picture = models.ImageField(blank=True, upload_to='image/')
    author = models.CharField(max_length=150, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content


class Catalogue(models.Model):
    product = models.CharField(max_length=250)
    picture = models.ImageField(blank=True, upload_to='image/')
    description = models.TextField(blank=False)
    owner = models.CharField(max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.product

class DirectMessage(models.Model):
    content = models.TextField(blank=False)
    author = models.ForeignKey(User,
    related_name='client_message', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content



