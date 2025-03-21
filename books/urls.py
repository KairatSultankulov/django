from django.urls import path
from  . import views

urlpatterns = [
    path('aboutme', views.about_me),
    path('mypet', views.my_pet),
    path('time', views.time),
    path("", views.books_list),
    path("book_list/<int:id>/", views.books_detail),
    path("search/", views.SearchBookView.as_view(), name="search"),
]