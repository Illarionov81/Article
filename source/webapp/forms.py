from django import forms

from webapp.models import Article, Category, MainCategory


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'category_id', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'parent_id']


class MainCategoryForm(forms.ModelForm):
    class Meta:
        model = MainCategory
        fields = ['title']
