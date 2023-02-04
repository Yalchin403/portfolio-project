from django.contrib import admin
from .models import *
from portfolio.mixins import CeleryExportMixin
from .resources import (
    BlogResource,
    ImageResource,
    SubscriptionResource,
    NotificationResource,
    CommentResource,
)
from import_export_celery.admin_actions import create_export_job_action


@admin.register(Blog)
class BlogAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Blog model to improve default admin functionalities"""

    resource_classes = [BlogResource]

    list_display = [
        "id",
        "title",
        "time_pub",
        "image",
        "descript",
        "slug",
        "visit_counter",
        "is_draft",
    ]

    list_display_links = [
        "id",
        "title",
        "time_pub",
        "image",
        "descript",
        "slug",
        "visit_counter",
        "is_draft",
    ]

    actions = (create_export_job_action,)


@admin.register(Image)
class ImageAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Image model to improve default admin functionalities"""

    resource_classes = [ImageResource]

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

    actions = (create_export_job_action,)


@admin.register(Subscription)
class ImageAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Subscription model to improve default admin functionalities"""

    resource_classes = [SubscriptionResource]

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

    actions = (create_export_job_action,)


@admin.register(Notification)
class NotificationAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Notification model to improve default admin functionalities"""

    resource_classes = [NotificationResource]

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

    actions = (create_export_job_action,)


@admin.register(Comment)
class CommentAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Comment model to improve default admin functionalities"""

    resource_classes = [CommentResource]

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

    actions = (create_export_job_action,)
