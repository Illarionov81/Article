from django.http import JsonResponse

from webapp.models import MainCategory, Category, Article


def main_categories(request, *args, **kwargs):
    if request.method == 'GET':
        fields = ('pk', 'title',)
        products = MainCategory.objects.values(*fields)
        return JsonResponse(list(products), safe=False)


def categories(request, *args, **kwargs):
    if request.method == 'GET':
        fields = ('pk', 'title', 'parent_id',)
        products = Category.objects.values(*fields)
        return JsonResponse(list(products), safe=False)


def articles(request, *args, **kwargs):
    if request.method == 'GET':
        fields = ('pk', 'title', 'description', 'category_id', 'user_id', 'image')
        products = Article.objects.values(*fields)
        return JsonResponse(list(products), safe=False)

