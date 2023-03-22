from django.urls import path, re_path, include
from catalog import views

urlpatterns = [
    path('', views.index, name="index"),
]

# Используйте include() чтобы добавлять URL из каталога приложения
urlpatterns += [
    #
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed')
]
