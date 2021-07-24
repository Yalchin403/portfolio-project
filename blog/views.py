from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Blog, Subscription, Comment
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.http import JsonResponse
from .forms import CommentForm
from django.contrib.auth.models import User


class BlogView(View):
    def get(self, request):
        blogs = Blog.objects.order_by('-time_pub').all()
        per_page = 6
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
        comment_qs = d_blog.comments.all()
        try:
            if not 'viewed_post_%s' % d_blog.id in request.session:
                d_blog.visit_counter += 1
                request.session['viewed_post_%s' % d_blog.id] = True
                d_blog.save()

        except:
            pass # we don't do anything if user already has viewed the post
        form = CommentForm()
        context = {'form': form, 'd_blog': d_blog, "comments": comment_qs}
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
			objs = Blog.objects.order_by('-time_pub').all()

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
	
def error_404(request, exception):
        return render(request,'blog/error_404.html')
    
def add_comment(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        owner = request.user
        blog_obj = get_object_or_404(Blog, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            if content:
                try:
                    already_exists = Comment.objects.filter(content=content).exists()
                except:
                    already_exists = False
                if not already_exists:
                    comment_obj = Comment(content=content, owner=owner, blog=blog_obj)
                    comment_obj.save()
        comment_qs = blog_obj.comments.all()
        form = CommentForm()
        context = {"scroll":True, "form":form, 'd_blog': blog_obj, "comments": comment_qs}
        return render(request, 'blog/detail.html', context)
    return HttpResponse("Method not allowed or you are not authenticated")
    

def add_reply(request, pk, b_id):
    content = request.POST.get('replyContent')
    comment_obj = get_object_or_404(Comment, pk=pk)
    blog_obj = get_object_or_404(Blog, pk=b_id)
    if request.method == 'POST' and request.user.is_authenticated:
        if content:
            try:
                already_exists = Comment.objects.filter(content=content).exists()
            except:
                already_exists = False
            if not already_exists:
                owner = request.user
                reply_obj = Comment(content=content, owner=owner, parent=comment_obj, blog=blog_obj)
                reply_obj.save()
        form = CommentForm()
        comment_qs = blog_obj.comments.all()
        context = {"scroll":True, "form":form, 'd_blog': blog_obj, "comments": comment_qs}
        return render(request, 'blog/detail.html', context)
    return HttpResponse("Method not allowed or you are not authenticated")

def up_vote(request, pk):
    try:
        username = request.POST.get("user_obj") # username from ajax call
        user_obj = get_object_or_404(User, username=username)
        comment_obj = get_object_or_404(Comment, pk=pk)
        print(user_obj, comment_obj)
    except:
        user_obj = None
        comment_obj = None
        
    if comment_obj and user_obj:
        if user_obj in comment_obj.up_votes.all():
            comment_obj.up_votes.remove(user_obj)
            net_votes = comment_obj.net_votes
            data = {'up_voted': False,
                    'net_votes': net_votes}
            return JsonResponse(data)
        	
        if user_obj in comment_obj.down_votes.all():
            comment_obj.down_votes.remove(user_obj)
        comment_obj.up_votes.add(user_obj)
        net_votes = comment_obj.net_votes
        data = {"up_voted": True,
                "net_votes": net_votes}
        return JsonResponse(data)

    
def down_vote(request, pk):
    try:
        user_obj = request.user
        comment_obj = get_object_or_404(Comment, pk=pk)
    except:
        user_obj = None
        comment_obj = None
        
    if comment_obj and user_obj:
        if user_obj in comment_obj.down_votes.all():
            comment_obj.down_votes.remove(user_obj)
            net_votes = comment_obj.net_votes
            data = {'down_voted': False,
                    'net_votes': net_votes}
            return JsonResponse(data)
        	
        if user_obj in comment_obj.up_votes.all():
            comment_obj.up_votes.remove(user_obj)
        comment_obj.down_votes.add(user_obj)
        net_votes = comment_obj.net_votes
        data = {"down_voted": True,
                "net_votes": net_votes}
        return JsonResponse(data)
