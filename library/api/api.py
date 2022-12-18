from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from library.models import (
    Book,
    Author,
    Category,
)
from library.api.serializers import (
    BookSerializer,
    AuthorSerializer,
    CategorySerializer,
)


class BooksAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        ''' Get a list of all Books '''
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ''' Create a new Book '''
        return super().post(request, *args, **kwargs)


class BookAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        ''' Retrieve specified Book's details '''
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ''' Update specified Book '''
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        ''' Update specified Book, partially '''
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ''' Delete specified Book, permanently '''
        return super().delete(request, *args, **kwargs)


class AuthorsAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        ''' Get a list of all Authors '''
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ''' Create a new Author '''
        return super().post(request, *args, **kwargs)


class AuthorAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        ''' Retrieve specified Author's details '''
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ''' Update specified Author '''
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        ''' Update specified Author, partially '''
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ''' Delete specified Author, permanently '''
        return super().delete(request, *args, **kwargs)


class CategoriesAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        ''' Get a list of all Categories '''
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ''' Create a new Category '''
        return super().post(request, *args, **kwargs)


class CategoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        ''' Retrieve specified Category details '''
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ''' Update specified Category '''
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        ''' Update specified Category, partially '''
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        ''' Delete specified Category, permanently '''
        return super().delete(request, *args, **kwargs)
