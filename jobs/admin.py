from django.contrib import admin
from .models import Job
from .resources import JobResource
from portfolio.mixins import CeleryExportMixin
from import_export_celery.admin_actions import create_export_job_action


@admin.register(Job)
class JobAdmin(CeleryExportMixin, admin.ModelAdmin):
    """ModelAdmin for User model to improve default admin functionalities"""

    resource_classes = [JobResource]

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

    actions = (create_export_job_action,)
