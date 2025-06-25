from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Book
from django.db.models import Avg

def index(request):
    books = Book.objects.all().order_by("-ratting")
    num_books = books.count()
    avg_ratting = books.aggregate(Avg("ratting"))
    temp = loader.get_template('index.html')
    return HttpResponse(temp.render({
        "books":books,
        "total_number_of_books" : num_books,
        "avge_rattings_of_all_books" : avg_ratting
    }))

def book_details(request , slug):
    books = Book.objects.get(slug=slug)
    temp = loader.get_template('book_details.html')
    return HttpResponse(temp.render({
        "title" : books.title,
        "author" : books.author,
        "ratting" : books.ratting,
        "is_bestselling" : books.is_bestselling
    }))