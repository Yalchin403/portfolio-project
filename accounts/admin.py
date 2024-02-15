from django.contrib import admin
from accounts.models import Profile
from django.contrib.auth.models import User


admin.site.unregister(User)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ModelAdmin for Profile model to improve default admin functionalities"""

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


@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    """ModelAdmin for User model to improve default admin functionalities"""

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
