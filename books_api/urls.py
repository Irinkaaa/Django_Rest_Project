from django.urls import path
from books_api.views import ListBookView, DetailBookView

urlpatterns = [
    path('books/', ListBookView.as_view(), name='books list api'),
    path('books/<int:pk>/', DetailBookView.as_view(), name='book details api'),
]
