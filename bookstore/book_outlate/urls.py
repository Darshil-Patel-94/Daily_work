from django.urls import path
from . import views


urlpatterns = [
    path("",views.index , name="home"),
    path("book-details/<slug:slug>",views.book_details,name="book_details_page")
]