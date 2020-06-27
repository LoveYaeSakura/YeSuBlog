from django.contrib import admin
from .models import Article, Category
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'brief', 'total_views', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
