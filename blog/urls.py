from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('<int:blog_id>/', views.DetailView.as_view(), name='d_blog'),
    ]
