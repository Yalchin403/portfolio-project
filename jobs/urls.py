from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='jobs'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    ]
