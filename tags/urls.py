from django.urls import path
from . import views

urlpatterns = [
    path('all_tags_books/', views.AllCategoryBookView.as_view(), name='all'),
    path('for_children_tags_book/', views.ForChildrenCategoryBookView.as_view(), name='for_children'),
    path('for_teen_tags_book/', views.ForTeenCategoryBookView.as_view(), name='for_teen'),
]