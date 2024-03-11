from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/bloghome.html')

def post(request, slug):
    return render(request, 'blog/blogpost.html')