from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name='blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('search', views.SearchView.as_view(), name='search'),
    path('<str:slug>/', views.DetailView.as_view(), name='d_blog'),
    path('user/subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    ]
