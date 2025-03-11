from django.urls import path
from  . import views

urlpatterns = [
    path('aboutme', views.about_me),
    path('mypet', views.my_pet),
    path('time', views.time),
    path("book_list/", views.books_list),
    path("book_list/<int:id>/", views.books_detail),
]