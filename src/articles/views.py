from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = 'articlesApp/article_list.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articlesApp/article_new.html'
    fields = ('title', 'body', 'author','lat', 'lng')

class ArticleDetailView(DetailView):
    model = Article
    fields = ('title', 'body')

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articlesApp/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articlesApp/article_delete.html'
    success_url = reverse_lazy('article_list')

