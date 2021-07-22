from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.FileField(upload_to='media')
    
    def __str__(self):
        return f"{self.admin.username}'s photo"