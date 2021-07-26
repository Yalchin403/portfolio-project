from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import CreateUserForm, AccountForm
from .utils import user_karma, auto_subscribe
from .models import Profile
from django.contrib import messages


class SignUp(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('jobs:home')
        else:
            form = CreateUserForm()
            context = {'form': form}
            return render(request, "accounts/signup.html", context)
    def post(self, request):

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            user_obj = User.objects.get(username=user)
            auto_subscribe(user_obj)
            messages.success(request, f'{user}, account has been successfully created for you')
            return redirect('accounts:signIn')
        else:
            return render(request, 'accounts/signup.html', {'form':form})

class SignIn(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('jobs:home')
        return render(request, 'accounts/signin.html')
        
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_  = request.GET.get('next')
            if next_:
                return redirect(f'https://yalchin.info/{next_}') 
            return redirect('jobs:home')
            
        else:
            messages.info(request, 'Username or password invalid')
            return render(request, 'accounts/signin.html')

        messages.error(request, "Your account is not active!")
        return render(request, 'accounts/signin.html')


class SignOut(View):
    def get(self, request):
        logout(request)
        return redirect('accounts:signIn')
    
    
class Profile(View):
    
    def get(self, request):
        if request.user.is_authenticated:
            user_obj = request.user
            username = user_obj.username
            email = user_obj.email
            profile_photo = user_obj.profile.profile_photo
            karma = user_karma(user_obj)
            form = AccountForm(initial={'username': username, 'email': email, 'profile_photo':profile_photo})
            context = {'form':form,
                       "karma": karma}
            return render(request, 'accounts/account.html', context)
        return redirect('accounts:signIn')
    
    def post(self, request):
        if request.user.is_authenticated:
            user_obj = request.user
            form = AccountForm(request.POST, request.FILES)
            is_clear = request.POST.get("profile_photo-clear")
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                current_username = request.user.username
                current_email = request.user.email
                print(current_email, current_username, email, username)
                if not email == current_email or not username == current_username:
                    existing_email = User.objects.filter(email=email).exists()
                    existing_username = User.objects.filter(username=username).exists()
                    if existing_email or existing_username:
                        messages.add_message(request, messages.INFO, 'Email or username already taken...')
                        return redirect("accounts:profile")
                profile_photo = form.cleaned_data['profile_photo']
                
                user_obj.username = username
                user_obj.email = email
                username = user_obj.username
                if profile_photo or is_clear:
                    profile_obj = user_obj.profile
                    profile_obj.profile_photo = profile_photo
                    profile_obj.save()
                user_obj.save()
                
                return redirect("accounts:profile")
            return redirect("accounts:profile")
        return redirect("accounts:singIn")
            
        
        