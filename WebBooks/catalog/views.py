from django.shortcuts import render
from .models import *
from django.http import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *


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

    # Количество посещений этого view, подсчитанное в переменной session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_instances_available_sales': num_instances_available_sales,
        'num_instances_available_in_stock': num_instances_available_in_stock,
        'num_instances_available_in_order': num_instances_available_in_order,
        'num_authors': num_authors,
        'num_visits': num_visits
    }
    # Отсортировка HTML-шаблона index.html с данными внутри переменной context.
    return render(request, 'index.html', context=context)


# Класс отображения данных.
class BookListViews(generic.ListView):
    model = Book
    paginate_by = 3


# Класс отображения всех книг.
class BookDetailView(generic.DetailView):
    model = Book


# Класс отображения всех авторов. (Сам)
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


# Класс отображения всех авторов. (Сам)
class AuthorDetailView(generic.DetailView):
    model = Author


# Универсальный класс представления списка книг, находящихся в заказе у текущего пользователя.
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='0').order_by('due_back')


def authors_add(request):
    author = Author.objects.all()
    authorsform = AuthorsForm()
    return render(request, 'catalog/authors_add.html', {'form': authorsform, 'author': author})


def create(request):
    if request.method == 'POST':
        author = Author()
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death')
        author.save()
        return HttpResponseRedirect('/authors_add/')


def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect('/authors_add/')
    except Author.DoesNotExist:
        return HttpResponseNotFound('<h2>Автор не найден</h2>')


def edit(request, id):
    author = Author.objects.get(id=id)
    if request.method == 'POST':
        author.first_name = request.POST.get('first_name')
        author.last_name = request.POST.get('last_name')
        author.date_of_birth = request.POST.get('date_of_birth')
        author.date_of_death = request.POST.get('date_of_death')
        author.save()
        return HttpResponseRedirect('/authors_add/')
    else:
        return render(request, 'edit.html', {'author': author})
