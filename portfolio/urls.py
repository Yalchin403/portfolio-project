from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

admin.autodiscover()
admin.site.enable_nav_sidebar = False

handler404 = 'blog.views.error_404'

urlpatterns = [
    path('owner/', admin.site.urls),
    path('', include('jobs.urls')),
    path('blog/', include('blog.urls'), name='blog'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path(r'^ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

