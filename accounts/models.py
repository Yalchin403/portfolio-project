from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.FileField(upload_to='media', null=True)
    
    def __str__(self):
        return f"{self.admin.username}'s photo"
    
    def save(self, *args, **kwargs):
        if not self.profile_photo:
            self.profile_photo = "media/default.jpg"
        return super().save(*args, **kwargs)
    
@receiver(post_save, sender=User)
def create_user_profile( sender, instance, created, **kwargs ):
    if created:
        Profile.objects.create(admin=instance)