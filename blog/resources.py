from import_export import resources
from .models import Blog, Comment, Notification, Subscription, Image
from import_export.admin import ImportExportModelAdmin


class BlogResource(resources.ModelResource):
    """Resource for Blog admin import/export resource"""

    class Meta:
        model = Blog
        chunk_size = 5000


class CommentResource(resources.ModelResource):
    """Resource for Comment admin import/export resource"""

    class Meta:
        model = Comment
        exclude = ("parent",)
        chunk_size = 5000


class NotificationResource(resources.ModelResource):
    """Resource for Notification admin import/export resource"""

    class Meta:
        model = Notification
        chunk_size = 5000


class SubscriptionResource(resources.ModelResource):
    """Resource for Subscription admin import/export resource"""

    class Meta:
        model = Subscription
        chunk_size = 5000


class ImageResource(resources.ModelResource):
    """Resource for Image admin import/export resource"""

    class Meta:
        model = Image
        chunk_size = 5000
