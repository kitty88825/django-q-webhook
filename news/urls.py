"""
news URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import ArticleViewSet


app_name = 'news'

router = SimpleRouter(False)
router.register('article', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
