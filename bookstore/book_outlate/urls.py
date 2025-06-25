from django.urls import path
from . import views

urlpatterns = [
    path("",views.index , name="home"),
    path("book-details/<int:id>",views.book_details,name="book_details_page")
]