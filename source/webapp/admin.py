from django.contrib import admin

from webapp.models import Article, Category, MainCategory


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('category_id',)
    list_display = ('id', 'title', 'user_id', )
    list_display_links = ('id', 'title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'parent_id',)
    list_display_links = ('id', 'title',)


class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(MainCategory, MainCategoryAdmin)
