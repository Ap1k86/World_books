from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


# Модель для хранения жанров книг.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги:", verbose_name="Жанр книги")

    def __str__(self):
        return self.name


# Модель для хранения языков книг.
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name


# Модель для хранения авторов книг.
class Author(models.Model):
    objects = None
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения", verbose_name="Дата рождения", blank=True,
                                     null=True)
    date_of_death = models.DateField(help_text="Введите дату смерти", verbose_name="Дата смерти", null=True, blank=True)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        # Возвращает URL-адрес для доступа к определенному экземпляру книги.
        return reverse('author-detail', args=[str(self.id)])


# Модель для хранения книг.
class Book(models.Model):
    objects = None
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр книги",
                              verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык книги",
                                 verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги",
                                    verbose_name="Автор книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги",
                               verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")

    # Настройка отображения списков в админке.
    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает URL-адрес для доступа к определенному экземпляру книги.
        return reverse('book-detail', args=[str(self.id)])


# Модель для хранения отдельных экземпляров книг и их статуса.
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

    def __str__(self):
        return self.name


# Модель экземпляр книги.
class BookInstance(models.Model):
    objects = None
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер", null=True)
    imprint = models.CharField(max_length=200, help_text="Введите издательство и год выпуска",
                               verbose_name="Издательство")
    status = models.ForeignKey("Status", on_delete=models.CASCADE, help_text="Изменить состоянии экземпляра",
                               verbose_name="Статус экземпляра книги", null=True)
    due_back = models.DateField(help_text="Введите конец срока статуса", verbose_name="Дата окончания статуса",
                                null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Заказчик",
                                 help_text="Выберите заказчика книги")

    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    def __str__(self):
        return '%s %s %s' % (self.inv_nom, self.book, self.status)
