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
    path('', NewList.as_view(), name='news_list'),
    path('<int:pk>', NewDetail.as_view(), name='post_detail'),
    path('create/', NewCreate.as_view(), name='post_create'),
    path('<int:pk>/edit', NewUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete', NewDelete.as_view(), name='post_delete'),
    path('search/', NewListSearch.as_view(), name='news_search'),
]
