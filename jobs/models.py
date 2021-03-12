from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=400)
    start_time = models.DateTimeField(null=True)
    def __str__(self):
        return self.title
