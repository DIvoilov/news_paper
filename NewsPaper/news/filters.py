import datetime

import django_filters
from django import forms
from django_filters import *
from .models import Post
from django.db import models
from django_filters.widgets import *
from datetime import datetime


class NewsFilter(FilterSet):
    @property
    def qs(self):
        parent = super().qs
        type_n = 'N'
        return parent.filter(type=type_n)


class ArticleFilter(FilterSet):
    @property
    def qs(self):
        parent = super().qs
        type_n = 'A'
        return parent.filter(type=type_n)


class NewsFilterSearch(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__user__username': ['icontains'],
            'date_add': ['gt'],
        }

        filter_overrides = {
            models.DateTimeField: {
                'filter_class': django_filters.DateTimeFilter,
                'extra': lambda f: {
                    'widget': forms.SelectDateWidget(
                        years=[i for i in range(datetime.now().year, datetime.now().year - 100, -1)])
                }
            }
        }

    @property
    def qs(self):
        parent = super().qs
        type_n = 'N'
        return parent.filter(type=type_n)


class ArticleFilterSearch(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__user__username': ['icontains'],
            'date_add': ['gt'],
        }

        filter_overrides = {
            models.DateTimeField: {
                'filter_class': django_filters.DateTimeFilter,
                'extra': lambda f: {
                    'widget': forms.SelectDateWidget(
                        years=[i for i in range(datetime.now().year, datetime.now().year - 100, -1)])
                }
            }
        }

    @property
    def qs(self):
        parent = super().qs
        type_n = 'A'
        return parent.filter(type=type_n)
