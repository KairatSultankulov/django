from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import models
from django.views import generic
from django.urls import reverse_lazy
from .forms import RecipeForm, IngredientForm

class RecipeListView(generic.ListView):
    model = models.Recipe
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipes'

class RecipeDetailView(generic.DetailView):
    model = models.Recipe
    template_name = 'recipes/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, queryset=None):
        return models.Recipe.objects.get(id=self.kwargs['id'])

class RecipeCreateView(generic.CreateView):
    model = models.Recipe
    form_class = RecipeForm
    template_name = 'recipes/add_recipe.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class IngredientCreateView(generic.CreateView):
    model = models.Ingredient
    form_class = IngredientForm
    template_name = 'recipes/add_ingredient.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class RecipeDeleteView(generic.DeleteView):
    model = models.Recipe
    template_name = 'recipes/confirm_delete.html'
    success_url = reverse_lazy('recipe_list')

    def get_object(self, queryset=None):
        return models.Recipe.objects.get(id=self.kwargs['id'])
