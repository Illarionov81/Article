from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from webapp.forms import ArticleForm
from webapp.models import Article


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article/article_create.html'
    form_class = ArticleForm

    def form_valid(self, form):
        article = form.save(commit=False)
        article.user_id = self.request.user
        article.save()
        form.save_m2m()
        return redirect('webapp:article_view', pk=article.pk)


class ArticleView(LoginRequiredMixin, DetailView):
    template_name = 'article/article.html'
    model = Article


class Articles(LoginRequiredMixin, ListView):
    template_name = 'article/articles_view.html'
    context_object_name = 'articles'
    model = Article


class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    template_name = 'article/article_update.html'
    form_class = ArticleForm
    model = Article
    permission_required = 'webapp.change_article'

    def get_success_url(self):
        return reverse('webapp:article_view', kwargs={'pk': self.object.pk})


class ArticleDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'article/article_delete.html'
    model = Article
    success_url = reverse_lazy('webapp:articles_view')
    permission_required = 'webapp.delete_article'
