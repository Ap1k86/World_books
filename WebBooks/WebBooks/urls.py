from django.contrib import admin
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    # Два варианта пути.
    path('catalog/books', views.BookListViews.as_view(), name='books'),
    # re_path(r'^books/$', views.BookListViews.as_view(), name='books'),
    # Маршрут просмотра определенной книги
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # Два варианта пути. (Сам)
    path('catalog/authors', views.AuthorListView.as_view(), name='authors'),
    # re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    # Маршрут просмотра определенного автора. (Сам)
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='author-detail'),
]
