from django.http import HttpResponse
from django.shortcuts import render
from . models import blog

# Create your views here.

def home(request):
    allposts = blog.objects.all()
    
    return render(request, 'blog/bloghome.html', {"allposts": allposts})

def post(request, slug):
    posts = blog.objects.filter(slug=slug).first()
    context = {"posts" : posts}
    return render(request, 'blog/blogpost.html', context)