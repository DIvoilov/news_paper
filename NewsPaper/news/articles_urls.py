from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', ArticleList.as_view(), name='articles_list'),
    path('<int:pk>', ArticleDetail.as_view(), name='post_detail'),
    path('search/', ArticleListSearch.as_view(), name='articles_search'),
    path('create/', ArticleCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', ArticleUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', ArticleDelete.as_view(), name='post_delete'),
]
