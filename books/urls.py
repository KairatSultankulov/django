from django.urls import path
from  . import views

urlpatterns = [
    path('aboutme', views.about_me),
    path('mypet', views.my_pet),
    path('time', views.time)
]