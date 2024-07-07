from django.shortcuts import render
from django.views.generic import *
from datetime import datetime
from .models import *
from .filters import *
from .forms import PostForm
from django.urls import reverse_lazy


# Create your views here.
class NewList(ListView):
    model = Post
    ordering = 'date_add'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_new'] = None
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs


class ArticleList(ListView):
    model = Post
    ordering = 'date_add'
    template_name = 'articles.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['next_new'] = None
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewListSearch(ListView):
    model = Post
    ordering = 'date_add'
    template_name = 'news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilterSearch(self.request.GET, queryset)
        return self.filterset.qs


class ArticleListSearch(ListView):
    model = Post
    ordering = 'date_add'
    template_name = 'articles_search.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ArticleFilterSearch(self.request.GET, queryset)
        return self.filterset.qs


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class NewDetail(PostDetail):
    queryset = Post.objects.filter(type="N")


class ArticleDetail(PostDetail):
    queryset = Post.objects.filter(type="A")


class NewCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.type = 'N'
        return super().form_valid(form)


class ArticleCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        new = form.save(commit=False)
        new.type = 'A'
        return super().form_valid(form)


class NewUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'new_edit.html'

class ArticleUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class NewDelete(DeleteView):
    model = Post
    template_name = 'new_delete.html'
    success_url = reverse_lazy('news_list')

class ArticleDelete(DeleteView):
    model = Post
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')
