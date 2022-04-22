from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import Job
from django.core.mail import EmailMessage
from portfolio.settings import EMAIL_HOST_USER
from django.contrib import messages


class HomeView(View):
    def get(self, request):
        jobs = Job.objects.order_by('-start_time')
        return render(request, 'jobs/new_home.html')


class ContactView(View):
    def get(self, request):
        return HttpResponse("Method not allowed!")

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        content = f"""
            Hello, it's {name},
            {message}
            
            Best,
            
            {name}
            {email} 
        """
        # send email

        try:
            email_body = content
            email = "yalchinmammadli@yalchin.info"

            msg = EmailMessage(
                subject,
                email_body,
                EMAIL_HOST_USER,
                [email]
            )
            msg.content_subtype = "html"
            msg.send()

            return HttpResponse("Your message has been sent successfully, thanks for reaching out!", status=200)

        except:
            return HttpResponse("", status=500)
