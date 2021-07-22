from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name='blog'
urlpatterns = [
    path('', views.BlogView.as_view(), name='blog'),
    path('search', views.SearchView.as_view(), name='search'),
    path('<str:slug>/', views.DetailView.as_view(), name='d_blog'),
    path('user/subscribe/', views.SubscribeView.as_view(), name='subscribe'),
    path('add_comment/<str:pk>/', views.add_comment, name='add_comment'),
    path('add_reply/<str:pk>/<str:b_id>/', views.add_reply, name='add_reply'),
    path('ajax/up_vote/<str:pk>', views.up_vote, name='ajax_upvote'),
    path('ajax/down_vote/<str:pk>', views.down_vote, name='ajax_downvote'),
    ]
