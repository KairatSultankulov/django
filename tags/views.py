from django.shortcuts import render
from  . import models
from django.views import generic


class AllCategoryBookView(generic.ListView):
    model = models.Product
    template_name = 'tags/all_category_book.html'
    context_object_name = 'query'



class ForChildrenCategoryBookView(generic.ListView):
    model = models.Product
    template_name = 'tags/for_category_book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='Книги для детей')



class ForTeenCategoryBookView(generic.ListView):
    model = models.Product
    template_name = 'tags/for_teen_category_book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Product.objects.filter(tags__name='книги для подростков')
