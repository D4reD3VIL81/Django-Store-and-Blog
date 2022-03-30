from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Post
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Post
from django.urls import reverse_lazy


# Putting views here.

class AuthorCreateView(CreateView):
    model = Post
    fields = ['text_01','qouted_text_01','title','post_publish_date']

    def set_author():
        None

    def set_publish_date():
        None

class AuthorUpdateView(UpdateView):
    model = Post
    fields = ['name']

class AuthorDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')

class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/detail_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostListView(ListView):

    model = Post
    template_name = 'blog/list_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

