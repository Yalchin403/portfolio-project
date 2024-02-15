from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """ModelAdmin for User model to improve default admin functionalities"""

    list_display = [
        "id",
        "title",
        "description",
        "company_name",
        "date_from",
        "date_to",
    ]

    list_display_links = [
        "id",
        "title",
        "description",
        "company_name",
        "date_from",
        "date_to",
    ]
