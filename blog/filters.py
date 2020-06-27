# -*-encoding=utf8 -*-
__author__ = 'Thee'

from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Article


class ArticleFilter(filters.FilterSet):

    title = filters.CharFilter(field_name='title', lookup_expr='contains')
    brief = filters.CharFilter(field_name='brief', lookup_expr='contains')
    content = filters.CharFilter(field_name='content', lookup_expr='contains')

    class Meta:
        model = Article
        fields = ['title', 'content', 'brief']
