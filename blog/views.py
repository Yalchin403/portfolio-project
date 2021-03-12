from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Blog
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q


# Create your views here.
class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.order_by('-time_pub').all()
        per_page = 5
        paginator = Paginator(blogs, per_page)
        num_of_pages = paginator.num_pages
        page_number = request.GET.get('page')
        if not page_number:
        	page_number = 1
       	elif int(page_number) > num_of_pages:
       		page_number=str(num_of_pages)
       	elif int(page_number) < 1:
       		page_number = "1"

        page_obj = paginator.get_page(page_number)
        context = {'page_obj':page_obj, "page_num":page_number, "num_of_pages":num_of_pages}
        return render(request, 'blog/blogs.html', context)

        
class DetailView(View):
    def get(self, request, blog_id):
        d_blog = get_object_or_404(Blog, pk=blog_id)
        context = {'d_blog': d_blog}
        return render(request, 'blog/detail.html', context)


class SearchView(View):
	def get(self, request):
		if request.method == "GET":
			if request.GET.get('search'):
				search_list = request.GET.get('search').split(' ')
				for search in search_list:
					objs = Blog.objects.filter(
						Q(title__icontains=search) | Q(descript__icontains=search)
						).distinct()

			else:
				objs = []
				searched = "Search Blog Post"

			per_page = 5
			paginator = Paginator(objs, per_page)
			num_of_pages = paginator.num_pages
			page_number = request.GET.get('page')
			if not page_number:
				page_number = 1
			elif int(page_number) > num_of_pages:
				page_number=str(num_of_pages)
			elif int(page_number) < 1:
				page_number = "1"
			page_obj = paginator.get_page(page_number)
			searched = request.GET.get('search')

			context = {'page_obj':page_obj, "page_num":page_number, "num_of_pages":num_of_pages, "searched": searched}
			return render(request, 'blog/blogs.html', context)