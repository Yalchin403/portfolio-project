from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    descript = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, unique=True, blank=True)
    visit_counter = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.descript[:250] + '...'
    
    def pretty_pub(self):
        return self.time_pub.strftime('%b %e %Y')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Image(models.Model):
    img_name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.img_name


class Subscription(models.Model):
    email = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name