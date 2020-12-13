from django import forms

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'category_id', 'image']
