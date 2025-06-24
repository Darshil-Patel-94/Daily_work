from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def home(request):
    temp = loader.get_template('home.html')
    return HttpResponse(temp.render())

def posts(request):
    temp = loader.get_template('all-post.html')
    return HttpResponse(temp.render())

def post_details(request):
    pass
