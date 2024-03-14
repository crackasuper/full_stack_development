from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from . models import Contact
from blog.models import blog
from . models import register

from .forms import LoginForm, SignupForm
# Create your views here.

def home(request):
    allposts = Contact.objects.all()
    return render(request, 'home/home.html',{"allposts": allposts})

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


def search(request):
    query = request.GET['query']
    allposts = blog.objects.filter(title__icontains=query)
    context = {'allposts': allposts}
    return render(request, 'home/search.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user:
                login(request)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form' : form})

def log_out(request):
    logout(request)
    return render('login')

def signup(request):
    if request.method == 'POST':
        form  = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'home/signup.html', {'form': form})
