from django.urls import path
from  . import views

urlpatterns = [
    path('aboutme', views.AboutMeView.as_view(), name='aboutme'),
    path('mypet', views.MyPetView.as_view(), name='mypet'),
    path('time', views.TimeView.as_view(), name='time'),
    path("", views.BookListView.as_view(), name='book_list'),
    path("book_list/<int:id>/", views.BookDetailView.as_view(), name='book_detail'),
    path("search/", views.SearchBookView.as_view(), name="search"),
]