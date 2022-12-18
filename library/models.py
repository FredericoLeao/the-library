from django.db import models
from base_model import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=255)


class Category(BaseModel):
    name = models.CharField(max_length=255)


class Book(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1500, null=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    isbn = models.CharField(max_length=20, unique=True, null=True)
    cover = models.ImageField(upload_to='uploads/', null=True)
