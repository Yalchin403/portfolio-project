from blog.models import Comment
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from blog.models import Subscription

def user_karma(user_obj):
    comment_qs = Comment.objects.filter(owner=user_obj)
    net_votes = [comment.net_votes for comment in comment_qs]
    total_karma = sum(net_votes)
    return total_karma

def auto_subscribe(user_obj):
    email = user_obj.email
    username = user_obj.username
    sub_obj = Subscription(email=email, full_name=username)
    sub_obj.save()