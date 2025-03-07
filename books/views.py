from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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