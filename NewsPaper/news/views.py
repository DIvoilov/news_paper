from django.shortcuts import render
from django.views.generic import *
from datetime import datetime
from .models import *


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = 'date_add'
    template_name = 'news.html'
    context_object_name = 'news'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_new'] = None
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
