from django.contrib import admin

from webapp.models import Article, Category


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('category_id',)
    list_display = ('id', 'title', 'user_id', )
    list_display_links = ('id', 'title',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
