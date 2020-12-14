from django.urls import path, include

from webapp.views import CategoryCreate, Categories, CategoryUpdate, CategoryDelete, CategoryNewsView
from webapp.views.article_views import ArticleView, Articles, ArticleUpdate, ArticleDelete, ArticleCreate
from webapp.views.main_category import MainCategoryCreate, MainCategories, MainCategoryView, MainCategoryUpdate, \
    MainCategoryDelete

app_name = 'webapp'

urlpatterns = [
    path('articles/', Articles.as_view(), name='articles_view'),
    path('article/create', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article_view'),
    path('article/<int:pk>/update', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete', ArticleDelete.as_view(), name='article_delete'),

    path('categories/', Categories.as_view(), name='categories_view'),
    path('category/create', CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/', CategoryNewsView.as_view(), name='category_news'),
    path('category/<int:pk>/update', CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete', CategoryDelete.as_view(), name='category_delete'),

    path('', MainCategories.as_view(), name='main_categories_view'),
    path('main_category/create', MainCategoryCreate.as_view(), name='main_category_create'),
    path('main_category/<int:pk>/', MainCategoryView.as_view(), name='main_category_view'),
    path('main_category/<int:pk>/update', MainCategoryUpdate.as_view(), name='main_category_update'),
    path('main_category/<int:pk>/delete', MainCategoryDelete.as_view(), name='main_category_delete'),

 ]

