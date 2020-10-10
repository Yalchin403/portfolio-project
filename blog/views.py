from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Blog
# Create your views here.
class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.order_by('-time_pub')
        context = {'blogs': blogs, 'count':0}
        return render(request, 'blog/blogs.html', context)

class DetailView(View):
    def get(self, request, blog_id):
        d_blog = get_object_or_404(Blog, pk=blog_id)
        context = {'d_blog': d_blog}
        return render(request, 'blog/detail.html', context)
