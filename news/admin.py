from django.contrib import admin

from .models import Reporter, Article


@admin.register(Reporter)
class ReporterAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass
