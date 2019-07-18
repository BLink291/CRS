from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify

from django.urls import reverse_lazy
from .models import Article
# Create your views here.

from .forms import NewPostForm

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 3
    template_name = 'articlesApp/article_list.html'


class ArticleCreateView(LoginRequiredMixin ,CreateView):
    model = Article
    template_name = 'articlesApp/article_new.html'
    form_class = NewPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title) 
        response = super(ArticleCreateView, self).form_valid(form)
        return response
    
    success_url = '/articles'

class ArticleDetailView():
    def post_detail(request, year,month, day, post):
        article  = get_object_or_404(Article,slug=post,
                                        created__year=year,
                                        created__month=month,
                                        created__day=day)
        return render (request,'articlesApp/article_detail.html',
                    {'post' : article})

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = 'articlesApp/article_edit.html'

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articlesApp/article_delete.html'
    success_url = reverse_lazy('article_list')

