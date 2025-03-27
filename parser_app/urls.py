from django.urls import path
from . import views

urlpatterns = [
    path("mybook_list/", views.MybookListView.as_view(), name="mybook_list"),
    path("rezka_list/", views.RezkaFilmListView.as_view(), name="rezka_list"),
    path("parser_form/", views.ParserForm.as_view(), name="parser_form"),
]