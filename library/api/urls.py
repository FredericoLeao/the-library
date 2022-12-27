from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from library.api import (
    AuthorsAPIView,
    AuthorAPIView,
    CategoriesAPIView,
    CategoryAPIView,
    BooksAPIView,
    BookAPIView,
)


schema_view = get_schema_view(
    openapi.Info(
        title='The Library API Documentation',
        default_version='v1',
        description='Base URL is http://your_domain.com/api',
        terms_of_service=''
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('documentation/',
         schema_view.with_ui('swagger', cache_timeout=0),
         name='swagger-schema'),
    path('authors/', AuthorsAPIView.as_view()),
    path('authors/lookup/', AuthorsAPIView.as_view()),
    path('authors/<int:pk>/', AuthorAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view()),
    path('categories/<int:pk>/', CategoryAPIView.as_view()),
    path('books/', BooksAPIView.as_view()),
    path('books/<int:pk>/', BookAPIView.as_view()),
]