from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def contact(request):
    messages.success(request, "Welcome to cantact us..happy to hear from you.")
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone)< 10 or len(content) < 4:
            messages.warning(request, "please fill the form correctly")
        
        else:
           contact = Contact(name = name, email = email, phone = phone, content = content)
           contact.save()
           messages.success(request, "your form was sent successfully")
        
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')


