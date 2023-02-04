from django.contrib import admin
from accounts.models import Profile
from portfolio.mixins import CeleryExportMixin
from .resources import ProfileResource, UserResource
from import_export_celery.admin_actions import create_export_job_action
from django.contrib.auth.models import User


admin.site.unregister(User)


@admin.register(Profile)
class ProfileAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for Profile model to improve default admin functionalities"""

    resource_classes = [ProfileResource]

    list_display = [
        "id",
        "admin",
        "profile_photo",
    ]

    list_display_links = [
        "id",
        "admin",
        "profile_photo",
    ]

    actions = (create_export_job_action,)


@admin.register(User)
class ProfileAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for User model to improve default admin functionalities"""

    resource_classes = [UserResource]

    list_display = [
        "id",
        "username",
        "email",
    ]

    list_display_links = [
        "id",
        "username",
        "email",
    ]

    actions = (create_export_job_action,)
