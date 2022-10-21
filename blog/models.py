import json
from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from django.core.mail import EmailMessage
from portfolio.settings import EMAIL_HOST_USER
from celery import shared_task


class Blog(models.Model):
    title = models.CharField(max_length=200)
    time_pub = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    descript = RichTextUploadingField(blank=True, null=True)
    slug = models.SlugField(null=True, unique=True, blank=True, max_length=200)
    visit_counter = models.IntegerField(default=0)
    is_draft = models.BooleanField(default=True, null=True, blank=True)

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

    def save(self, *args, **kwargs):
        try:
            email_body =f"Congrats, you've got new subscriber<br>Name: {self.full_name}"
            email = "yalchinmammadli@yalchin.info"

            msg = EmailMessage(
                "New Subscription",
                email_body,
                EMAIL_HOST_USER,
                [email]
            )
            msg.content_subtype = "html"
            msg.send()
        except:
            print("Couldn't send the email")
        
        return super().save(*args, **kwargs)



class Notification(models.Model):

    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    subject = "New article has just been posted!"

    def __str__(self):
        return self.post.title

    def save(self,*args, **kwargs):
        # send notification to subscribers on the background
        send_notification_2_subs.delay(self.post.id, self.subject)

        return super().save(*args, **kwargs)


class Comment(MPTTModel):
    content = RichTextField(blank=True, null=True, config_name='default')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')
    up_votes = models.ManyToManyField(User, related_name="up_votes")
    down_votes = models.ManyToManyField(User, related_name="down_votes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)
    boss_notified = models.BooleanField(default=False)
    
    class MPTTMeta:
        order_insertion_by = ['-created_at']

    @property
    def net_votes(self):
        return self.up_votes.all().count() - self.down_votes.all().count()
    
    def __str__(self):
        return f"{self.blog.title} - {self.content} - {self.owner.username}"
    
    def save(self, *args, **kwargs):
        
        if not self.boss_notified:
            try:
                email_body =f"New comment to a blog post called {self.blog.title} by:<br>{self.owner}<br>\
                Go to https://yalchin.info/owner to verify the comment<br>\
                Comment:<br>{self.content}"
                email = "yalchinmammadli@yalchin.info"

                msg = EmailMessage(
                    f"New Comment by {self.owner}",
                    email_body,
                    EMAIL_HOST_USER,
                    [email]
                )
                msg.content_subtype = "html"
                msg.send()
                self.boss_notified = True
            except:
                print("Couldn't send the email")
            
        if self.parent and self.is_verified:
            post_url = self.blog.get_absolute_url()
            comment_owner_email = self.parent.owner.email
            try:
                email_body =f"New reply to your comment added you can \
                find it in the comment section of this blog post <br>\
                Your comment:<br>{self.parent.content}<br>\
                Replied by:<br>{self.owner}\
                Go to https://yalchin.info/{post_url} to the reply<br>\
                "
                email = comment_owner_email

                msg = EmailMessage(
                    f"New Reply by {self.owner}",
                    email_body,
                    EMAIL_HOST_USER,
                    [email]
                )
                msg.content_subtype = "html"
                msg.send()
            except:
                print("Couldn't send the email")
        
        return super().save(*args, **kwargs)


@shared_task
def send_notification_2_subs(post_id, subject):
    subs_objs = Subscription.objects.all()

    for sub_obj in subs_objs:

        try:
            post_obj = Blog.objects.get(id=post_id)
            post_url = post_obj.get_absolute_url()
            post_title = post_obj.title
            email_body =f'Hello, dear <b>{sub_obj.full_name}</b>,<br>New article on <b>"{post_title}"</b> has just been posted on\
            Yalchin`s Blog!<br>See the post by following link below:<br>\
            Link to post: https://yalchin.info{post_url}<br>Thanks for your interest!<br>Best,<br>Yalchin Mammadli'
            
            email = sub_obj.email

            msg = EmailMessage(
                subject,
                email_body,
                EMAIL_HOST_USER,
                [email]
            )
            msg.content_subtype = "html"
            msg.send()

        except:
            print("Couldn't send the email")