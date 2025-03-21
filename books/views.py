from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models
from django.views import generic

class SearchBookView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'query'

    def get_queryset(self):
        return models.Books.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def books_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id,
            }
        )

def books_list(request):
    if request.method == "GET":
        query = models.Books.objects.all()
        return render (
            request,
            template_name="book.html",
            context = {
                "query": query,
            }
        )


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Hi! My name is Kairat, I'm 23 years old. I'm always open to new opportunities and strive to grow in various areas of life. I love learning new things, finding creative solutions, and sharing experiences with others.")

def my_pet(request):
    if request.method == "GET":
        pet_name = 'REX'
        return HttpResponse(
            f"My pet name is {pet_name}"
            "<img src='https://www.bethowen.ru/upload/iblock/898/8982eee1d576c30e28811046c021a8af.jpg' />"
        )

def time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
        return HttpResponse(current_time)