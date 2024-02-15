from django.contrib import admin
from .models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """ModelAdmin for Blog model to improve default admin functionalities"""

    list_display = [
        "id",
        "title",
        "time_pub",
        "image",
        "slug",
        "visit_counter",
        "is_draft",
    ]

    list_display_links = [
        "id",
        "title",
        "time_pub",
        "image",
        "slug",
        "visit_counter",
        "is_draft",
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """ModelAdmin for Image model to improve default admin functionalities"""

    list_display = [
        "id",
        "img_name",
        "img",
    ]

    list_display_links = [
        "id",
        "img_name",
        "img",
    ]


@admin.register(Subscription)
class ImageAdmin(admin.ModelAdmin):
    """ModelAdmin for Subscription model to improve default admin functionalities"""

    list_display = [
        "id",
        "email",
        "full_name",
    ]

    list_display_links = [
        "id",
        "email",
        "full_name",
    ]


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """ModelAdmin for Notification model to improve default admin functionalities"""
    list_display = [
        "id",
        "post",
        "subject",
    ]

    list_display_links = [
        "id",
        "post",
        "subject",
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ModelAdmin for Comment model to improve default admin functionalities"""

    list_display = [
        "id",
        "content",
        "owner",
        "blog",
        "parent",
        "created_at",
        "updated_at",
        "is_verified",
        "boss_notified",
    ]

    list_display_links = [
        "id",
        "content",
        "owner",
        "blog",
        "parent",
        "created_at",
        "updated_at",
        "is_verified",
        "boss_notified",
    ]
