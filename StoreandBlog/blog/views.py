from re import template
from sre_constants import SUCCESS
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.detail import DetailView, ListView
from .models import Post
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from .forms import *
from django.views.generic.edit import FormView
from .forms import PostCreationForm, Pos

# Create your views here.

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

class PostDeleteOrUpdateFormView(FormView):
    template_name = 'blog/update_or_delete_post.html'
    form_class = PostChangeOrUpdateForm
    success_url = 'post-list'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


class PostCreationFormView(FormView):
    template_name = 'blog/form.html'
    form_class = PostCreationForm
    success_url = 'post-list'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)

    
