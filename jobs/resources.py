from import_export import resources
from .models import Job


class JobResource(resources.ModelResource):
    """Resource for Job admin import/export resource"""

    class Meta:
        model = Job
        chunk_size = 5000


