from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Job
# Create your views here.
class HomeView(View):
    def get(self, request):
        jobs = Job.objects.order_by('-start_time')
        return render(request, 'jobs/home.html', {'jobs': jobs})
