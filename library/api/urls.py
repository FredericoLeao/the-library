from django.urls import path
from library.api import (
    AuthorsAPIView,
    AuthorAPIView,
    CategoriesAPIView,
    CategoryAPIView,
    BooksAPIView,
    BookAPIView,
)


urlpatterns = [
    path('authors/', AuthorsAPIView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
    path('books/', BooksAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),
]