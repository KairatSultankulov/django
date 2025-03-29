from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from datetime import datetime
from . import models

class SearchBookView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        query = self.request.GET.get('q')
        cache_key = f'query_{query}'
        books = cache.get(cache_key)
        if not books:
            books = models.Books.objects.filter(title__icontains=query)
            cache.set(cache_key, books, 60 * 15)
        return books

@method_decorator(cache_page(60 * 15), name='dispatch')
class BookDetailView(generic.DetailView):
    model = models.Books
    template_name = 'book_detail.html'
    context_object_name = 'book'

@method_decorator(cache_page(60 * 15), name='dispatch')
class BookListView(generic.ListView):
    model = models.Books
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        books = cache.get('query')
        if not books:
            books = self.model.objects.all()
            cache.set('query', books, 60 * 15)
        return books

@method_decorator(cache_page(60 * 15), name='dispatch')
class AboutMeView(generic.TemplateView):
    template_name = 'about_me.html'

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi! My name is Kairat, I'm 23 years old. I'm always open to new opportunities and strive to grow in various areas of life. I love learning new things, finding creative solutions, and sharing experiences with others.")

@method_decorator(cache_page(60 * 15), name='dispatch')
class MyPetView(generic.TemplateView):
    template_name = 'my_pet.html'

    def get(self, request, *args, **kwargs):
        pet_name = 'REX'
        return HttpResponse(
            f"My pet name is {pet_name}"
            "<img src='https://www.bethowen.ru/upload/iblock/898/8982eee1d576c30e28811046c021a8af.jpg' />"
        )

@method_decorator(cache_page(60 * 15), name='dispatch')
class TimeView(generic.TemplateView):
    template_name = 'time.html'

    def get(self, request, *args, **kwargs):
        current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        return HttpResponse(current_time)
