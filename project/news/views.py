from django.views.generic import ListView, DetailView
from .models import *
from .filters import PostFilter
from pprint import pprint
from django.shortcuts import render


class PostList(ListView):
    model = Post
    ordering = '-create'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        pprint(context)
        return context

class PostSearch(PostList):
    template_name = 'search.html'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
