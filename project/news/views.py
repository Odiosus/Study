from django.views.generic import ListView, DetailView
from .models import *

class PostList(ListView):
    model = Post
    ordering = 'create'
    template_name = 'posts.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'