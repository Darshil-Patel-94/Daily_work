from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="Home"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.post_details,name="post-details")
]