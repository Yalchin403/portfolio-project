from django.contrib import admin
from .models import Blog, Images
from markdownx.admin import MarkdownxModelAdmin
# Register your models her

admin.site.register(Blog)
admin.site.register(Images)