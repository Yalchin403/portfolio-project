from import_export import resources
from .models import User, Profile


class UserResource(resources.ModelResource):
    """Resource for User admin import/export resource"""

    class Meta:
        model = User
        chunk_size = 5000


class ProfileResource(resources.ModelResource):
    """Resource for Profile admin import/export resource"""

    class Meta:
        model = Profile
        chunk_size = 5000
