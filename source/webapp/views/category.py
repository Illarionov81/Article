from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from webapp.forms import CategoryForm
from webapp.models import Category, Article


class CategoryCreate(CreateView):
    model = Category
    template_name = 'category/category_create.html'
    form_class = CategoryForm

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return redirect('webapp:category_news', pk=category.pk)


class CategoryNewsView(DetailView):
    template_name = 'category/category_news.html'
    model = Category

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        articles = Article.objects.filter(category_id=category.pk)
        context['articles'] = articles
        context['category'] = category
        return context


class Categories(ListView):
    template_name = 'category/categories_view.html'
    model = Category


class CategoryUpdate(UpdateView):
    template_name = 'category/category_update.html'
    form_class = CategoryForm
    model = Category

    def get_success_url(self):
        return reverse('webapp:category_news', kwargs={'pk': self.object.pk})


class CategoryDelete(DeleteView):
    template_name = 'category/category_delete.html'
    model = Category
    success_url = reverse_lazy('webapp:categories_view')
