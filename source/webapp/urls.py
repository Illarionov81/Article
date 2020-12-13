from django.urls import path, include
from webapp.views.article_views import ArticleView, Articles, ArticleUpdate, ArticleDelete, ArticleCreate


app_name = 'webapp'

urlpatterns = [
    path('', Articles.as_view(), name='articles_view'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),

 ]

