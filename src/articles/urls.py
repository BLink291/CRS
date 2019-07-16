from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
)

app_name = 'articles'
urlpatterns = [

    path('', ArticleListView.as_view(), name='list'),

    path('<int:pk>/edit/',
        ArticleUpdateView.as_view(), name='article_edit'), 
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        ArticleDetailView.as_view(), name='article_detail'), 
    path('<int:pk>/delete/',
        ArticleDeleteView.as_view(), name='article_delete'), 

    path('new/', ArticleCreateView.as_view(), name='article_new'),
    

]