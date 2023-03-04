from django.shortcuts import render
from django.http import *

# Create your views here.


# Главная
def index(request):
    return HttpResponse("Главная страница сайта 'Мир Книг!'")
