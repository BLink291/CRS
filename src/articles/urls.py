from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleCreateView,
    ArticleDetailView
)

app_name = 'articles'
urlpatterns = [

    path('', ArticleListView.as_view(), name='list'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
        ArticleDetailView.post_detail, name='article_detail'), 

    path('new/',ArticleCreateView.as_view(), name='article_new'),
    

]