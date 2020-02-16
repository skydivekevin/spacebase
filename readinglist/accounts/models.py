from django.db import models
from booklist.models import Book

class User():
  book = models.ManyToManyField(Book)

