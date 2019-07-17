from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 3
    template_name = 'articlesApp/article_list.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articlesApp/article_new.html'
    fields = ('title', 'body', 'author','lat', 'lng')


def post_detail(request, year,month, day, post):
    article  = get_object_or_404(Article,slug=post,
                    created__year=year,
                    created__month=month,
                    created__day=day)
    return render (request, 
            'articlesApp/article_detail.html',
                {'post' : article})

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articlesApp/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articlesApp/article_delete.html'
    success_url = reverse_lazy('article_list')

