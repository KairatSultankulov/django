from django.urls import path
from  . import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:id>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('add_recipe/', views.RecipeCreateView.as_view(), name='add_recipe'),
    path('add_ingredient/', views.IngredientCreateView.as_view(), name='add_ingredient'),
    path('delete_recipe/<int:id>/', views.RecipeDeleteView.as_view(), name='delete_recipe'),
]