from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Blog, Subscription
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.order_by('-time_pub').all()
        per_page = 5
        paginator = Paginator(blogs, per_page)
        num_of_pages = paginator.num_pages
        page_number = request.GET.get('page')
        if not page_number:
        	page_number = "1"
       	elif int(page_number) > num_of_pages:
       		page_number=str(num_of_pages)
       	elif int(page_number) < 1:
       		page_number = "1"

        page_obj = paginator.get_page(page_number)
        context = {'page_obj':page_obj, "page_num":page_number, "num_of_pages":num_of_pages}
        return render(request, 'blog/blogs.html', context)

        
class DetailView(View):
    def get(self, request, slug):
        d_blog = get_object_or_404(Blog, slug=slug)
        context = {'d_blog': d_blog}
        return render(request, 'blog/detail.html', context)


class SearchView(View):
	def get(self, request):
		no_result = False
		if request.GET.get('search'):
			search_list = request.GET.get('search').split(' ')
			for search in search_list:
				objs = Blog.objects.order_by('-time_pub').filter(
					Q(title__icontains=search) | Q(descript__icontains=search)
					).distinct()

			no_result = False
			
			if not objs:
				no_result = True

		else:
			messages.error(request, 'You cannot leave empty...')
			searched = "Search Blog Post"
			objs = Blog.objects.all()

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

		context = {'page_obj':page_obj, 
		"page_num":page_number, 
		"num_of_pages":num_of_pages, 
		"searched": searched,
		"no_result": no_result}
		return render(request, 'blog/blogs.html', context)


class SubscribeView(View):
	def post(self, request):
		full_name = request.POST.get('fullname')
		email = request.POST.get('email')

		if full_name and email:
			if Subscription.objects.filter(email=email).exists():
				messages.error(request, 'You have already subscribed...')
				return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

			sub_obj = Subscription(email=email, full_name=full_name)
			sub_obj.save()
			return render(request, 'blog/subs_thank.html')

		else:
			messages.error(request, 'You can not leave the form field/s empty...')
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))