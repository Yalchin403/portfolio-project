from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.core.mail import send_mail
from portfolio.settings import EMAIL_HOST_USER
from django.urls import reverse
from django.core.mail import EmailMessage


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

    def get_absolute_url(self):
        return reverse('blog:d_blog', kwargs={'slug':self.slug})

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


class Notification(models.Model):

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    # emails = [sub_obj.email for sub_obj in sub_objs]

    subject = "New article has just been posted!"
    

    def save(self,*args, **kwargs):
        sub_objs = Subscription.objects.all()
        post_url = self.post.get_absolute_url()
        for sub_obj in sub_objs:

            try:

                email_body =f'Hello, dear <b>{sub_obj.full_name}</b>,<br>New article on <b>"{self.post.title}"</b> has just been posted on\
                Yalchin`s Blog!<br>See the post by following link below:<br>\
                Link to post: https://yalchin.info{post_url}<br>Thanks for your interest!<br>Best,<br>Yalchin Mammadli'
                
                email = sub_obj.email

                # send_mail(self.subject, email_body, EMAIL_HOST_USER, [email], fail_silently = False)

                msg = EmailMessage(
                    self.subject,
                    email_body,
                    EMAIL_HOST_USER,
                    [email]
                )
                msg.content_subtype = "html"
                msg.send()

            except:
                pass

        return super().save(*args, **kwargs)


    


        