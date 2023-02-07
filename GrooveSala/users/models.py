from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') 
    contact = models.CharField(max_length=25, null=True, blank=True)
    members=models.IntegerField(null=True, blank=True)
    musical_genre=models.CharField(max_length=100, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images', null=True, blank=True)
