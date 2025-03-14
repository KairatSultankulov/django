from django.urls import path
from . import views

urlpatterns = [
    path('all_tags_books/', views.all_category_book, name='all'),
    path('for_children_tags_book/', views.for_children_category_book, name='for_children'),
    path('for_teen_tags_book/', views.for_teen_category_book, name='for_teen'),
]