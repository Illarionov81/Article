from django.urls import path

from api_v1.views import main_categories, categories, articles

app_name = 'api_v1'

urlpatterns = [
    path('main_categories/', main_categories, name='main_categories'),
    path('categories/', categories, name='categories'),
    path('articles/', articles, name='articles'),
]
