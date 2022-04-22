from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='jobs'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('forms/contact/', views.ContactView.as_view(), name='contact')
    ]
