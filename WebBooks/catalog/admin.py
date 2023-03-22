from django.contrib import admin
from .models import *


# Определения к классу администратор.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


# Встроенное редактирование связных записей.
class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance


# Регистрируем классы администратора книг.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author')
    # Для одновременного отображения таблицы list_display и list_filter.
    inlines = [BooksInstanceInLine]


# Регистрируем классы администратора для экземпляров книг.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    # Кака-то непонятная штука вышла:)
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Статус и окончание его действия', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )


# Register your models here.
# admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
# не используем т.к. создали классы @admin.register(Book) и @admin.register(BookInstance)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Status)
