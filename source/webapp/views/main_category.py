from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from webapp.forms import MainCategoryForm
from webapp.models import Category, MainCategory


class MainCategoryCreate(CreateView):
    model = MainCategory
    template_name = 'main_category/create_main_category.html'
    form_class = MainCategoryForm

    def form_valid(self, form):
        category = form.save(commit=False)
        category.save()
        return redirect('webapp:main_category_view', pk=category.pk)


class MainCategoryView(DetailView):
    template_name = 'main_category/one_main_category.html'
    model = MainCategory

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        main_category = get_object_or_404(MainCategory, pk=self.kwargs.get('pk'))
        categories = Category.objects.filter(parent_id=main_category.pk)
        context['categories'] = categories
        context['main_category'] = main_category
        return context


class MainCategories(ListView):
    template_name = 'main_category/all_main_categories.html'
    model = MainCategory


class MainCategoryUpdate(UpdateView):
    template_name = 'main_category/main_category_update.html'
    form_class = MainCategoryForm
    model = MainCategory

    def get_success_url(self):
        return reverse('webapp:main_category_view', kwargs={'pk': self.object.pk})


class MainCategoryDelete(DeleteView):
    template_name = 'main_category/delete_main_category.html'
    model = MainCategory
    success_url = reverse_lazy('webapp:main_categories_view')
