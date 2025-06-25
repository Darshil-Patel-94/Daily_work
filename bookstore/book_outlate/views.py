from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Book

def index(request):
    books = Book.objects.all().values()
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render({
        "books":books   
    }))

def book_details(request , id):
    books = Book.objects.get(pk=id)
    temp = loader.get_template('book_details.html')
    return HttpResponse(temp.render({
        "title" : books.title,
        "author" : books.author,
        "ratting" : books.ratting,
        "is_bestselling" : books.is_bestselling
    }))