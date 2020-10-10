from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=400)
    def __str__(self):
        return self.title
