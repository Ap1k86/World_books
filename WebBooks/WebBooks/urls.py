from django.contrib import admin
from django.urls import path, re_path, include
from catalog import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    # Два варианта пути.
    # path('catalog/books', views.BookListViews.as_view(), name='books'),
    re_path(r'^books/$', views.BookListViews.as_view(), name='books'),
    # Снова 2 пути.
    # Маршрут просмотра определенной книги
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    # Два варианта пути.
    # path('catalog/authors', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'),

    # Маршрут просмотра определенного автора. (Сам)
    re_path(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('authors_add/', views.authors_add, name='authors_add'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('create/', views.create, name='create')
]

urlpatterns += [
    # Добавление URL-адреса для входа в систему.
    path('accounts/', include('django.contrib.auth.urls')),
    path('catalog/', include('catalog.urls')),
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
