from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleCreate(CreateView):
    model = Article
    template_name = 'article/article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user_id = self.request.user
        article.save()
        return redirect('webapp:article_view', pk=article.pk)


class ArticleView(DetailView):
    template_name = 'article/article.html'
    model = Article


class Articles(ListView):
    template_name = 'article/articles_view.html'
    context_object_name = 'articles'
    model = Article


class ArticleUpdate(UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    model = Article

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.pk})


class ArticleDelete(DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    success_url = reverse_lazy('webapp:articles_view')
