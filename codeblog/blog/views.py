from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("this is blog home page")

def blogpost(request, slug):
    return HttpResponse(f"this is blog post : {slug}")