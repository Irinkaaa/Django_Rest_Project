from django.urls import path

from books.views import index

urlpatterns = [
    path('', index, name='book index'),
]