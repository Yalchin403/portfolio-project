from django.contrib import admin
from .models import *
# Register your models her

admin.site.register(Blog)
admin.site.register(Image)
admin.site.register(Subscription)
admin.site.register(Notification)
admin.site.register(Comment)