from django.contrib import admin
from django.urls import path, re_path
from catalog import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    # Два варианта пути.
    # path('catalog/books', views.BookListViews.as_view(), name='books'),
    re_path(r'^books/$', views.BookListViews.as_view(), name='books'),

]
