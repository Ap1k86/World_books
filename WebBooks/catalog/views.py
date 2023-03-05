from django.shortcuts import render
from .models import *
from django.http import *
from django.views import generic

# Create your views here.


# Главная
def index(request):
    # return render(request, 'index.html')
    # Генерация "количеств" некоторых главных объектов.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (Статус = "На складе")
    # Здесь метод 'all()' применен по умолчанию.
    num_instances_available = BookInstance.objects.filter().count()
    num_instances_available_in_stock = BookInstance.objects.filter(status=1).count()
    num_instances_available_sales = BookInstance.objects.filter(status=2).count()
    num_instances_available_in_order = BookInstance.objects.filter(status=3).count()
    # # Авторы книг.
    num_authors = Author.objects.count()

    # Отсортировка HTML-шаблона index.html с данными внутри переменной context.
    return render(request, 'index.html', {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_instances_available_sales': num_instances_available_sales,
        'num_instances_available_in_stock': num_instances_available_in_stock,
        'num_instances_available_in_order': num_instances_available_in_order,
        'num_authors': num_authors,
        # 'num_visits': num_visits
    })


# Класс отображения данных.
class BookListViews(generic.ListView):
    model = Book
