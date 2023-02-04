from django.db import models

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    company_name = models.CharField(max_length=50)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    @property
    def description_bullet_points(self)-> list:
        return  self.description.replace('\n', '').split('-')

    def __str__(self):
        return self.title
    
    @classmethod
    def export_resource_classes(cls):
        from .resources import JobResource

        return {
            "jobs": ("job resources", JobResource)
        }
