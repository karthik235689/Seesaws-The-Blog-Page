from django.urls import path
from . import views
urlspattern=[
    path("",views.staring_page,name="starting_page"),
    path("posts",views.posts,name="posts"),
    path("posts/<slug:slug>",views.single_post,name="post_details_page") #/posts/my-first-post
]